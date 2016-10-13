from math import log
class InfoGain:
    def __init__(self,path):
        self.data = []
        self.count = 0
        self.labelColIDX = 0
        f = open(path)
        lines = f.readlines()
        f.close()
        ##read file format
        for i in range(len(lines)):
            lines[i] = lines[i].strip("\n")
            if (i == 0):
                 #print("file format:" + lines[i])
                 format = lines[i].split("\t")
                 for j in range(len(format)):
                    #print(format[j])
                    if(format[j] == 'label'):
                        self.labelColIDX = j
            else:
                vector = []
                field = lines[i].split("\t")
                for j in range(len(field)):
                    if self.labelColIDX == j:
                        label = field[j]
                        #print label
                    else:
                        vector.append(field[j])
                self.data.append((label,vector))
                self.count = self.count + 1
                #print("data:" + lines[i])
    def getEntropy(self,simples,vector):
        result = 0
        for k in vector:
            p = (k * 1.0 / simples)
            result -= p * log(p,2)
        return result
    def getConditionalEntropy(self,simples,col):
        result = 0
        feature = {}
        for t2 in self.data:
                v1 = int(t2[1][col])
                vector = [0,0,0]
                label = int(t2[0])
                if(v1 not in feature):
                    if(label not in vector):
                        vector[label]=1#dict
                    else:
                        vector[label] = vector[label] + 1
                    feature[v1] = vector
                else:
                    feature[v1][label] = feature[v1][label] + 1
        for v in feature:
            count = 0
            for l in feature[v]:
                count +=l
            p = count*1.0 / simples
            result += (p * self.getEntropy(count,feature[v]))
        return result
gain = InfoGain("D:\Python-Project\dataset\loan.csv")
#print gain.getEntropy(15,[9,6])
print gain.getConditionalEntropy(15,0)
# print gain.getEntropy(5,4)