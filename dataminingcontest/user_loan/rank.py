import pandas as pd

browse_mean = "E:/data/browse_mean.csv"
bill_mean = "E:/data/bill_mean.csv"
bank_mean = "E:/data/bank_mean.csv"

browse = pd.read_csv(browse_mean)
bill = pd.read_csv(bill_mean)
browse_features = browse.drop(["uid"], axis=1).columns
bill_features = bill.drop(["uid"], axis=1).columns
bank_features = bank_mean.drop(["uid"], axis=1).columns


browse_rank = pd.DataFrame(data=browse.uid, columns=["uid"])
for feature in browse_features:
    browse_rank["r"+feature] = browse[feature].rank(method='max')
browse_rank.to_csv("E:/data/browse_rank.csv")



bill_rank = pd.DataFrame(data=bill.uid, columns=["uid"])
for feature in bill_features:
    bill_rank["r"+feature] = bill_rank[feature].rank(method='max')
bill_rank.to_csv("E:/data/bill_rank.csv")


bank_rank = pd.DataFrame(data=bank_mean.uid,columns=["uid"])
for feature in bank_features:
    bank_rank["r"+feature] = bank_rank[feature].rank(method='max')
bank_rank.to_csv("E:/data/bill_rank.csv")