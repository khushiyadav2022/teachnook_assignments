# -*- coding: utf-8 -*-
"""minor_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g4fO384ahQvabZ-j8U5MxGkoQX-mrD77
"""

# Python Minor Project
# Create A Countdown Timer Using Python

# Features To Include
# Reset/ Stop
# Pause /Resume

import time

def start(t):
  # t = int(input("Set COUNTDOWN's time in seconds: "))
  while t:
    mins, secs=divmod(t,60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer)
    time.sleep(1)
    t -= 1
  print('your time is ended up')

def pause():
  pause_time=int(input("how much time you want to pause: "))
  time.sleep(pause_time)
  print("pause time over....Now COUNTDOWN start")
  start(t)

def stop():
  print("wait...")
  time.sleep(5)
  print("\n oppss...it's not working...please start the timer ")
  

def reset(t1):  
  while t1:
    t1=int(input("In how much time you want to reset: "))
    mins, secs=divmod(t,60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print("within", t1," sec it will start...please wait")
    time.sleep(t1)    
    start(t)
    break

print("Select operation.")
print("start")
print("pause")
print("stop")
print("reset")

while True:
    choice = input("Enter choice(start/pause/stop/reset): ")
    if choice in ('start', 'pause', 'stop', 'reset'):
      t = int(input("Set COUNTDOWN's time in seconds: "))
      
      if choice == 'start':
        start(t)
        

      elif choice == 'pause':
        pause()

      elif choice == 'stop':
        stop()

      elif choice == 'reset':
        reset(t)

      aim = input("you want to exit? (yes/no): ")
      if aim == "yes":
        break
      elif aim=="no":
        pass
      else:
        print("please choose 'YES' or 'NO' only")
    
    else:
        print("Invalid Input")





