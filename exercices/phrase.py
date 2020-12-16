phrases = []
consignes = []



def mon_mad_lib():

    phrases.append("{} fait des biscuits le jour de la veille de Noël.")
    consignes.append("nom d'une femelle dans ta famille (mère,soeur,enfant...):")
    phrases.append("Elle utilise un {} pour déchiqueter la pâte.")
    consignes.append("outil de la cuisine, nom masculin:")
    phrases.append("Une fois qu'elle a fini de la mettre en pièce, elle a mis les morceaux de la pâte dans le four. Après que les biscuits étaient cuits, elle les a placé sur une {}.")
    consignes.append("nom féminin d'un objet qui peut soutenir des choses.")
    phrases.append("À minuit, Père Noël a réveillé tout le monde quand il a {} avec un très grand bruit.")
    consignes.append("verbe écrit au participe passé et s'accorde avec l'auxiliaire avoir:")
    phrases.append("Les enfants ont reconnu qui les a réveillé, alors ils sont allés voir le Père Noël. Ils l'ont demandé pour des {}.")
    consignes.append("nom commun au pluriel(masculin ou féminin) qui désigne un objet:")
    phrases.append("Le Père Noël a accepté leurs demandes, tout pendant qu'il mangeait des biscuits. Il leur a aussi remercié pour les biscuits en leur donnant des {}.")    
    consignes.append("nom commun au pluriel(masculin ou féminin) qui désigne un objet autre que celui de ci-haut:")

mon_mad_lib()


mots = []

for c in consignes:

    print("Taper un mot qui est un(e) {}".format(c))
    mots.append(input())



print("Quand tu est prêt(e) pour le résultat, tape Enter")
input()

for i in range(len(phrases)):
    print(phrases[i].format(mots[i]))

print("\n Passez un Joyeux Noël!")