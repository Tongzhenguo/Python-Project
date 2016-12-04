import os

import pandas as pd

files = os.listdir('featurescore_discret')
fs = {}
for f in files:
    t = pd.read_csv('featurescore_discret/'+f)
    t.index = t.feature
    t = t.drop(['feature'],axis=1)
    d = t.to_dict()['score']
    for key in d:
	if key in ['n1','n2','n3','n4','n5','n6','n7','n8','n9','n10']:
	    continue
        if fs.has_key(key):
            fs[key] += d[key]
        else:
            fs[key] = d[key] 
            
fs = sorted(fs.items(), key=lambda x:x[1],reverse=True)

t = []
for (key,value) in fs:
    t.append("{0},{1}\n".format(key,value))

with open('dataminingcontest/feature_select/discret_feature/discret_feature_score.csv','w') as f:
    f.writelines("feature,score\n")
    f.writelines(t)




