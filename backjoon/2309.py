dwarfs = sorted([int(input()) for _ in range(9)])

for i in range(9):
    for j in range(i+1, 9):
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            for k in range(9):
                if i != k and j != k:
                    print(dwarfs[k])
            exit()