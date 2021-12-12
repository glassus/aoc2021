rawdata = open('input_test.txt').read().splitlines()
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

def Parcours(node, visited = None):
    if visited is None:
        visited = []
        
    if node not in visited:
        visited.append(node)
    
    unvisited = [n for n in voisins[node] if n not in visited]
    
    for node in unvisited:
        parcours(node, visited)
    
    return visited



# def cherche_parcours(node, parcours = None):
#     global stock_sol
#     if parcours is None:
#         parcours = []
#         
#     if node not in parcours:
#         parcours.append(node)
#         if node == 'end':
#             stock_sol.append(parcours)
#             print('trouvé')
#             return None
#     
#     to_visit = [n for n in voisins[node] if n not in parcours]
#     
#     for n in to_visit:
#         cherche_parcours(n, parcours)

# cherche_parcours('start')
# print(stock_sol)          

# stock = [['start']]
# sol = []
# 
# while len(stock) < 8:
#     for parcours in stock:
#         stock_temp = []
#         last_node = parcours[-1]
#         for node in voisins[last_node]:
#             if node not in parcours or is_big(node):
#                 new_parcours = list(parcours)
#                 new_parcours.append(node)
#                 if node == 'end':
#                     sol.append(new_parcours)
#                 stock_temp.append(new_parcours)
#         #stock.remove(parcours)
#     stock += stock_temp
# print(len(stock))
# print(sol)

























frontier = []
frontier.append('start')
came_from = dict()
came_from['start'] = None

while not frontier == []:
    current = frontier.pop(0)
    print(voisins[current])
    for suivant in voisins[current]:
        if is_big(suivant) or suivant not in came_from:
            frontier.append(suivant)
            came_from[suivant] = current            

            
current = 'end'
path = []
while current != 'start':
    path.append(current)
    current = came_from[current]
path.append('start')
path.reverse()
print(path) 