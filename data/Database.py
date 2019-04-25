import pandas as pd


class CreateDatabase(object):
    def __init__(self):
        self.cols = ["gender", "state", "zip", "organ", "height", "weight", "autoimmune_disease", "hiv", "malignancies", "other_problem", "on_insulin", "no_insulin", "time_insulin", "storke", "pacemaker", "on_dialysis", "serum_creatinine", "life_support", "hepatitis", "fatty_liver", "smoker", "ventilation", "pneumonia", "asthamatic", "address", "waiting"]
        self.dict = {}
        self.dictList = list()
    def createDataBase(self):
        data = pd.read_csv("data.csv", header=None, skiprows=1)
        data = data.values.tolist()
        f = open('dictData.txt', 'w')
        #print(data[1][0])
        for i in range(len(data)):
            for j in range(len(data[i])):
                self.dict[self.cols[j]] = data[i][j]
            f.write(str(self.dict))
            f.write("\n")
            print(self.dict)

    def org_dict(self):
        data = pd.read_csv("data.csv", header=None, skiprows=1)
        data = data.values.tolist()
        f = open('dictOrg.txt', 'w')
        for i in range(len(self.cols)):
            f.write(str(self.cols[i]))
            f.write(':[')
            for j in range(len(data)):
                f.write(str(data[j][i]))
                if(j < len(data)-1):
                    f.write(',')
            f.write(']')
            f.write('\n')

    def organ_patient_goals(self):
        dictrs = {}
        dictis = {}
        dict = {}
        data = pd.read_csv("data.csv", header=None, skiprows=1)
        data = data.values.tolist()
        print(len(data[0]))
        f = open('organ_patient_goals.txt', 'w')


        for i in range(len(data)):
            dictrs[self.cols[len(self.cols) - 1]] = data[i][len(self.cols) - 1]
            dictrs[self.cols[len(self.cols) - 2]] = data[i][len(self.cols) - 2]
            for j in range(len(data[i])-2):
                dictis[self.cols[j]] = data[i][j]

            dict['request_slots'] =  dictrs
            dict['inform_slots'] = dictis
            print(dict)

            f.write(str(dict))
            f.write("\n")
            dict.clear()
        f.close()







database = CreateDatabase()
#database.createDataBase()
#database.org_dict()
database.organ_patient_goals()