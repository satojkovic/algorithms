T = int(input())
vowels = set(['a', 'e', 'i', 'o', 'u'])
for t in range(1, T + 1):
    kingdom = input().rstrip()
    last_char = kingdom[-1].lower()
    if last_char in vowels:
        ruler = 'Alice'
    elif last_char == 'y':
        ruler = 'nobody'
    else:
        ruler = 'Bob'
    print('Case #{}: {} is ruled by {}.'.format(t, kingdom, ruler))
