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

def sol_valide(lst):
    #return True
    tab = []
    for node in lst:
        if not is_big(node):
            tab.append(lst.count(node))
    #print(lst)
    #print(tab)
    if tab.count(2) <= 1:
        return True
    return False

def autorise(node, lst):
    tab = []
    for n in lst:
        if not is_big(node):
            tab.append(lst.count(n))
    n2 = tab.count(2)
    if lst.count(node) >= 1 and n2 >= 2:
        return False
    return True


stock_set = set()
stock_lst = []
sol = []
def expand_lst(lst = ['start']):
    dernier = lst[-1]
    for node in voisins[dernier]:
        if node != 'start':
            if True or autorise(node, lst):
                if lst.count(node) <= 2 or is_big(node):
                    new_lst = lst.copy()
                    new_lst.append(node)
                    if sol_valide(new_lst):
                        #mot = "".join(node for node in new_lst)
                        #if mot not in stock_set :
                        stock_lst.append(new_lst)
                         #   stock_set.add(mot)

expand_lst()

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
            

