#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
#2020/12/09

Bon= True
while Bon:
  print("Ceci est un programme qui compte jusqu'à 50 par des bonds de 2:")
  print("Pour lister des bonds de 2, tape « a »")
  print("Pour lister des bonds de 3, tape « b »")
  print("Pour ne plus visionner, tape sur n'importe quel lettre ")  
  choix= input().lower()
  if choix== "a":
    print("")
    Bon= True
    for i in range(0,50,2):
       print(i)
    print("Voici la liste!")
  elif choix== "b":
    Bon= True
    for c in range(0,50,3):
      print(c)
  else:
    Bon= False
    print("Merci pour avoir visionné! Reviens pour de l'aide une autre fois!")
        