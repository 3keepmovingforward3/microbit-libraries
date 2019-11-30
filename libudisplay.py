# Write your code here :-)
from microbit import *

def turnUp(xx,yy):
    for x in range(0,9,1):
        display.set_pixel(xx,yy,x)
        sleep(180)

def turnDown(xx,yy):
    for x in range(9,-1,-1):
        display.set_pixel(xx,yy,x)
        sleep(180)

turnUp(2,3)
turnDown(2,3)
# while 1:
  #  display.clear()

  #  display.set_pixel(2,3,8)
  #  sleep(180)
  #  display.clear()

  #  display.set_pixel(3,2,8)
   # display.set_pixel(2,2,8)
   # display.set_pixel(1,2,8)
  #
    #display.set_pixel(3,4,8)
    #display.set_pixel(2,4,8)
    #display.set_pixel(1,4,8)

    #display.set_pixel(3,3,8)
    #display.set_pixel(1,3,8)
    #sleep(180)
    #display.clear()
