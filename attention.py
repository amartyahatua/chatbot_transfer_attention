from keras.layers import Bidirectional, Concatenate, Permute, Dot, Input, LSTM, Multiply
from keras.layers import RepeatVector, Dense, Activation, Lambda
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.models import load_model, Model
import keras.backend as K
import numpy as np

from faker import Faker
import random
from tqdm import tqdm
from babel.dates import format_date
from nmt_utils import *
from dl_model import *
import matplotlib.pyplot as plt
#%matplotlib inline

m = 640

dataPre = datapreprocessing()

trainset, testset = dataPre.createData()

Tx = 4
Ty = 4

# Defined shared layers as global variables
repeator = RepeatVector(Tx)
concatenator = Concatenate(axis=-1)
densor1 = Dense(10, activation = "tanh")
densor2 = Dense(1, activation = "relu")
activator = Activation(softmax, name='attention_weights') # We are using a custom softmax(axis = 1) loaded in this notebook
dotor = Dot(axes = 1)


def one_step_attention(a, s_prev):

    s_prev = repeator(s_prev)
    concat = concatenator([a,s_prev])
    e = densor1(concat)
    energies = densor2(e)
    alphas = activator(energies)
    context = dotor([ alphas,a])

    return context

def model(Tx, Ty, n_a, n_s, human_vocab_size, machine_vocab_size):

    X = Input(shape=(Tx, human_vocab_size))
    s0 = Input(shape=(n_s,), name='s0')
    c0 = Input(shape=(n_s,), name='c0')
    s = s0
    c = c0

    outputs = []
    a = Bidirectional(LSTM(n_a, return_sequences = True), input_shape = (m, Tx, n_a*2))(X)

    for t in range(Ty):

        context = one_step_attention(a, s)
        s, _, c = post_activation_LSTM_cell(context,initial_state = [s, c])
        out = output_layer(s)
        outputs.append(out)

    model = Model([X, s0, c0], outputs = outputs)
    return model




n_a = 32
n_s = 64
post_activation_LSTM_cell = LSTM(n_s, return_state = True)
output_layer = Dense(23, activation=softmax)
model = model(Tx, Ty, n_a, n_s, 23, 23)
model.summary()
opt = Adam(lr = 0.005, beta_1 = 0.9, beta_2 = 0.999,decay = 0.01)
model.compile(loss = 'categorical_crossentropy', optimizer = opt,metrics = ['accuracy'])
s0 = np.zeros((m, n_s))
c0 = np.zeros((m, n_s))
testset = np.asarray(testset)
outputs = list(testset.swapaxes(0,1))
model.fit([trainset, s0, c0], outputs, epochs=500, batch_size=10)
