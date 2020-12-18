#Tâche: Listes-cumulatif
#Par David Malek, maldav31@ecolecatholique.ca
#2020/12/09

print("Salut, je suis un générateur qui choisi des repas au hasard pour que vous puissiez choisir ce que vous deviez manger!")
print("SVP entrer les noms des repas que vous pensez à manger après avoir cliqué sur Enter")
print("Cliquez sur '=' après avoir fini la liste")
print("Pour répéter le processus, tapez 'r' pour recommencer immédiatement.")
enter= input()
print("Lister les repas de votre choix ci-dessous pour que j'en choisi un parmi la liste:")
menu=[]
repeat= True
while repeat:
  meal= input()  
  menu.append(meal)
  if meal== '=':
    repeat= False
    menu.remove("=")
    print("Voici la liste que vous avez rédigé:", menu)
    print("Cliquez Enter pour que je choisis au hazard parmi les repas de cette liste:")
    enter=input()
    import random
    print("Le repas que j'ai choisi est:", random.choice(menu))
    print("")
    print("J'espère que mon choix de repas est délicieux!")
  elif meal== 'r':
    repeat= True
    menu.remove('r')
    print("D'accord, vous pouvez réécrire votre liste")