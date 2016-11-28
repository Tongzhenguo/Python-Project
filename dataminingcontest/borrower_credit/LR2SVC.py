import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


#load data
train_x_csv = pd.read_csv("F:\code\Python-Project\dataset\\borrower_credit\select_feature_train_x.csv")
train_y_csv = pd.read_csv("F:\code\Python-Project\dataset\\borrower_credit\\train_y.csv")
test_csv = pd.read_csv("F:\code\Python-Project_\dataset\\borrower_credit\select_feature_test_x.csv")
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

plt.figure(figsize=(3 * 2, n_classifiers * 2))
plt.subplots_adjust(bottom=.2, top=.95)

for index, (name, classifier) in enumerate(classifiers.items()):
    classifier.fit(X, y)
    y_pred = classifier.predict(X)
    classif_rate = np.mean(y_pred.ravel() == y.ravel()) * 100
    print("classif_rate for %s : %f " % (name, classif_rate))
    # View probabilities=
    probas = classifier.predict_proba(test_x)
    print probas
    n_classes = np.unique(y_pred).size
    for k in range(n_classes):
        plt.subplot(n_classifiers, n_classes, index * n_classes + k + 1)
        plt.title("Class %d" % k)
        if k == 0:
            plt.ylabel(name)
        imshow_handle = plt.imshow(probas[:, k].reshape((100, 100)),
                                   extent=(3, 9, 1, 5), origin='lower')
        plt.xticks(())
        plt.yticks(())
        idx = (y_pred == k)
        if idx.any():
            plt.scatter(X[idx, 0], X[idx, 1], marker='o', c='k')
# show probability label
ax = plt.axes([0.15, 0.04, 0.7, 0.05])
plt.title("Probability")
plt.colorbar(imshow_handle, cax=ax, orientation='horizontal')
plt.show()