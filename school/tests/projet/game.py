#Tâche: Programme base pygame en python
#Par David Malek, maldav31@ecolecatholique.ca
#2021/01/18
import pgzrun
import random

WIDTH=500
HEIGHT=300
space= Actor("space.png")


jetpack= Actor("jetpack.png")
jetpack.pos= (50, 250)

rocket= Actor("rocket.png")

score= 0 #Score initial au commencement
rocket.speed= -1# Vitesse initiale des fusées
dead= False # Quand True, le personnage est entré en collision avec fusée

def reset_faster():
    rocket.speed += 1
    rocket.x = (WIDTH)
    rocket.y = random.randint(0, HEIGHT, rocket.height)


def draw():
  space.draw()
  screen.draw.text("Score: " + str(score), midtop = (WIDTH / 2, 5), fontsize = 30)
  if (not dead):
    jetpack.draw()
    rocket.draw()

  else:
    screen.draw.text("YOU DIED", center= (WIDTH/2, HEIGHT/2), fontsize = 50)



def update():
  global score, dead
  if keyboard.w:
    jetpack.y -= 5 
  if keyboard.s:
    jetpack.y += 5

  if (rocket.x <= 0):
    score += 1    
    rocket.x += rocket.speed

  if jetpack.colliderect(rocket):
    dead= True


pgzrun.go()