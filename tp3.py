from collections import defaultdict
from lexique import *
#import unidecode

EQUIV_NON_ACCENTUE = {'à':'a', 'â': 'a', 'ä': 'a', 'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e'
                      , 'î':'i', 'ï':'i', 'ô': 'o', 'ö': 'o', 'ù':'u', 'û':'u', 'ü':'u', 'ÿ':'y'}

def sort(s):
    """
    Renvoie une chaine de caractères contenant tous les caractères de la chaîne passée en paramètre triés dans lordre lexicographique.
    
    :param s: (str) une chaîne de caractères
    :return: (str) une chaîne de caractères contenant les caractères de s triés dans l’ordre croissant
    CU: any
    
    Exemple:
    >>> sort ('timoleon')
    'eilmnoot'
    >>> sort ('ceciestuntest')
    'cceeeinsstttu'
    """
    s_liste = list(s)
    return "".join(sorted(s_liste))


def sont_anagrammes1(s1, s2):
    """
    Vérifie si les deux chaînes sont des anagrammes en utilisant la fonction sorted().
    
    :param s2(s1,): (str) deux chaînes de caractères
    :return: (bool) True si s1 et s2 sont anagrammatiques, False sinon
    CU: any
    
    Exemples:
    >>> sont_anagrammes1('orange', 'organe')
    True
    >>> sont_anagrammes1('orange','Organe')
    False
    """
    l1 = list(s1)
    l2 = list(s2)
    if sorted(l1) == sorted(l2):
        return True
    return False

def sont_anagrammes2(s1, s2):
    """
    Vérifie si les deux chaînes sont des anagrammes en utilisant des dictionnaires.
    
    :param s2(s1,): (str) deux chaînes de caractères
    :return: (bool) True si s1 et s2 sont anagrammatiques, False sinon
    CU: any
    
    Exemples:
    >>> sont_anagrammes2('orange', 'organe')
    True
    >>> sont_anagrammes2('orange','Organe')
    False
    """
    dico1 = defaultdict(int)
    dico2 = defaultdict(int)
    for c in s1:
        dico1[c] += 1
    for c in s2:
        dico2[c] += 1
    return dico1 == dico2

def sont_anagrammes3(s1, s2):
    """
    Vérifie si les deux chaînes sont des anagrammes en utilisant la méthode count.
    
    :param s2(s1,): (str) deux chaînes de caractères
    :return: (bool) True si s1 et s2 sont anagrammatiques, False sinon
    CU: any
    
    Exemples:
    >>> sont_anagrammes3('orange', 'organe')
    True
    >>> sont_anagrammes3('orange','Organe')
    False
    """
    ensemble_carac = set(s1).union(set(s2))
    for c in ensemble_carac:
        if s1.count(c) != s2.count(c):
            return False
    return True


def bas_case_sans_accent(s):
    """
    Renvoie une châine de caractères identique à celle passée en paramètre sauf pour les lettres majuscules et accentuées qui sont converties en leur équivalent minuscule non accentué.
    
    :param s: (str) La chaine de caracètres à convertir
    :return: (str) La même chaîne mais convertie 
    
    CU: any
    
    Exemples:
    >>> bas_case_sans_accent('Orangé')
    'orange'
    """
    res = ""
    s = s.lower()
    for c in s:
        if c in EQUIV_NON_ACCENTUE:
            res += EQUIV_NON_ACCENTUE[c]
        else:
            res += c
    return res


def sont_anagrammes4(s1, s2):
    """
    Vérifie si les deux chaînes sont des anagrammes en utilisant la fonction bas_case_sans_accent().
    
    :param s2(s1,): (str) deux chaînes de caractères
    :return: (bool) True si s1 et s2 sont anagrammatiques, False sinon
    
    CU: any
    
    Exemples:
    >>> sont_anagrammes4('orange', 'organe')
    True
    >>> sont_anagrammes4('orange','Organe')
    True
    """
    s1, s2 = bas_case_sans_accent(s1), bas_case_sans_accent(s2)
    ensemble_carac = set(s1).union(set(s2))
    for c in ensemble_carac:
        if s1.count(c) != s2.count(c):
            return False
    return True


def anagrammes(mot):
    """
    Renvoie la liste des anagrammes d'un mot passé en paramètre, ces anagrammes appartenant au lexique. Utilise la fonction sont_anagrammes4().
    :param mot: (str) un mot dont on veut les anagrammes.
    :return: (list) la liste des mots figurant dans le LEXIQUE qui sont des anagrammes de mot
    
    CU: any
    
    Exemple:
    >>> anagrammes('orange')
    ['onagre', 'orange', 'orangé', 'organe', 'rongea']
    >>> anagrammes('info')
    ['foin']
    >>> anagrammes('Calbuth')
    []
    """
    res = []
    for c in LEXIQUE:
        if sont_anagrammes4(mot, c):
            res.append(c)
    return res

def cle(s):
    """
    Calcule et renvoie la clé que doit avoir un mot donné dans le dictionnnaire.
    
    :param s: (str) le mot dont on veut la clé
    :return: (str) la clé du mot
     
    CU: any
    
    Exemples:
    >>> cle('Orangé')
    'aegnor'
    """
    s = bas_case_sans_accent(s)
    s = sort(s)
    return s


def anagrammes2(mot):
    """
    Renvoie la liste des anagrammes d'un mot passé en paramètre, ces anagrammes appartenant au lexique. Utilise le dictionnaire ANAGRAMMES.
    
    :param mot: (str) un mot dont on veut les anagrammes.
    :return: (list) la liste des mots figurant dans le LEXIQUE qui sont des anagrammes de mot
    
    CU: any
    
    Exemple:
    >>> anagrammes('orange')
    ['onagre', 'orange', 'orangé', 'organe', 'rongea']
    >>> anagrammes('info')
    ['foin']
    >>> anagrammes('Calbuth')
    []
    """
    return ANAGRAMMES[cle(mot)]


def odometre_incrementation(compteur, compteur_maximum):
    """
    Incremente une liste d'entiers comme le ferait un odometre (par la droite). Si toutes les valeurs sont déjà au maximum, alors le compteur est renvoyé tel quel.
    
    :param compteur: (list[int]) Le compteur a incrémenter
    :param compteur_maximum: (int ou list[int]) Si le type est int: La valeur maximale (comprise) pour toutes les cases de compteur. Si le type est list: Les valeurs maximales pour les cases de compteurs une à une
    :return: (list[int])
    
    CU: len(compteur) == len(compteur_maximum) 
    
    Exemples:
    >>> odometre_incrementation([0,0,0], 5)
    [0, 0, 1]
    >>> odometre_incrementation([0,0,25], 25)
    [0, 1, 0]
    >>> odometre_incrementation([0, 1, 1, 3], [1, 1, 1, 3])
    [1, 0, 0, 0]
    """
    
    length = len(compteur)
    
    # Si c'est un entier, on crée une liste avec toutes les valeurs égales.
    if type(compteur_maximum) == type(5):
        compteur_maximum = [compteur_maximum for i in range(length)]
    
    # On crée une liste compteur_bool en paralelle avec la liste compteur.
    # Si un élement à un index i dans compteur est à son maximum, 
    # alors l'element au même index dans compteur_bool sera True
    compteur_bool = []
    for i, valeur in enumerate(compteur):
        if valeur == compteur_maximum[i]:
            compteur_bool.append(True)
        else:
            compteur_bool.append(False)

    for i in range(length-1, -1, -1): # On part de la droite.
        if compteur_bool[i] == False: # Si la valeur a la position i n'est PAS au maximum, on l'incrémente.
            compteur[i] += 1
            while i != length-1: # On remonte le compteur pour remettre a zéro les éventuels élements avant celui que l'on vient d'incrémenter
                i += 1
                compteur[i] = 0
                
            # On a incrémenté la valeur voulue, on peut sortir de la boucle for.
            break
    return compteur


def anagrammes_phrase(phrase):
    """
    Renvoie la liste des phrases obtenues en remplaçant chacun des mots par leurs anagrammes.
    
    :param phrase: (str) Une phrase dont on veut voir les anagrammes
    :return: (list) la liste des phrases obtenues
    
    CU: any
    
    Exemples:
    >>> anagrammes_phrase('Mange ton orange')
    ['mange ont onagre', 'mange ont orange', 'mange ont orangé', 'mange ont organe', 'mange ont rongea', 'mange ton onagre', 'mange ton orange', 'mange ton orangé', 'mange ton organe', 'mange ton rongea', 'mangé ont onagre', 'mangé ont orange', 'mangé ont orangé', 'mangé ont organe', 'mangé ont rongea', 'mangé ton onagre', 'mangé ton orange', 'mangé ton orangé', 'mangé ton organe', 'mangé ton rongea']
    """
    res_liste = []
    liste_anagrammes = []
    
    # Rajoute la liste des anagrammes d'un mot dans liste_anagrammes.
    # Si le mot n'est pas dans LEXIQUE, rajoute juste une liste contenant le mot
    for mot in phrase.split():
        mot = bas_case_sans_accent(mot)
        if mot in LEXIQUE:
            liste_anagrammes.append(anagrammes2(mot))
        else:
            liste_anagrammes.append([mot])
            
    # compteur_index est une liste qui représente les index des anagrammes dans liste_anagrammes,
    # Grâce à la fonction odometre_incrementation, il va prendre toutes les combinaisons d'index possible,
    # Ainsi, ça va permettre d'iterer à travers TOUTES les combinaisons possible des anagrammes.
    # Bon, il existe peut être un moyen plus simple ou une fonction integrée, mais j'ai pas trouvé.
    
    compteur_index = [0 for i in range(len(liste_anagrammes))]
    compteur_index[-1] = -1 # Compense l'incrémentation dans le while.
    compteur_index_max = [len(i)-1 for i in liste_anagrammes]   # Représente les valeurs maximales que pourront prendre les élements dans compteur_index.
    while compteur_index != compteur_index_max:
        compteur_index = odometre_incrementation(compteur_index, compteur_index_max)
        phrase_anagramme = []
        for i in range(len(compteur_index)):
            random_word = liste_anagrammes[i][compteur_index[i]]
            phrase_anagramme.append(random_word)
        phrase_anagramme = " ".join(phrase_anagramme)
        res_liste.append(phrase_anagramme)
        
    return res_liste



print("len(LEXIQUE) =", len(LEXIQUE), "len(set(LEXIQUE)) =", len(set(LEXIQUE)))
print("Le lexique contient", len(LEXIQUE), "mots")
if len(LEXIQUE) == len(set(LEXIQUE)):
    print("Le lexique ne contient aucun doublon")
else:
    print("Le lexique contient des doublons")

print("Anagrammes du mot 'chien' avec la premiere fonction de recherche: ", anagrammes("chien"))

# Anagrammes d'un mot : seconde méthode
# Il n'est pas raisonnable de prendre les mots du lexique pour clés, on aurait beaucoup trop de clés avec la même valeur
print("Création du dictionnaire d'anagrammes...")
ANAGRAMMES = defaultdict(list)
for s in LEXIQUE:
    ANAGRAMMES[cle(s)].append(s)
print("Création terminée !")

print("Anagrammes du mot 'chien' avec la seconde fonction de recherche: ", anagrammes2("chien"))

# Pour des raisons de lisibilité, j'ai limité le nombre de mots à 5
print("Methode 1:")
for i in range(5):
    print(anagrammes(LEXIQUE[i]))

print("Methode 2:")
for i in range(5):
    print(anagrammes2(LEXIQUE[i]))
print("On constate que la méthode 2 est beaucoup BEAUCOUP plus rapide")

print("Anagrammes de la phrase 'Mange ton orange':",anagrammes_phrase('Mange ton orange'))

# if __name__ == "__main__":
# 
#     import doctest
# 
#     doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)