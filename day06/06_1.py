data = open('input_test.txt').read().splitlines()
data = open('input.txt').read().splitlines()

data = [int(k) for k in data[0].split(',')]

def cycle(lst):
    cp_lst = lst.copy()
    for i in range(len(lst)):
        cp_lst[i] -= 1
        if cp_lst[i] == -1:
            cp_lst[i] = 6
            cp_lst.append(8)
    return cp_lst

for _ in range(80):
    data = cycle(data)
print(len(data))