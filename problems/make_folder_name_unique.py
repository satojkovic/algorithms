def make_folder_name_unique(names):
    def assign_name(name, k):
        return ''.join([name, '(', str(k), ')'])

    assigned = {}
    res = []
    for name in names:
        if not name in assigned:
            res.append(name)
            assigned[name] = 1
        else:
            k = assigned[name]
            while assign_name(name, k) in assigned:
                k += 1
            assigned[name] = k
            assigned[assign_name(name, k)] = 1
            res.append(assign_name(name, k))
    return res