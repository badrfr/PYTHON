def compter_voyelles(mot):
    voyelles = 'aeiouyAEIOUY'  # Inclut les voyelles en majuscules et minuscules
    nombre_voyelles = 0

    for lettre in mot:
        if lettre in voyelles:
            nombre_voyelles += 1

    return nombre_voyelles

# Exemple d'utilisation
mot = input("Entrez un mot: ")
print("Le nombre de voyelles dans le mot est:", compter_voyelles(mot))
