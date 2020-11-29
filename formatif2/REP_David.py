#Tâche: input et opérations en python
#Par David Malek, maldav31@ecolecatholique.ca
# 2020/11/29
print("")
print("Ceci est un programe qui fournit le produit de deux nombres.")
print("NOTE: La réponse fournie sera en nombre décimal.")
print("")
print("Entrer le premier nombre:")
Premier_nombre= input()
Premier_nombre= float(Premier_nombre)
print("Entrer le deuxième nombre:")
Deuxième_nombre= input()
Deuxième_nombre= float(Deuxième_nombre)
print("Écrire la réponse arrondi de ce que vous pensez:")
VOTRE_RÉPONSE= input()
VRAI_RÉPONSE= Premier_nombre * Deuxième_nombre
print("La bonne réponse:")
print(VRAI_RÉPONSE)