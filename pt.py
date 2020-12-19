t = int(input())
s, n = (int(x) for x in input().split())

pr =  [[0]*n for i in range(n+1)]
res = [[0]*n for i in range(n+1)]
M = []

for i in range(n):
    M.append([int(x) for x in input().split()])

for i in range(1, n+1):
    for k in range(n):
        res[i][k] = res[i-1][k]
        pr[i][k] = k
    for j in range(n):
        for k in range(n):
            if M[j][k] > 0 and res[i-1][j] + M[j][k] > res[i][k]:
                res[i][k] = max(res[i][k], res[i-1][j] + M[j][k])
                pr[i][k] = j

idx = 0
for i in range(0, n):
    idxt = i
    if res[n][idxt] > res[n][idx]:
        for j in range(n, 0, -1): idxt = pr[j][idxt]
        if idxt == s - 1: idx = i

ans = []
for i in range(n, 0, -1):
    if pr[i][idx] != idx:
        ans.append(M[pr[i][idx]][idx])
    idx = pr[i][idx]

for el in reversed(ans):
    print(el, end = ' ')
print()
