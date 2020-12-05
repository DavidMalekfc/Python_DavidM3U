#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
# 2020/12/06
print("")
print("Insérer votre nom d'utilisateur:")
name= input()
print("")
print("Salut",name,", je me nomme MathMaj et je suis un magicien!")
print("Aimez-vous les mathématiques? (répondre par oui ou non)")
réponse_1= input().lower()
if réponse_1 == "oui":
  print("Excellent! Je vais essayer de vous tromper avec un problème à résoudre!")
  print("")
  print("Alors commençons avec la première devinette! Soit le nombre entier x:")
  print("Je suis divisible par 3;")
  print("La somme de chacun de mes chiffres est 9;")
  print("Je suis plus grand que 110, mais moins grand que 130.")
  print("Aussi, mes chiffres sont chacunes trouvés une fois seulement dans le nombre. Quel est ce nombre?")
  print("Entrer votre réponse ci-dessous:")
  choix= input()
  if choix== "126":
    print("Bravo! Vous avez la bonne réponse!")
    print("")
    print("C'est le temps pour la prochaine devinette!")
    print("Je suis un nombre pair à deux chiffres. Je suis divisible par 2, 3, et 6, et la racine carré de mon nombre est aussi sois 2,3, OU 6. Quand on inverse la position de mes chiffres, je devient un nombre impair qui est plus grand que mon nombre initial par 27 et je deviens impair.")
    print("Quel est mon nombre final?")
    final= input()
    if final== "63":
      print("Bravo, vous avez la bonne réponse!")
      print("Félicitations! Vous êtes très intelligent!")
    else:
      print("Votre réponse n'est pas valide, vous avez une autre chance:")
      chance= input()
      if chance== "63":
        print("Bravo, vous avez eu la bonne réponse cette fois.")
      else:
        print("Mauvaise réponse, revenez une autre fois.")
  else:
    print("Votre réponse est fausse. Si vous voulez essayer encore, cliquez sur le bouton: Run ")
elif réponse_1 == "non":
  print("Je vais essayer de changer votre opinion avec un problème amusant!")
  print("")
  print("Alors commençons avec la première devinette! Soit le nombre entier x:")
  print("Je suis divisible par 3;")
  print("La somme de chacun de mes chiffres est 9;")
  print("Je suis plus grand que 110, mais moins grand que 130.")
  print("Aussi, mes chiffres sont chacunes trouvés une fois seulement dans le nombre. Quel est ce nombre?")
  print("Entrer votre réponse ci-dessous:")
  choix= input()
  if choix== "126":
    print("Bravo! Vous avez la bonne réponse!")
    print("")
    print("C'est le temps pour la prochaine devinette!")
    print("Je suis un nombre pair à deux chiffres. Je suis divisible par 2, 3, et 6, et la racine carré de mon nombre est aussi sois 2,3, OU 6. Quand on inverse la position de mes chiffres, je devient un nombre impair qui est plus grand que mon nombre initial par 27 et je deviens impair.")
    print("Quel est mon nombre final?")
    final= input()
    if final==63:
      print("Bravo, vous avez la bonne réponse!")
      print("Félicitations! Vous êtes très intelligents!")
    else:
      print("Votre réponse n'est pas valide, vous avez une autre chance:", final)
      if final== 63:
        print("Bravo, vous avez eu la bonne réponse cette fois.")
  else:
    print("Votre réponse est fausse. Si vous voulez essayer encore, cliquez sur le bouton: Run ")
else:
  print("Je n'ai pas compris votre réponse. Répondez simplement par oui ou non après avoir cliqué sur Run encore une fois.")