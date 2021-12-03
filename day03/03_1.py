data = open('input_test.txt').read().splitlines()
data = open('input1.txt').read().splitlines()

nbl = len(data)
lg_mot = len(data[0])

d = [0] * lg_mot

for mot in data:
    for i in range(lg_mot):
        if mot[i] == '1':
            d[i] += 1

gamma = [0] * lg_mot
epsilon = [1] * lg_mot
for i in range(lg_mot):
    if d[i] > nbl // 2:
        gamma[i] = 1
        epsilon[i] = 0

gamma = "".join(str(k) for k in gamma)
epsilon = "".join(str(k) for k in epsilon)

power = int(gamma, 2) * int(epsilon, 2)
print(power)