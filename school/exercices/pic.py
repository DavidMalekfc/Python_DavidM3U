import pgzrun

WIDTH= 2000
HEIGHT= 800

ball= Actor("ball.png")
ball.pos= (WIDTH, HEIGHT/2)
speed= 1

def draw():
  screen.fill("white")
  ball.draw()

def update():
  ball.x= ball.x - speed
  ball.y= ball.y + speed

pgzrun.go()