#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
#2020/12/09

g= True
while g:
  print("Pour trouver les bonds d'un nombre de votre choix qui est inférieur à 50 suit les étapes:")
  print("Pour commencer à jouer, tape « a »")
  print("Pour essayer avec un autre nombre après avoir joué, tape « c » ")  
  print("Pour quitter le programme après avoir joué, tape « b »")
  choix= input().lower()
  if choix== "a":
    print("choisis un nombre inférieur à 50:")
    bond= 0
    num= "0"
    while num.isdigit():
      g=True
      repeat= False
      bond += int(num)
      num= input()
      for i in range(0,50, int(num)):
       print(i)
       choice= input()
      if choice== "b":
        g= False
        print("Merci pour avoir exploré avec nous!")
      elif choice== "c":
        g= True