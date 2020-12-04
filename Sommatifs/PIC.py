#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
# 2020/12/06
print("")
print("Insérer votre nom d'utilisateur:")
name= input()
print("")
print("Salut", name,", je me nomme MathMaj et je suis un magicien!")
print("Aimez-vous les mathématiques? (répondre par oui ou non)")
réponse_1= input().lower()
if réponse_1 == "oui":
  print("Excellent! Je vais essayer de vous tromper avec un problème à résoudre!")
  print("")
  print("Alors commençons notre devinette! Soit le nombre entier x:")
  print("Je suis divisible par 3;")
  print("La somme de chacun de mes chiffres est 9;")
  print("Je suis plus grand que 100, mais moins grand que 130.")
  print("Aussi, mes chiffres sont chacunes trouvés une fois seulement dans le nombre. Quel est ce nombre?")
  print("Entrer votre réponse ci-dessous:")
  choix= input()
  if choix== "126":
    print("Bravo! Vous avez la bonne réponse!")
    print("Merci pour avoir participé! Revenez à chaque jour pour de nouvelles devinettes!")
  else:
    print("Votre réponse est fausse. Si vous voulez essayer encore, cliquez sur le bouton: Run ")
elif réponse_1 == "non":
  print("Je vais essayer de changer votre opinion par un problème amusant!")
  print("")
  print("Alors commençons notre devinette! Soit le nombre entier x:")
  print("Je suis divisible par 3;")
  print("La somme de chacun de mes chiffres est 9;")
  print("Je suis plus grand que 100, mais moins grand que 130.")
  print("Aussi, mes chiffres sont chacunes trouvés une fois seulement dans le nombre. Quel est ce nombre?")
  print("Entrer votre réponse ci-dessous:")
  choix= input()
  if choix== "126":
    print("Bravo! Vous avez la bonne réponse!")
    print("")
    print("Merci pour avoir participé! Revenez à chaque jour pour de nouvelles devinettes!")
  else:
    print("Votre réponse est fausse. Si vous voulez essayer encore, cliquez sur le bouton: Run ")
else:
  print("Je n'ai pas compris votre réponse. Répondez simplement par oui ou non après avoir cliqué sur Run encore une fois.")