def function(list):
    list2 = set(list)
# On a infecter la liste dans un ensemble
    for x in list:
        if x < 0:
# On parcourt la liste et on verifie si on a des valeurs > 0
            if x*(-1) not in list2:
                list2.append(x)
# Si c'est le cas on prend sa valeur absolut et on check si elle est deja dans la list2, si c'est pas le cas on l'ajoute à la liste2
        else:
            if x * (-1) in list2:
                list2.pop(x * (-1))
                list2.append(x)
# Sinon on supprime la valeur absolut de la valeur negatif de la liste 2 et on ajoute son couple positif dans la liste2
# Pour mieux comprendre ( si la liste2 contient -6 et qu'il y a un 6 dans list (initial) on supprime le -6 de la list2et on ajoute le 6 dans la list2
            else:
                list2.append(x)
# Sinon on ajoute directement la valeur
    somme = 0
    for x in list2:
        somme = somme + x
    return somme
# Et on fin on fait la somme des valeurs de la list2

print(function([-2, -5, 6, -2, -3, 1, 5, -6]))