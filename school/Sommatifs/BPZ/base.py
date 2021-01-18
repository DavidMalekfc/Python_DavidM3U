#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
#2021/01/15
import pgzrun

WIDTH= 400
HEIGHT= 300
keep_play= True

#Les instructions pour marquer un but
instructions=("Marquer un but en utilisant les clés \n W,A,S,D pour déplacer le ballon.")

#Sprite ballon basket
ball= Actor("b-ball.png")
ball.pos= (20,275)
spin= 3

#Sprite fillet basket
net= Actor("basketnet.png")
net.pos= (375,100)

#Affichage graphique 
def draw():
  screen.fill("white")
  ball.draw()
  net.draw()
  screen.draw.text(instructions, (0,0), color="black", fontsize=23)

#Rotation du ballon et marquer un but
def update():
  ball.angle -= spin
  if (ball.colliderect(net)):
    keep_play= False

#Mouvement du ballon
def on_key_down(key):
  if key== keys.W:
    ball.y -= 10
  elif key== keys.D:
    ball.x += 10 
  elif key== keys.S:
    ball.y += 10
  elif key== keys.A:
    ball.x -= 10

""" #option à essayer (je viens de l'écrire)
while keep_play:
  draw()
  update()
  on_key_down(key)
  if (ball.colliderect(net)):
    keep_play= False
"""
pgzrun.go()