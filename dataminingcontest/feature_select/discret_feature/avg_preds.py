import os

import pandas as pd

files = os.listdir('./preds_discret')
print len(files)
pred = pd.read_csv('./preds_discret/'+files[0])
uid = pred.uid
score = pred.score
for f in files[1:]:
    pred = pd.read_csv('./preds_discret/'+f)
    score += pred.score

score /= len(files)

pred = pd.DataFrame(uid,columns=['uid'])
pred['score'] = score
pred.to_csv('dataminingcontest/feature_select/discret_feature/avg_preds_discret.csv',index=None,encoding='utf-8')
