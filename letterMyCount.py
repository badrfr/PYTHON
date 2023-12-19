mot = input("Entrez un mot : ")
l = input("Quelle est la lettre recherchée : ")
def myCount(mot, lettre):
    c = 0  # Initialisation du compteur à 0
    for char in mot:  # Parcours de chaque caractère dans le mot
        if char == lettre or char == lettre.upper():  # Si le caractère correspond à la lettre recherchée
            c += 1  # Incrémenter le compteur
    return c  # Retourner le compteur après avoir fini de parcourir le mot

# Utilisation de la fonction myCount pour obtenir le nombre d'occurrences de la lettre
c = myCount(mot, l)



print('La lettre', l, 'a été utilisée', c, 'fois')
