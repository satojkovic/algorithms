def is_alien_char_sorted(words, order):
    order_index = {c:i for i, c in enumerate(order)}
    N = len(words)
    for i in range(N - 1):
        prev_word = words[i] if len(words[i]) <= len(words[i+1]) else words[i+1]
        next_word = words[i+1] if len(words[i]) <= len(words[i+1]) else words[i]
        toggle = False if len(words[i]) <= len(words[i+1]) else True
        is_order = True
        for j in range(len(prev_word)):
            if order_index[prev_word[j]] == order_index[next_word[j]]:
                continue
            elif order_index[prev_word[j]] < order_index[next_word[j]]:
                break
            else:
                is_order = False
                break                
        if (toggle and is_order) or (not toggle and not is_order):
            return False
    return True
