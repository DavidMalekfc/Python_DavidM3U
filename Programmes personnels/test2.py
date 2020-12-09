#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
# 2020/12/06

### 1. Présentation entre utilisateur et console

print("")
print("Insérer votre nom d'utilisateur:")
name= input()
print("")
print("Salut",name,", je me nomme MathMaj et je suis un magicien!")
print("Aimes-tu les mathématiques? (répondre par oui ou non)")

## 1.1 Réponse oui ou non (si « oui », il continue. Si « non », ne peut pas continuer)

réponse_1= input().lower() 
if réponse_1 == "oui":
  print("Excellent! Je vais essayer de vous tromper avec un problème à résoudre!")
  estVrai= True
elif réponse_1== "non":
  print("C'est dommage, on aurait pu s'amuser ensemble avec les maths!")
  estVrai= False 
else:
  print("Je n'ai pas compris votre réponse. Répondez simplement par oui ou non après avoir cliqué sur Run encore une fois.")
  estVrai= False 

### 2. DEVINETTE 1
if estVrai:
  print("")
  print("DEVINETTE 1:")
  print("Alors commençons avec la première devinette! Soit le nombre entier x:")
  print("Je suis divisible par 3;")
  print("La somme de chacun de mes chiffres est 9;")
  print("Je suis plus grand que 110, mais moins grand que 130.")
  print("Aussi, mes chiffres sont chacuns trouvés une fois seulement dans le nombre. Quel est ce nombre?")
  print("Entrer votre réponse ci-dessous:")
  
  ## 2.1 Code de la réponse de devinette 1
  choix= input()
  while choix != "126":
    print("Mauvaise réponse, essayes encore:")
    choix = input()
  else:
    if choix == "126":
      print("Bravo! C,est la bonne réponse!")
      print ("Cliques sur Enter pour passer à la prochaine question!")
      enter= input()

### 3. DEVINETTE 2
if estVrai:
  print("")
  print("DEVINETTE 2:")
  print("C'est le temps pour la prochaine devinette!")
  print("Je suis un nombre pair à deux chiffres.") 
  print("Je suis divisible par 2, 3, et 6, et la racine carré de mon nombre est aussi soit 2,3, OU 6.")
  print("Quand on inverse la position de mes chiffres, je devient un nombre impair") 
  print("qui est plus grand que mon nombre initial par 27.")
  print("Quel est mon nombre final?")

  ## 3.1 Code de la réponse de devinette 2 
  choix = input()
  while choix != "63":
    print("Mauvaise réponse, essayes encore:")
    choix = input()
  else:
    if choix == "63":
      print("Bravo! C'est la bonne réponse!")
      print ("Cliques sur Enter pour passer à la prochaine étape:")
      enter= input()

### 4. Rétroaction
if estVrai:
  print("")
  print("")
  print("As-tu aimé les deux devinettes? (répondre par oui ou non)")
  answer= input().lower()
  if answer== "oui":
    print("Je suis content que tu les aimes. Merci beaucoup pour avoir participé!")
  elif answer== "non":
    print("AH! C'est dommage! Je m'amusait bien avec toi! Reviens demain pour de nouvelles devinettes, possiblement dans un autre domaine!")
  else:
    print("Je n'ai pas compris donc je vais présumer que c'est un oui. Merci pour avoir participé!")