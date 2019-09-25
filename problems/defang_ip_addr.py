def defang_ip_addr1(address):
    defanged = []
    for ch in address:
        if ch == '.':
            defanged.append('[.]')
        else:
            defanged.append(ch)
    return ''.join(defanged)