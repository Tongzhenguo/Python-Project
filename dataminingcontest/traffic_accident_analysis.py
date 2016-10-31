# coding=utf-8
tianqiFile = open("F:\code\Python-Project\dataset\wf1.csv")
readlines = tianqiFile.readlines()
for line in readlines:
    if (not line.__contains__("天气状况")):
        ss = line.strip().replace("\t", ",").split(",")
        print(ss[0])
