import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


#load data
train_x_csv = pd.read_csv("dataset\\borrower_credit\select_feature_train_x.csv")
train_y_csv = pd.read_csv("dataset\\borrower_credit\\train_y.csv")
test_csv = pd.read_csv("dataset\\borrower_credit\select_feature_test_x.csv")
test_x = test_csv.drop(test_csv.columns[[0]],axis=1).values

y_0 = train_y_csv[train_y_csv.y == 0]
for i in range(13458 / 1542 ):
    train_y_csv = train_y_csv.append(y_0)

X_ = train_x_csv.drop(train_x_csv.columns[[0]],axis=1) #index' axis = 0 and remove "uid" field
X = X_.values
y = train_y_csv["y"].values

n_features = X.shape[1]
C = 1.0

# Create different classifiers. The logistic regression cannot do
# multiclass out of the box.
classifiers = {'L1 logistic': LogisticRegression(C=C, penalty='l1'),
               'L2 logistic (OvR)': LogisticRegression(C=C, penalty='l2'),
               'L2 logistic (Multinomial)': LogisticRegression(
                C=C, solver='lbfgs', multi_class='multinomial')
               }

n_classifiers = len(classifiers)

#model select
for index, (name, classifier) in enumerate(classifiers.items()):
    classifier.fit(X, y)
    y_pred = classifier.predict(X)
    classif_rate = np.mean(y_pred.ravel() == y.ravel()) * 100
    print("classif_rate for %s : %f " % (name, classif_rate))
    # View probabilities=
    probas = classifier.predict_proba(test_x)
    print probas

best_clf = LogisticRegression(C=C, penalty='l2')
classifier.fit(X, y)
probas = classifier.predict_proba(test_x)
