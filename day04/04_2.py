data = open('input_test.txt').read().splitlines()
data = open('input.txt').read().splitlines()



class Carte:
    def __init__(self):
        self.numeros = []
        self.rang_victoire = 0
        self.val_victoire = 0
        
        
    def marque_num(self, num):
        for i in range(5):
            for j in range(5):
                if self.numeros[i][j] ==  num:
                    self.numeros[i][j] = 0
                    
    def est_gagnante(self):
        for row in self.numeros:
            if sum(row) == 0:
                return True
        for j in range(5):
            if sum([self.numeros[i][j] for i in range(5)]) == 0:
                return True
        return False
    
    def somme_totale(self):
        return sum([sum(row) for row in self.numeros])

tirage = [int(k) for k in data[0].split(',')]

cartes = []
data = [ligne.replace('  ',' ').strip() for ligne in data]

for k in range(2, len(data), 6):
    carte = Carte()
    carte.numeros = [[int(n) for n in data[l].split(' ')] for l in range(k, k + 5)]
    cartes.append(carte)

def jeu():
    rang = 1
    for nb in tirage:
        for carte in cartes:
            if not carte.est_gagnante():
                carte.marque_num(nb)
                if carte.est_gagnante():
                    carte.rang = rang
                    rang += 1
                    carte.val_victoire = nb * carte.somme_totale()

jeu()
ans = sorted(cartes, key = lambda c : c.rang)[-1].val_victoire
print(ans)
