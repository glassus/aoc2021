rawdata = open('input_test.txt').read().splitlines()
rawdata = open('input.txt').read().splitlines()

n, p = len(rawdata), len(rawdata[0])

M = [[int(nb) for nb in rawdata[i]] for i in range(n)]

def is_val_min(i, j):
    val = M[i][j]
    
    if (i, j) == (0, 0):
        return val < M[i][j+1] and val < M[i+1][j]
    if (i, j) == (n-1, 0):
        return val < M[i-1][j] and val < M[i][j+1]
    if (i, j) == (n-1, p-1):
        return val < M[i-1][j] and val < M[i][j-1]
    if (i, j) == (0, p-1):
        return val < M[i][j-1] and val < M[i+1][j]
    
    if i == 0:
        return val < min(M[i][j-1], M[i][j+1], M[i+1][j])
    if i == n - 1:
        return val < min(M[i][j-1], M[i][j+1], M[i-1][j])
    
    if j == 0:
        return val < min(M[i-1][j], M[i+1][j], M[i][j+1])
    if j == p - 1:
        return val < min(M[i-1][j], M[i+1][j], M[i][j-1])
    
    return val < min(M[i-1][j], M[i+1][j], M[i][j-1], M[i][j+1])

risk = 0
for i in range(n):
    for j in range(p):
        risk += (1 + M[i][j]) * int(is_val_min(i, j)) 

print(risk)