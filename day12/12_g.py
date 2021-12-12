# code ignoble, à ne surtout pas lire

rawdata = open('input_test.txt').read().splitlines()
#rawdata = open('input_test2.txt').read().splitlines()
#rawdata = open('input.txt').read().splitlines()

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



count_visit = {}
for node in nodes:
    count_visit[node] = 0


def ok_to_visit(node):
    if is_big(node):
        return True
    if count_visit[node] == 0:
        return True
    if count_visit[node] == 1:
        if node in ('start', 'end'):
            return False
        else:
            return True
    return False






stock_set = set()
stock_lst = []
sol = []
def expand_lst(lst = ['start']):
    dernier = lst[-1]
    if 'end' in voisins[dernier]:
        new_lst = lst.copy()
        new_lst.append('end')
        stock_lst.append(new_lst)
        
    
    else:
        for node in voisins[dernier]:
            if lst.count(node) != 2:
                if node != 'start':
                    if lst.count(node) <= 2 or is_big(node):
                        new_lst = lst.copy()
                        new_lst.append(node)
                        stock_lst.append(new_lst)
                    #mot = "".join(node for node in new_lst)
#                     if mot not in stock_set:
#                         stock_lst.append(new_lst)
#                         stock_set.add(mot)

expand_lst()
#print(stock_lst)
for parcours in stock_lst:
    expand_lst(parcours)
    if parcours[-1] == 'end':
        sol.append(parcours)
        
print(len(sol))
sol2 = []
for prop in sol:
    i_end = prop.index('end')
    tent = prop[:i_end+1]
    if tent not in sol2:
        sol2.append(tent)
        

print(len(sol2))
sol3 = []
for prop in sol2:
    tab = []
    for node in nodes:
        if not is_big(node):
            tab.append(prop.count(node))
    if tab.count(2) <= 1:
        sol3.append(prop)

print(len(sol3))
            
# for k in sol:
#     if k not in sol3:
#         print(k)
