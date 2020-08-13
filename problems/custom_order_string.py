from collections import Counter
def custom_order_string(S, T):
    t_dic = Counter(T)
    res = []
    for s in S:
        if s in t_dic:
            res.append(s * t_dic[s])
            del t_dic[s]
    if len(t_dic) != 0:
        res.extend([t * t_dic[t] for t in t_dic.keys()])
    return ''.join(res)

if __name__ == "__main__":
    print(custom_order_string('zap', 'badczap'))
    print(custom_order_string('abcde', 'qrs'))