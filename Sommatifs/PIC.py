#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
# 2020/12/06

# 1. Présentation entre utilisateur et console

print("")
print("Insérer votre nom d'utilisateur:")
name= input()
print("")
print("Salut",name,", je me nomme MathMaj et je suis un magicien!")
print("Aimez-vous les mathématiques? (répondre par oui ou non)")
réponse_1= input().lower()

# Devinette 1

if réponse_1 == "oui":
  print("Excellent! Je vais essayer de vous tromper avec un problème à résoudre!")
  estVrai= True
elif réponse_1== "non":
  print("C'est dommage, on aurait pu s'amuser ensemble avec les maths!")
  estVrai= False
else:
  print("Je n'ai pas compris votre réponse. Répondez simplement par oui ou non après avoir cliqué sur Run encore une fois.")
  estVrai= False

# Devinette 1
if estVrai:
  print("")
  print("Alors commençons avec la première devinette! Soit le nombre entier x:")
  print("Je suis divisible par 3;")
  print("La somme de chacun de mes chiffres est 9;")
  print("Je suis plus grand que 110, mais moins grand que 130.")
  print("Aussi, mes chiffres sont chacunes trouvés une fois seulement dans le nombre. Quel est ce nombre?")
  print("Entrer votre réponse ci-dessous:")

# Code de la réponse de devinette 1
  choix= input()
  if choix == "126":
    estVrai= True
    print("Bravo! Vous avez la bonne réponse!")
  elif choix != "126":
    print("Votre réponse n'est pas valide, vous avez une autre chance")
    chance= input()
    if chance== "126":
      estVrai= True
      print("Bravo, vous avez eu la bonne réponse cette fois.")
    elif chance!= "126":
      estVrai= False
      print("Mauvaise réponse, vous pouvez essayer encore en cliquant sur Run.")

# DEVINETTE 2
if estVrai:
  print("")
  print("C'est le temps pour la prochaine devinette!")
  print("Je suis un nombre pair à deux chiffres. Je suis divisible par 2, 3, et 6, et la racine carré de mon nombre est aussi soit 2,3, OU 6. Quand on inverse la position de mes chiffres, je devient un nombre impair qui est plus grand que mon nombre initial par 27 et je deviens impair.")
  print("Quel est mon nombre final?")

# Code de la réponse de devinette 2
  final= input()
  if final== "63":
    print("Bravo, vous avez la bonne réponse!")
    print("Félicitations! Vous êtes très intelligent!")
  else:
    print("Votre réponse n'est pas valide, vous avez une autre chance:")
    final2= input()
    if final2== "63":
      print("Bravo, vous avez eu la bonne réponse cette fois.")
    else:
      print("Mauvaise réponse, revenez une autre fois.")
      estVrai= False

if estVrai:
  print("Avez vous aimé les deux devinettes?")
  answer= input().lower()
  if answer== "oui":
    print("Cela est effectivement la réponse que l'on cherche. Merci beaucoup pour avoir pour avoir participé!")
  elif answer== "non":
    print("AH! C'est dommage! Je m'amusait bien avec toi! Reviens demain pour de nouvelles devinettes, possiblement dans un autre domaine!")
  else:
    print("Je n'ai pas compris donc je vais assumer que c'est un oui. Merci pour avoir participé!")