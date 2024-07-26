import random
import turtle
import time
import tortoise
from words import wordslist
while True:
  ans = ""
  anslist = []
  garg = 1
  
  turtle.Screen().bgcolor("grey")
  tortoise.screen.listen()
  word = wordslist[random.randint(0,len(wordslist) - 1)]
  for char in word:
    index = ord(char)
    anslist = []
    bin = format(index,'b')
    charnum = 2
    for char in bin:
      if charnum == 6:
        if char == "1":
          tortoise.draw_lettering("yellow","C",-50)
        elif char == "0":
          tortoise.draw_lettering("black","C",-50)
        charnum = charnum + 1
      elif charnum == 5:
        if char == "1":
          tortoise.draw_lettering("yellow","O",-25)
        elif char == "0":
          tortoise.draw_lettering("black","O",-25)
        charnum = charnum + 1
      elif charnum == 4:
        if char == "1":
          tortoise.draw_lettering("yellow","D",0)
        elif char == "0":
          tortoise.draw_lettering("black","D",0)
        charnum = charnum + 1
      elif charnum == 3:
        if char == "1":
          tortoise.draw_lettering("yellow","E",25)
        elif char == "0":
          tortoise.draw_lettering("black" ,"E",25)
        charnum = charnum + 1
      elif charnum == 2:
        if char == "1":
          tortoise.draw_lettering("yellow","S",50)
        elif char == "0":
          tortoise.draw_lettering("black","S",50)
        charnum = charnum + 1
    time.sleep(5)
    tortoise.screen.update()
  anslist.append(input(" answer: "))
  for i in anslist:
    ans = ans + i
  if ans == word:
    print("correct")
    break
  else:
    print("incorrect",word)
    break
    #abcdefghijklmnopqrstuvwxyz
