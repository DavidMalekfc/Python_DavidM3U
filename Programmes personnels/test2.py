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

# Devinette 1 si la personne aime mathématiques

if réponse_1 == "oui":
  print("Excellent! Je vais essayer de vous tromper avec un problème à résoudre!")
  estVrai= True
elif réponse_1== "non":
  print("C'est dommage")
  estVrai= False

if estVrai:
  print("")
  print("Alors commençons avec la première devinette! Soit le nombre entier x:")
  print("Je suis divisible par 3;")
  print("La somme de chacun de mes chiffres est 9;")
  print("Je suis plus grand que 110, mais moins grand que 130.")
  print("Aussi, mes chiffres sont chacunes trouvés une fois seulement dans le nombre. Quel est ce nombre?")
  print("Entrer votre réponse ci-dessous:")

# Code avec la réponse de devinette 1
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