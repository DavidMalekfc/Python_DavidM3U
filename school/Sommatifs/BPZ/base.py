#Tâche: Programme base pygame en python
#Par David Malek, maldav31@ecolecatholique.ca
#2021/01/18
import pgzrun

WIDTH= 400
HEIGHT= 300
keep_play= True

#Les instructions pour marquer un but
instructions=("Marquer un but en utilisant les clés \n W,A,S,D pour déplacer le ballon \n aux environs du fillet.")

#Sprite ballon basket
ball= Actor("b-ball.png")
ball.pos= (20,275)
spin= 3

#Sprite fillet basket
net= Actor("basketnet.png")
net.pos= (375,100)


# Déplacement du ballon
def on_key_down(key):
  if keyboard.w:
    ball.y -= 15
  elif keyboard.d:
    ball.x += 15 
  elif keyboard.s:
    ball.y += 15
  elif keyboard.a:
    ball.x -= 15

#Affichage graphique 
def draw():
  if keep_play:
    screen.fill("white")
    ball.draw()
    net.draw()
    screen.draw.text(instructions, (0,0), color="black", fontsize=23)
  else: 
    screen.fill("green")
    screen.draw.text("BUT!!! Faire Run pour recommencer", center = (WIDTH / 2,HEIGHT / 2), fontsize = 30)  

#Rotation du ballon
def update():
  global keep_play
  ball.angle -= spin
  """
  if keyboard.w:
    ball.y -= 10
  elif keyboard.d:
    ball.x += 10 
  elif keyboard.s:
    ball.y += 10
  elif keyboard.a:
    ball.x -= 10
  """
  if (ball.colliderect(net)):
    keep_play=False

pgzrun.go()