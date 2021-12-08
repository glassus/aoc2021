from statistics import median, mean

data = open('input_test.txt').read().splitlines()
data = open('input.txt').read().splitlines()

data = [int(k) for k in data[0].split(',')]

data = [16,1,2,0,4,2,7,1,2,140,150,160,170,180]

def cout(n) : #part 1
    s = 0
    for k in data:
        s += abs(k - n)
    return s

def cout(n): # part2
    s = 0
    for k in data:
        v = abs(k - n)
        s += (v*(v+1))//2
    return s


import matplotlib.pyplot as plt

xpoints = range(min(data), max(data) + 1)
ypoints = [cout(k) for k in xpoints]


plt.plot(xpoints, ypoints, '+')
plt.show()

# 
minimum = False
pos = (min(data) + max(data))//2

while not minimum:
    if cout(pos - 1) < cout(pos) < cout(pos + 1):
        pos -= 1
    elif cout(pos - 1) > cout(pos) > cout(pos + 1):
        pos += 1
    else :
        minimum = True

print(pos, cout(pos))
print(mean(data))