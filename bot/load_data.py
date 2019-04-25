import  pandas as pd


def load_dict():
   # dict = {}
    dictAll = {}
    data_path = 'data.csv'
    data = pd.read_csv(data_path, header=None, skiprows=1)
    cols = ["gender", "state", "zip", "organ", "height", "weight", "autoimmune_disease", "hiv", "malignancies", "other_problem", "on_insulin", "no_insulin", "time_insulin", "storke", "pacemaker", "on_dialysis", "serum_creatinine", "life_support", "hepatitis", "fatty_liver", "smoker", "ventilation", "pneumonia", "asthamatic", "address", "waiting"]

    data = pd.read_csv("data.csv", header=None, skiprows=1)
    data = data.values.tolist()
    f = open('dictData.txt', 'w')
    # print(data[1][0])
    for i in range(len(data)):
        dict = {}
        for j in range(len(data[i])):
            dict[cols[j]] = data[i][j]
        #f.write(str(dict))
        #f.write("\n")
        #print(self.dict)
        dictAll[i] = dict
        #dict.clear()
    #print(dictAll)
    return dictAll

def load_orgdict():
    cols = ["gender", "state", "zip", "organ", "height", "weight", "autoimmune_disease", "hiv", "malignancies",
            "other_problem", "on_insulin", "no_insulin", "time_insulin", "storke", "pacemaker", "on_dialysis",
            "serum_creatinine", "life_support", "hepatitis", "fatty_liver", "smoker", "ventilation", "pneumonia",
            "asthamatic", "address", "waiting"]
    dict = {}
    data = pd.read_csv("data.csv", header=None, skiprows=1)
    data = data.values.tolist()
    for i in range(len(cols)):
        valueList = []
        for j in range(len(data)):
            valueList.append(data[j][i])
        dict[str(cols[i])] = valueList

    return  dict


def load_goals():
    dictrs = {}
    dictis = {}
    dict = {}
    dataList = []
    data = pd.read_csv("data.csv", header=None, skiprows=1)
    data = data.values.tolist()
    cols = ["gender", "state", "zip", "organ", "height", "weight", "autoimmune_disease", "hiv", "malignancies",
            "other_problem", "on_insulin", "no_insulin", "time_insulin", "storke", "pacemaker", "on_dialysis",
            "serum_creatinine", "life_support", "hepatitis", "fatty_liver", "smoker", "ventilation", "pneumonia",
            "asthamatic", "address", "waiting"]
    #print(len(data[0]))
    f = open('organ_patient_goals.txt', 'w')

    for i in range(len(data)):
        dictrs[cols[len(cols) - 1]] = data[i][len(cols) - 1]
        dictrs[cols[len(cols) - 2]] = data[i][len(cols) - 2]
        for j in range(len(data[i]) - 2):
            dictis[cols[j]] = data[i][j]

        dict['request_slots'] = dictrs
        dict['inform_slots'] = dictis

        dataList.append(dict)

    return  dataList


#load_orgdict()
load_goals()