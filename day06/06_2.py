data = open('input_test.txt').read().splitlines()
data = open('input.txt').read().splitlines()

data = [int(k) for k in data[0].split(',')]

d = {}
for k in range(9):
    d[k] = 0

for k in data:
    d[k] += 1

for _ in range(256):
    sauv = d[0]
    for i in range(1,9):
        d[i-1] = d[i]
    d[8] = sauv
    d[6] += sauv
    #print(d)

s = 0
for k in range(9):
    s += d[k]
print(s)