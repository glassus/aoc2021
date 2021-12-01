data_str = open('input1.txt').read().splitlines()

data = [int(chaine) for chaine in data_str]

mesures3 = [data[i] + data[i+1] + data[i+2] for i in range(len(data)-2)]

sol = sum([1 for i in range(1, len(mesures3)) if mesures3[i] > mesures3[i-1]])

print(sol)