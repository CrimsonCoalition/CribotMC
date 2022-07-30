import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

#foodEatTiming = 0
print("Now. Switch To your Minecraft Window and unpause The Game.")

time.sleep(1)
print("Starting Bot in...")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")



def ai():
  foodEatTiming = 0
  
  while foodEatTiming < 30:
    keyboard.press('w')
    time.sleep(.6)
    mouse.press(Button.left)
    mouse.release(Button.left)
    foodEatTiming += 1
  eatFood()


    


  

def eatFood():
  #while True:
  keyboard.release('w')
  keyboard.press('s')
  keyboard.press('2')
  keyboard.release('2')
  mouse.press(Button.right)
  time.sleep(4)
  mouse.release(Button.right)
  keyboard.press('1')
  keyboard.release('1')
  keyboard.release('s')
  foodCoolDown = 0
  ai()


ai()
