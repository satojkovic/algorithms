def gen_next_move(currentState):
    res = []
    for i in range(1, len(currentState)):
        if currentState[i-1:i+1] == '++':
            s = currentState[:i-1] + '--' + currentState[i+1:]
            res.append(s)
    return res

if __name__ == '__main__':
    print(gen_next_move('++++'))
