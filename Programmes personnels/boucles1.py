#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
# 2020/12/09

produit= 1
num= "1"
while num.isdigit():
    produit= produit * int(num)    
    print("Entrer un nombre entier:")
    print("Taper « = » pour afficher le résultat:") 
    num=input()
print("Le produit est", produit)

print("choisit un de ses nombres pour que je divise le produit précédent:")
for i in range(1,4):
  print(i)
  choix= int(input())
  break

