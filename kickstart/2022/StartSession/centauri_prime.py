T = int(input())
vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
for t in range(1, T + 1):
    kingdom = input().rstrip()
    if kingdom[-1] == 'y' or kingdom[-1] == 'Y':
        ruler = 'nobody'
    elif kingdom[-1] in vowels:
        ruler = 'Alice'
    else:
        ruler = 'Bob'
    print('Case #{}: {} is ruled by {}.'.format(t, kingdom, ruler))
