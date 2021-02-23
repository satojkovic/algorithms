def is_alien_char_sorted(words, order):
    def compare(s, t, order_index):
        for s_ch, t_ch in zip(s, t):
            if order_index[s_ch] > order_index[t_ch]:
                return False
            elif order_index[s_ch] < order_index[t_ch]:
                return True
        return len(s) <= len(t)
    order_index = {c:i for i, c in enumerate(order)}
    N = len(words)
    return all(compare(words[i], words[i+1], order_index) for i in range(N - 1))
