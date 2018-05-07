#求骰子的可能值和概率
def probablity(n,g):
    if n < 1:
        return []
    data1 = [0] + [1] * g + [0] * g* (n - 1)
    data2 = [0] + [0] * g * n   # 开头多一个0，方便按照习惯从1计数
    flag = 0
    for v in range(2, n+1):  # 控制次数
        if flag:
            for k in range(v, g*v+1):
                data1[k] = sum([data2[k-j] for j in range(1, 7) if k > j])
            flag = 0
        else:
            for k in range(v, g*v+1):
                data2[k] = sum([data1[k-j] for j in range(1, 7) if k > j])
            flag = 1
    ret = []
    total = g ** n
    data = data2[n:] if flag else data1[n:]
    for v in data:
        ret.append(v*1.0/total)
    print data
    return ret