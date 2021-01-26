#Tâche: Programme pour projet pgzero en python
#Par David Malek, maldav31@ecolecatholique.ca
#2021/01/26
import pgzrun
import random

WIDTH=500  #Longueur de la base de la fenêtre
HEIGHT=300 #Hauteur de la 
dead= False 

#Sprite space
space= Actor("space.png")


# Sprite jetpack
jetpack= Actor("jetpack.png")
jetpack.pos= (50, 250) #Position initial de jetpack


#Sprite rocket
rocket= Actor("rocket2.png")
rocket.x= WIDTH
rocket.y= 150 


score= 0 #Score initial au commencement
speed= 2 # Vitesse initiale des fusées

print(rocket.height, jetpack.height)

def draw():
  space.draw()
  screen.draw.text("Score: " + str(score), midtop = (WIDTH / 2, 5), fontsize = 30)
  if not dead:
    jetpack.draw()
    rocket.draw()
  else:
    screen.draw.text("YOU DIED", center= (WIDTH/2, HEIGHT/2), fontsize = 50)


def update():
  global speed, score, dead

  #Condition quand bonhomme est vivant
  if not dead: 

    #Déplacer bonhomme veticalement
    if keyboard.w:
      jetpack.y -= 5
    if keyboard.s:
      jetpack.y += 5 

    # Limiter région de déplacement du bonhomme à la hauteur de la fenêtre
    # Condition: En enlevant de l'extrémité une certaine longueure (la hauteur de jetpack/2) pour que bohomme ne soit pas demi caché. 
    #SINON, on peut mettre une limite de <=0 et >=HEIGHT 
    if jetpack.y <= (0 + jetpack.height/2): 
      jetpack.y= (0 + jetpack.height/2)

    elif jetpack.y >= (HEIGHT - jetpack.height/2):
      jetpack.y= (HEIGHT - jetpack.height/2)

    # Code qui gère les déplacements horizotales des fusées quand position "x" de la fusée > 0
    if rocket.x>0:
      rocket.x -= speed # Déplacement horizontale de la fusée (droite vers la gauche)

    # Quand position "x" de fusée < 0
    else:
      speed += 1 # Quand déplacement est <= 0, speed augmente de 1 pixel pour le prochain update
      if speed >= 10: 
        speed = 10 # quand speed >= 10, garder une « vitesse constante » de 10 pixels par update

      score += 1 # score augmente quand une fusée sort de la gauche de l'écran x <= 0
      rocket.x = WIDTH #repositionnement de la fusée vers la droite
      rocket.y = random.randint((0 + jetpack.height/2), (HEIGHT-jetpack.height/2)) #Repositionnement au hasard de la fusée (verticalement)... 
      #La région est limitée à la fenêtre, mais en limitant davantage une longueur (la hauteur de jetpack/2) à partir de 0 et HEIGHT.

  # Si bonhomme entre en contact avec fusée, bonhomme meurt
  if jetpack.collidepoint(rocket.midleft) or jetpack.collidepoint(rocket.midtop) or jetpack.collidepoint(rocket.midbottom)  :
    dead= True
    

pgzrun.go()