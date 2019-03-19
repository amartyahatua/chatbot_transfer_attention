import random, copy, json
import cPickle as pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.optimizers import Adam
# from keras import layers
# import random, copy, json
# from keras import backend as K
import numpy as np
import pandas as pd
from numpy import array
from numpy import argmax


class datapreprocessing(object):


    def __init__(self):
        self.inputdata = pd.read_csv("data_rest.csv", index_col=False)
        self.datevalue = list()
        self.cityvalue = list()
        self.pricevalue = list()
        self.foodvalue = list()
        self.addrvalue = list()
        self.uniquedate = list()
        self.uniquecity = list()
        self.uniquepricrrange = list()
        self.uniquefood = list()
        self.uniqueaddr = list()
        self.onehotinput = list()
        self.date_encoded = list()
        self.city_encoded = list()
        self.pricrrange_encoded = list()
        self.food_encoded = list()
        self.addr_encoded = list()
        self.count = list()
        self.traingingdata = np.zeros((800,50))
        self.testingdata = np.zeros((800,50))
        self.dummylist = np.zeros((1,23))
        self.dummylist = self.dummylist.tolist()
        self.maxlen = 23
        self.onehotoutput = list()

    def oneHotDate(self):
        self.uniquedate = self.inputdata['date'].unique()
        self.datevalue  = array(self.uniquedate)
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(self.datevalue )
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        self.date_encoded = onehot_encoder.fit_transform(integer_encoded)
        #return date_encoded
        print(len(self.date_encoded[0]))

    def oneHotCity(self):
        self.uniquecity = self.inputdata['city'].unique()
        self.cityvalue = array(self.uniquecity)
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(self.cityvalue)
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        self.city_encoded = onehot_encoder.fit_transform(integer_encoded)
        print(len(self.city_encoded[0]))

    def oneHotPricrrange(self):
        self.uniquepricrrange = self.inputdata['pricrrange'].unique()
        self.pricevalue = array(self.uniquepricrrange)
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(self.pricevalue)
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        self.pricrrange_encoded = onehot_encoder.fit_transform(integer_encoded)
        print(len(self.pricrrange_encoded[0]))

    def oneHotFood(self):
        self.uniquefood = self.inputdata['food'].unique()
        self.foodvalue = array(self.uniquefood)
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(self.foodvalue)
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        self.food_encoded = onehot_encoder.fit_transform(integer_encoded)
        print(len(self.food_encoded[0]))

    def oneHotAddr(self):
        self.uniqueaddr = self.inputdata['addr'].unique()
        self.addrvalue = array(self.uniqueaddr)
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(self.addrvalue)
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        self.addr_encoded = onehot_encoder.fit_transform(integer_encoded)
        print(len(self.addr_encoded[0]))

    def createData(self):
        self.oneHotDate()
        self.oneHotCity()
        self.oneHotFood()
        self.oneHotPricrrange()
        self.oneHotAddr()
        for i in range(len(self.inputdata)):
            dateindex = np.where(self.uniquedate == self.inputdata["date"][i])[0][0]
            temp = self.date_encoded[dateindex]
            tempdate = np.pad(temp,(0,(self.maxlen-len(temp))),'constant', constant_values=(0))

            cityindex = np.where(self.uniquecity == self.inputdata["city"][i])[0][0]
            temp = self.city_encoded[cityindex]
            tempcity = np.pad(temp,(0,(self.maxlen-len(temp))),'constant', constant_values=(0))

            priceindex = np.where(self.uniquepricrrange == self.inputdata["pricrrange"][i])[0][0]
            temp = self.pricrrange_encoded[priceindex]
            tempprice = np.pad(temp,(0,(self.maxlen-len(temp))),'constant', constant_values=(0))

            foodindex = np.where(self.uniquefood == self.inputdata["food"][i])[0][0]
            temp = self.food_encoded[foodindex]
            tempfood = np.pad(temp,(0,(self.maxlen-len(temp))),'constant', constant_values=(0))

            addrindex = np.where(self.uniqueaddr == self.inputdata["addr"][i])[0][0]
            temp = self.addr_encoded[addrindex]
            tempaddr = np.pad(temp,(0,(self.maxlen-len(temp))),'constant', constant_values=(0))

            onehotlistouter = list()
            onehotlistoutertest = list()

            for j in range(4):

                #onehotlist = list()

                if (j == 0):
                    #onehotlist.append(tempdate.tolist())
                    onehotlistouter.append(tempdate.tolist())
                    onehotlistoutertest.append(tempcity.tolist())
                if (j==1):
                    #onehotlist.append(tempcity.tolist())
                    onehotlistouter.append(tempcity.tolist())
                    onehotlistoutertest.append(tempprice.tolist())
                if (j==2):
                    #onehotlist.append(tempprice.tolist())
                    onehotlistouter.append(tempprice.tolist())
                    onehotlistoutertest.append(tempfood.tolist())
                if (j==3):
                    #onehotlist.append(tempfood.tolist())
                    onehotlistouter.append(tempfood.tolist())
                    onehotlistoutertest.append(tempaddr.tolist())

                #if (j==4)

                # onehotlist.append(tempdate.tolist())
                # onehotlist.append(tempcity.tolist())
                # onehotlist.append(tempprice.tolist())
                # onehotlist.append(tempfood.tolist())
                # onehotlist.append(tempaddr.tolist())
                #
                self.onehotinput.append(onehotlistouter)
                self.onehotoutput.append(onehotlistoutertest)
                # onehotlisttest = list()
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(tempcity.tolist())
                # onehotlisttest.append(tempprice.tolist())
                # onehotlisttest.append(tempfood.tolist())
                # onehotlisttest.append(tempaddr.tolist())
                #
                # self.onehotoutput.append(onehotlisttest)
                #
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(tempprice.tolist())
                # onehotlisttest.append(tempfood.tolist())
                # onehotlisttest.append(tempaddr.tolist())
                #
                # self.onehotoutput.append(onehotlisttest)
                #
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(tempfood.tolist())
                # onehotlisttest.append(tempaddr.tolist())
                #
                # self.onehotoutput.append(onehotlisttest)
                #
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(self.dummylist)
                # onehotlisttest.append(tempaddr.tolist())
                #
                # self.onehotoutput.append(onehotlisttest)
        # print(len(self.onehotinput))
        # print(len(self.onehotoutput)), self.onehotoutput
        return self.onehotinput, self.onehotoutput

    def findLength(self):
        self.count.append(len(self.uniquedate))
        self.count.append(len(self.uniquecity))
        self.count.append(len(self.uniquepricrrange))
        self.count.append(len(self.uniquefood))
        self.count.append(len(self.uniqueaddr))
        return self.count

    # def testtrain(self):
    #
    #     countlist = self.findLength()
    #     for i in range(len(self.onehotinput)):
    #         trainingStartIndex = 0
    #         trainingEndIndex = 0
    #         testStartIndex = 0
    #         testEndIndex = 0
    #
    #         for j in range(5):
    #             trainingEndIndex = trainingEndIndex + countlist[j]
    #             self.traingingdata[(i*5)+j][trainingStartIndex:(trainingEndIndex)] = self.onehotinput[i][trainingStartIndex:(trainingEndIndex)]
    #             self.testingdata[(i*5)+j][trainingEndIndex:50] = self.onehotinput[i][trainingEndIndex:50]

#dataPre = datapreprocessing()
#dataPre.createData()
#dataPre.testtrain()
