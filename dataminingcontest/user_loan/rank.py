import pandas as pd

browse_mean = "E:/data/browse_mean.csv"
bill_mean = "E:/data/bill_mean.csv"
bank_mean = "E:/data/bank_mean.csv"
browse_rank_path = "E:/data/browse_rank.csv"
bill_rank_path = "E:/data/bill_rank.csv"
bank_rank_path = "E:/data/bank_rank.csv"

browse = pd.read_csv(browse_mean)
bill = pd.read_csv(bill_mean)
bank = pd.read_csv(bank_mean)
browse_features = browse.drop(["uid"], axis=1).columns
bill_features = bill.drop(["uid","bill_time","status"], axis=1).columns
bank_features = bank.drop(["uid"], axis=1).columns


browse_rank = pd.DataFrame(browse.uid,columns=["uid"])
for feature in browse_features:
    browse_rank["r"+feature] = browse[feature].rank(method='max')
browse_rank.to_csv(browse_rank_path,index=None)



bill_rank = pd.DataFrame(data=bill.uid, columns=["uid"])
for feature in bill_features:
    bill_rank["r"+feature] = bill[feature].rank(method='max')
bill_rank.to_csv(bill_rank_path,index=None)


bank_rank = pd.DataFrame(data=bank.uid,columns=["uid"])
for feature in bank_features:
    bank_rank["r"+feature] = bank[feature].rank(method='max')
bank_rank.to_csv(bank_rank_path,index=None)