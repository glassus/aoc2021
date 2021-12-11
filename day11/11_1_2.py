rawdata = open('input_test2.txt').read().splitlines()
rawdata = open('input.txt').read().splitlines()

import math

n, p = len(rawdata), len(rawdata[0])

M = [[int(nb) for nb in rawdata[i]] for i in range(n)]

compteur_flash = 0

set_coord = set()
for i in range(n):
    for j in range(p):
        set_coord.add((i,j))

def voisins(i, j):
    ens = {(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)}
    ens = ens.intersection(set_coord)
    return ens

def first_step():
    for i in range(n):
        for j in range(p):
            M[i][j] = (M[i][j] + 1) % 10
            
def flash(i, j):
    # -1 : a flashé    0: va flasher
    M[i][j] = -1
    for k, l in voisins(i, j):
        if M[k][l] not in (-1, 0):
            M[k][l] = (M[k][l] + 1) % 10


def produit():
    prod = 1
    for i in range(n):
        for j in range(p):
            prod *= M[i][j]
    return prod

def somme():
    s = 0
    for i in range(n):
        for j in range(p):
            s += M[i][j]
    return s


def total_flash():
    global compteur_flash
    while produit() == 0:
        for i in range(n):
            for j in range(p):
                if M[i][j] == 0:
                    compteur_flash += 1
                    flash(i, j)
    # remise des - 1 à 0
    for i in range(n):
        for j in range(p):
            if M[i][j] == -1:
                M[i][j] = 0    

def step():
    first_step()
    total_flash()

# part 1
# for _ in range(100):
#     step()
#     
# print(compteur_flash)



# part 2
k = 0
while somme() != 0:
    step()
    k += 1
print(k)
