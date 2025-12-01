N, M = map(int, input().split())
birds = {}
for i in range(N):
    A, B = map(int, input().split())
    if A not in birds:
        birds[A] = [B]
    else:
        birds[A].append(B)

for key in sorted(birds.keys()):
    print(sum(birds[key]) / len(birds[key]))
