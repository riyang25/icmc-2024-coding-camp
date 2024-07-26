import turtle
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
def draw_lettering(color,letter,x):
  pen.goto(x,0)
  pen.pendown()
  pen.color(color)
  pen.write(letter,move = False, align = 'center',font=("Arial",30,"normal"))
def start():
  return True
def somthing(arg):
  global garg
  garg = arg
def typing():
  for c in "qwertyuopasdfghjklzxcvbnm":
    screen.onkey(lambda: somthing(c),c)
    if screen.onkey(lambda: somthing(c),c):
      return True
