import pgzrun

WIDTH= 800
HEIGHT= 400

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