rawdata = open('input_test.txt').read().splitlines()
rawdata = open('input.txt').read().splitlines()

data = [[ligne.split('|')[0].strip(), ligne.split('|')[1].strip()] for ligne in rawdata]

nb = len(data)

pattern = []
output = []
for ligne in data:
    pattern.append([set(mot) for mot in ligne[0].split(' ')])
    output.append([set(mot) for mot in ligne[1].split(' ')])


def mot(ens):
    s = ''.join(list(ens))
    return s


def dico(motif):
    d = {}
    r = {}
    for ens in motif:
        if len(ens) == 2:
            d[mot(ens)] = '1'
            r['1'] = ens
        if len(ens) == 3:
            d[mot(ens)] = '7'
            r['7'] = ens
        if len(ens) == 4:
            d[mot(ens)] = '4'
            r['4'] = ens
        if len(ens) == 7:
            d[mot(ens)] = '8'
            r['8'] = ens
            
    for ens in motif:           
        if len(ens) == 6:
            if len(ens.intersection(r['1'])) == 1:
                d[mot(ens)] = '6'
                r['6'] = ens
            elif len(ens.intersection(r['4'])) == 4:
                d[mot(ens)] = '9'
                r['9'] = ens
            else:
                d[mot(ens)] = '0'
                r['0'] = ens                

    for ens in motif:           
        if len(ens) == 5:
            if len(ens.intersection(r['4'])) == 2:
                d[mot(ens)] = '2'
                r['2'] = ens
            elif len(ens.intersection(r['7'])) == 3:
                d[mot(ens)] = '3'
                r['3'] = ens
            else:
                d[mot(ens)] = '5'
                r['5'] = ens     


    return d

def nombre(i):
    d = dico(pattern[i])
    s = ''
    for ens in output[i]:
        for key in d:
            if set(key) == ens:
                s += d[key]
    return int(s)

print(sum([nombre(k) for k in range(nb)]))
        
