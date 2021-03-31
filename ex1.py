open = ["[", "{", "("]
# La liste des ouvrantes
close = ["]", "}", ")"]
# La liste des fermantes

def function(list):
    last_open = []
# last_open va parcourir la chaine en stockant les derniéres parties ouvrantes

    for x in list:
        if x in open:
            last_open.append(x)
# last_open.append(x) ajoute la derniére partie ouvrante lors de son parcours (append=ajoute)
        elif x in close:
            pos = close.index(x)
# La (pos) donne pour chaque charactére de la liste close un indice
            if ((len(last_open) > 0) and (open[pos] == last_open[len(last_open) - 1])):
                last_open.pop()
# Cette derniére cherche à verfier si le last_open a stocker des charactéres, si c'est le cas on verifie si l'indice de la derniére partie ouvrante égale à l'indice de la derniére partie fermante
# Si c'est le cas on supprime la derniére partie ouvrante de la liste last_open en passant par (pop) qui supprime le dernier element de la liste
            else:
                return "Unbalanced"
# Si les derniéres conditions ne sont pas verifier on affiche unbalanced
    if len(last_open) == 0:
        return "Balanced"
# Si la liste des last_open devient vide on affiche balanced
    else:
        return "Unbalanced"

print(function("[{()}]"))