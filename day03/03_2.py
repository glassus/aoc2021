data = open('input_test.txt').read().splitlines()
data = open('input1.txt').read().splitlines()

nbl = len(data)
lg_mot = len(data[0])


def filtre_maj(data, i):
    c = 0
    for mot in data:
        if mot[i] == '1':
            c += 1  
    if c >= len(data) - c:
        val_maj = "1"
    else:
        val_maj = "0"
    new_data = [mot for mot in data if mot[i] == val_maj]
    return new_data

data_max = list(data)
i = 0
while len(data_max ) != 1:
    data_max  = filtre_maj(data_max , i)
    i += 1


oxygen = int(data_max [0],2)


def filtre_min(data, i):
    c = 0

    for mot in data:
        if mot[i] == '1':
            c += 1
    if c >= len(data) - c:
        val_min = "0"
    else:
        val_min = "1"
    new_data = [mot for mot in data if mot[i] == val_min]
    return new_data




data_min = list(data)
i = 0
while len(data_min) != 1:
    data_min = filtre_min(data_min, i)
    i += 1


CO2 = int(data_min[0],2)


print(CO2*oxygen)

