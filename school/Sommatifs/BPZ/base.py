#Tâche: Programme interactif à la console en python
#Par David Malek, maldav31@ecolecatholique.ca
# 2021/01/15

import pgzrun

WIDTH= 700
HEIGHT= 500

#ballon basket
ball= Actor("bball.png")
ball.pos= (0, 100)
spin= 3

#Fillet basket
net= Actor("basketnet.png")
net.pos= (700,100)

#Affichage graphique 
def draw():
  screen.fill("white")
  ball.draw()
  net.draw()

#Rotation du ballon
def update():
  ball.angle += spin

#Mouvement du ballon
def on_key_down(key):
  if key== keys.w:
    ball.y -= 100
  if key== keys.d:
    ball.x += 50 
  if key== keys.s:
    ball.y += 100
  if key== keys.a:
    ball.x -= 50
  
pgzrun.go()