#Tâche: Listes-cumulatif
#Par David Malek, maldav31@ecolecatholique.ca
#2020/12/09
import random
print("Salut, je suis un générateur qui choisi des repas au hasard pour que vous puissiez choisir ce que vous deviez manger!")
print("SVP entrer les noms des repas que vous pensez à manger après avoir cliqué sur Enter")
print("Cliquez sur '=' après avoir fini la liste.")
print("Si vous faites des erreures en écrivant la liste, tapez 'r' sans taper'='.")
enter= input()
print("Lister les repas de votre choix ci-dessous pour que j'en choisi un parmi la liste:")

#Création du menu
menu=[]
repeat= True
while repeat:
  meal= input()  
  menu.append(meal)
  if meal== '=':
    repeat= False      
    menu.remove("=")
  elif meal== 'r':
    repeat= True
    menu.clear()
    print("D'accord, vous pouvez réécrire votre liste.")

#Choix au hasard par le programme
print("Voici la liste que vous avez rédigé:", menu)
print("Cliquez Enter pour que je choisis au hazard parmi les repas de cette liste:")
enter=input()
x=random.choice(menu)
print("Le repas que j'ai choisi est:", x)
print("")
print("J'espère que mon choix de repas est délicieux!")
print("")
print("Cliquez Enter pour passer à la prochaine étape.")
enter= input()

#Combo?
print("Voulez-vous un combo de votre choix? Si oui, tapez 'o' pour continuer. Si non, tapez 'q' pour quitter.")
proceed= input().lower()

#Si utilisateur veut un combo
if proceed== 'o':
  print("Parmi les repas de votre liste créé, lequel voulez-vous comme addition à votre repas?")
  print("(Vous avez", len(menu), "repas listés.)")
  print("Je vous donne le choix de choisir de cette liste pour votre combo.")
  print("SVP écrire le nom de l'item au complet. Voici le menu: ", menu)
  print("")
  print("Votre choix:")
  choice= input().lower()

  #Choix de combo
  if choice >= menu[0] and choice <= menu[len(menu)-1]:
    print("Donc, vous devez manger:", x, "et", choice)
    print("Tapez 'q' pour quitter")
    quit= input().lower()

    ##quitter après avoir choisi combo
    while quit != "q":
      print("Je n'ai pas compris, tapez 'q' pour quitter.")
      choix = input()
    else:
      if quit== "q":
        repeat= False
        print("Mangez bien et revenez encore une autre fois!")
  
  else:
    print("Ceci n'est pas dans la liste. SVP, écrire le nom du repas que vous aimerez ajouter à votre commande pour le combo")
elif proceed== "q":
  repeat= False
  print("Mangez bien et revenez encore une autre fois!")
else:
  print("Je n'ai pas compris")
