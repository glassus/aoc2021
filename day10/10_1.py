rawdata = open('input_test.txt').read().splitlines()
rawdata = open('input.txt').read().splitlines()

def cherche_erreur(ligne):
    pile = []
    for car in ligne:
        if car in {'(', '{', '[', '<'}:
            pile.append(car)
        else:
            ouvrant = pile.pop()
            if ouvrant + car not in {'()', '{}', '[]', '<>'}:
                return car
    return None

def points_ligne(ligne):
    code_erreur = cherche_erreur(ligne)
    if code_erreur is None:
        return 0
    elif code_erreur == ')':
        return 3
    elif code_erreur == ']':
        return 57
    elif code_erreur == '}':
        return 1197
    elif code_erreur == '>':
        return 25137
    

ans = sum([points_ligne(ligne) for ligne in rawdata])
print(ans)
    