import numpy as np

def replaceCost(s, t, sIndex, tIndex):
    if (s[sIndex] == t[tIndex]): return 0
    else: return 1

def buttom_up_edit_distance(w1, w2):
    if (not w1): return len(w2)
    if (not w2): return len(w1)

    w1Len = len(w1)
    w2Len = len(w2)
    # print(w1Len)
    # print(w2Len)

    minCost = np.zeros(shape=(w1Len, w2Len))
    # print(minCost)
    # print(minCost[4][5])

    minCost[w1Len - 1][w2Len - 1] = replaceCost(w1, w2, w1Len - 1, w2Len - 1)

    for j in reversed(range(0, w2Len - 1)):
        minCost[w1Len - 1][j] = 1 + minCost[w1Len - 1][j + 1]

    for i in reversed(range(0, w1Len - 1)):
        minCost[i][w2Len - 1] = 1 + minCost[i+1][w2Len - 1]
    
    for i in reversed(range(0, w1Len - 1)):
        for j in reversed(range(0, w2Len - 1)):
            replace = replaceCost(w1, w2, i, j) + minCost[i+1][j+1];
            delete = 1 + minCost[i+1][j];
            insert = 1 + minCost[i][j+1];
            minCost[i][j] = min(replace, delete, insert)
    
    return minCost[0][0]