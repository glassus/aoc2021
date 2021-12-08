rawdata = open('input_test.txt').read().splitlines()
rawdata = open('input.txt').read().splitlines()

data = [[ligne.split('|')[0].strip(), ligne.split('|')[1].strip()] for ligne in rawdata]

nb = len(data)

pattern = []
output = []
for ligne in data:
    pattern.append([set(mot) for mot in ligne[0].split(' ')])
    output.append([set(mot) for mot in ligne[1].split(' ')])

s = 0
for val in output:
    for ens in val:
        if len(ens) in (2, 3, 4, 7):
            s += 1
print(s)