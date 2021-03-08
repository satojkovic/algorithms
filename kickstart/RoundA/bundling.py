def gen_groups(words, i):
    if i == len(words) - 1:
        return [[[words[i]]]]

    res = []
    groups = gen_groups(words, i + 1)    
    for group in groups:
        for k, elem in enumerate(group):
            new_elem = elem + [words[i]]
            new_group = [new_elem]
            if k != 0:
                new_group.extend(group[:k])
            if k < len(group) - 1:
                new_group.extend(group[k+1:])
            res.append(new_group)
        group.append([words[i]])
        res.append(group)
    return res

if __name__ == '__main__':
    words = ['s4', 's3', 's2', 's1']
    print(gen_groups(words, 0))
