rawdata = open('input_test.txt').read().splitlines()
rawdata = open('input_test2.txt').read().splitlines()
rawdata = open('input.txt').read().splitlines()

nodes_vrac = [[n for n in couples.split('-')] for couples in rawdata] 
nodes = set()
for lst in nodes_vrac:
    for sommet in lst:
        nodes.add(sommet)
voisins = {}
for node in nodes:
    voisins[node] = set()
    for couple in nodes_vrac:
        if node in couple:
            if couple[0] != node:
                voisins[node].add(couple[0])
            if couple[1] != node:
                voisins[node].add(couple[1])            

def is_big(node):
    return ord(node[0]) < 90

stock_set = set()
stock_lst = []
sol = []
def expand_lst(lst = ['start']):
    dernier = lst[-1]
    for node in voisins[dernier]:
        if node not in lst or is_big(node):
            new_lst = lst.copy()
            new_lst.append(node)
            mot = "".join(node for node in new_lst)
            if mot not in stock_set:
                stock_lst.append(new_lst)
                stock_set.add(mot)

expand_lst()

for parcours in stock_lst:
    expand_lst(parcours)
    if parcours[-1] == 'end':
        sol.append(parcours)
        
print(len(sol))
