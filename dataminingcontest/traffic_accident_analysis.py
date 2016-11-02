# coding=utf-8
tianqiFile = open("F:\code\Python-Project\dataset\wf1.csv")
readlines = tianqiFile.readlines()
wfxwcount = {}
for line in readlines:
    if (not line.__contains__("wfxw")):
        ss = line.strip().replace("\t", ",").split(",")
        if (wfxwcount.has_key(ss[3])):
            wfxwcount[ss[3]] = wfxwcount[ss[3]] + 1
        else:
            wfxwcount[ss[3]] = 1
sorted1 = sorted(wfxwcount.iteritems(), key=lambda p: p[1], reverse=True)
for item in sorted1:
    print item
print len(wfxwcount)
#
# tianqiFile = open("F:\code\Python-Project\dataset\\accid1.csv")
# readlines = tianqiFile.readlines()
# wfxwcount = {}
# for line in readlines:
#     if (not line.__contains__("wfxw")):
#         ss = line.strip().replace("\t", ",").split(",")
#         colIDX = 1
#         for colitem in ss:
#             if(wfxwcount.has_key(ss[3])):
#                 wfxwcount[ss[3]] = wfxwcount[ss[3]] +1
#         else:
#             wfxwcount[ss[3]] = 1
# for item in wfxwcount.items():
#     print item
# print len(wfxwcount)
