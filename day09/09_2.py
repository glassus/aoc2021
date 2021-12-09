rawdata = open('input_test.txt').read().splitlines()
rawdata = open('input.txt').read().splitlines()

n, p = len(rawdata), len(rawdata[0])

M = [[int(nb) for nb in rawdata[i]] for i in range(n)]

N = [[1 if M[i][j] != 9 else 9 for j in range(p)] for i in range(n)] 

def voisins(i, j):
    if (i, j) == (0, 0):
        return [(i, j+1), (i+1, j)]
    if (i, j) == (n-1, 0):
        return [(i-1, j), (i, j+1)]
    if (i, j) == (n-1, p-1):
        return [(i-1, j), (i, j-1)]
    if (i, j) == (0, p-1):
        return [(i, j-1), (i+1, j)]
    
    if i == 0:
        return [(i, j-1), (i, j+1), (i+1, j)]
    if i == n - 1:
        return [(i, j-1), (i, j+1), (i-1, j)]
    
    if j == 0:
        return [(i-1, j), (i+1, j), (i, j+1)]
    if j == p - 1:
        return [(i-1, j), (i+1, j), (i, j-1)]
    
    return [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]


def parcours(i, j):
    global s
    if N[i][j] == 9:
        return None
    if N[i][j] == 0:
        return None
    if N[i][j] == 1:
        s += 1
        N[i][j] = 0
        for v in voisins(i, j):
            parcours(v[0], v[1])
    
basin =  []
for i in range(n):
    for j in range(p):
        if N[i][j] == 1:
            s = 0
            parcours(i, j)
            if s != 0:
                basin.append(s)
            
basin.sort()
print(basin[-1]*basin[-2]*basin[-3])
    
