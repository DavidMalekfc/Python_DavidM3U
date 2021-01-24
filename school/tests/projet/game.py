#Tâche: Programme pour projet pgzero en python
#Par David Malek, maldav31@ecolecatholique.ca
#2021/01/26
import pgzrun
import random

WIDTH=500
HEIGHT=300
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

print(jetpack.height, jetpack.width)
print(rocket.height, rocket.width)

def draw():
  space.draw()
  screen.draw.text("Score: " + str(score), midtop = (WIDTH / 2, 5), fontsize = 30)
  if dead:
    jetpack.draw()
    rocket.draw()
  else:
    screen.draw.text("YOU DIED", center= (WIDTH/2, HEIGHT/2), fontsize = 50)


def update():
  global speed, score, dead
  #Controller bonhomme veticalement
  if keyboard.w:
    jetpack.y -= 5
  if keyboard.s:
    jetpack.y += 5 
  # Limiter la région de déplacement verticale du bonhomme
  """if jetpack.y < 0 or jetpack.y > HEIGHT:
    jetpack.y == 0, HEIGHT"""


  if (rocket.x>0):
    rocket.x -= speed # Déplacement horizontale de la fusée
  
  else:
    speed += 1 # Quand déplacement est <= 0, speed augmente de 1 pixel pour le prochain update
    if speed >= 15: 
      speed = 13 # quand speed >= 15, garder une « vitesse constante » de 13 pixels par update
      # augmenter « vitesse de déplacement » du bonhomme
      if keyboard.w:
        jetpack.y -= 10
      if keyboard.s:
        jetpack.y += 10
    
    score += 1 # score augmente quand une fusée sort de la gauche de l'écran
    rocket.x = WIDTH #repositionnement de la fusée vers la droite
    rocket.y = random.randint(0, HEIGHT) #Repositionnement au hasard de la fusée (verticalement)

  # Si bonhomme entre en contact avec fusée, bonhomme meurt
  if (jetpack.colliderect(rocket)):
    dead= True
    


pgzrun.go()