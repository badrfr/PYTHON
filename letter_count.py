mot = input("Entrez un mot : ")
l = input("Quelle est la lettre recherchée : ")

c = mot.count(l)
# prendre en compte l en majuscule
c += mot.count(l.upper())


print('La lettre', l, 'a été utilisée', c, 'fois')
