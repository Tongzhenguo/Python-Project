import math


# def UserSimilarity(train):
#     """consine similarity
#     :param train:
#     :return:
#     """
#     W = dict()
#     for u in train.keys():
#         for v in train.keys():
#             if( u == v ):
#                 continue
#         W[u][v] = len(train[u] & train[v] ) ###the intersection of set
#         W[u][v] /= math.sqrt( len(train[u]) * len(train[v]) * 1.0 )
#     return W

def UserSimilarity(train):
    """bulid inverse table for item_users
    :param train:
    :return:
    """
    item_users = dict()
    for (u, items) in train.items():
        for i in items.keys():
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)
    # calculate co-reted items between users
    C = dict()
    N = dict()
    for (i, users) in item_users.items():
        for u in users:  # for each user
            if (not N.has_key(u)):
                N.setdefault(u, 0)
            if (not C.has_key(u)):
                C.setdefault(u, {})
            N[u] += 1
            for v in users:
                if (u == v):
                    continue
                if (not C[u].has_key(v)):
                    C[u].setdefault(v, 0)
                C[u][v] += 1
    # calculate final similarity matrix W
    W = dict()
    for (u, related_users) in C.items():
        if (not W.has_key(u)):
            W.setdefault(u, {})
        for (v, cuv) in related_users.items():
            if (not W[u].has_key(v)):
                W[u].setdefault(v, 0.0)
            W[u][v] = cuv / math.sqrt(N[u] * N[v])
    return W


train = {
    "A": {"a": None, "b": None, "d": None},
    "B": {"a": None, "c": None},
    "C": {"b": None, "e": None},
    "D": {"c": None, "d": None, "e": None}
}
print(UserSimilarity(train))
