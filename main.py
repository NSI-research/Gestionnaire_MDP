import json
import ast
import time
alphabet = {

    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
    '0': 53,
    '1': 54,
    '2': 55,
    '3': 56,
    '4': 57,
    '5': 58,
    '6': 59,
    '7': 60,
    '8': 61,
    '9': 62,
    '?': 63,
    ';': 64,
    ':': 65,
    '!': 66,
    '.': 67,
    '/': 68,
    '(': 69,
    ')': 70,
    '&': 71,
    ' ': 72
}
def charger_dictionnaire():
    try:
        with open('dictionnaire.json', 'r') as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return {}
def sauvegarder_dictionnaire(dico):
    with open('dictionnaire.json', 'w') as fichier:
        json.dump(dico, fichier)
dico = charger_dictionnaire()
def hashi(o, o2=888):
    l = []
    l2 = []
    r = []
    r2 = []
    for i in o:
        for (letter, num) in alphabet.items():
            if letter == i:
                l.append(num)
        for i in l:
            r.append(hex(i))
    if o2 != 888:
        for i in o2:
            for (letter, num) in alphabet.items():
                if letter == i:
                    l2.append(num)
        for i in l2:
            r2.append(hex(i))
        y = input(f"Confirmez-vous l'ajout de l'utilisateur {o} avec le mot de passse {o2} ?")
        if y != "Oui" and y != "oui":
            print("La demande est donc annulé.")
            return
        dico[json.dumps(r)] = json.dumps(r2)
        print(f"C'est good, {o} à été associé à {o2}")
    else:
        del dico[json.dumps(r)]
    sauvegarder_dictionnaire(dico)
    time.sleep(20)
    return r
def unhashi(o):
    l = []
    r = []
    p = ""
    mdpf = []
    for i in o:
        for (letter, num) in alphabet.items():
            if letter == i:
                l.append(num)
    for i in l:
        r.append(str(hex(i)))
    for (user, mdp) in dico.items():
        if r == ast.literal_eval(mdp):
            for i in ast.literal_eval(user):
                mdpf.append(int(i, 16))
            for i in mdpf:
                for (letter, num) in alphabet.items():
                    if num == int(i):
                        p += str(letter)
            print(f"{o} est le mot de passe de l'utilisateur {p}")
            return p
        elif r == ast.literal_eval(user):
            for i in ast.literal_eval(mdp):
                mdpf.append(int(i, 16))
            for i in mdpf:
                for (letter, num) in alphabet.items():
                    if num == int(i):
                        p += str(letter)
            print(f"{o} est l'utilisateur du mot de passe {p}")
            time.sleep(20)
            return p
    time.sleep(2)
    print("Aucune correspondance trouvée.")

    time.sleep(20)
x = ''
while x != "1" and x != "2" and x != "3":
    x = input("Que souhaitez vous ?\n\n\t1. Ajouter un mdp\n\t2. Chercher un mdp\n\t3. Supprimer un mdp\n\nDites 1 ou 2 : ")
    if x != "1" and x != "2" and x != "3":
        print("\nMerci de réhiterer.\n")
if x == "1":
    nuser = input("\nLe nom d'utilisateur est : ")
    nmdp = input("Le mdp est : ")
    hashi(nuser, nmdp)
elif x == "2":
    unhashi(input("Donnez un user, ou bien un mot de passe (attention, celui-ci doit correspondre parfaitement à celui que vous cherchez) : "))
else:
    try:
        hashi(input("Donnez le User à supprimer : "))
        print("User/MDP correctement supprimé.")
        time.sleep(20)
    except KeyError:
        print("\nEntrée invalide.")
        time.sleep(20)