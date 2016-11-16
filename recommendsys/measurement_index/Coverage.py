def GiniIndex(p):
    """
    :param p:the dict of item popularity
    :return:gini index
    """
    j = 1
    n = len(p)
    G = 0
    for item, weight in sorted(p.items(), key=lambda p: p[1]):
        G += (2 * j - n - 1) * weight
        j += 1
    return G / float(n - 1)
