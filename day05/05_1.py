import numpy as np


data = open('input_test.txt').read().splitlines()
data = open('input.txt').read().splitlines()

data = [line.split(' -> ') for line in data]
data = [[[int(k) for k in couple.split(',')] for couple in line] for line in data]

def taille(data):
    tmax = 0
    for couple in data:
        for points in couple :
            for coord in points:
                if coord > tmax :
                    tmax = coord
    return tmax + 1

tmax = taille(data)
m = np.zeros([tmax,tmax], dtype=int)


def est_horizontal(couple):
    return couple[0][1] == couple[1][1]

def est_vertical(couple):
    return couple[0][0] == couple[1][0]

def est_diagonal(couple):
    return (not est_horizontal(couple)) and (not est_vertical(couple))

def remplissage(m):
    for couple in data:
        if est_horizontal(couple):
            maxi = max(couple[0][0], couple[1][0])
            mini = min(couple[0][0], couple[1][0])
            for j in range(mini, maxi + 1):
                m[couple[0][1], j] += 1

        if est_vertical(couple):
            maxi = max(couple[0][1], couple[1][1])
            mini = min(couple[0][1], couple[1][1])
            for i in range(mini, maxi + 1):
                m[i, couple[0][0]] += 1
 
 
 
remplissage(m)
print(np.count_nonzero(m > 1))