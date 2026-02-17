def f(N):
    for x in range(113, N, 226):
            for i in range(0,13):
                if x + 3**i == N:
                    return i
    return 0

cnt = 0
for N in range(100_000, 1_000_000,2):
        if '0' not in str(N) and (M := f(N)):
            print(N, M)
            cnt += 1
            if cnt == 5:
                break
