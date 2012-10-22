from sys import exit

def room_one():
  print "You're now in the welcome center main lobby."
  print "There is a swarm of zombies about to enter the other door."
  print "1 - Run to the gift shop"
  print "2 - Go back to camp"
  print "3 - Run for the gun over the boar's head"
  
  answer = raw_input("> ")
  
  if answer == "2" or answer == "3":
    dead("You are zombie lunch!")
  elif answer == "1":
    room_two()
  else:
    dead("Learn to pick an option!")
    exit()
    
def room_two():
  print "The gift shop is full of great hiding places"
  print "Where do you hide?"
  print "1 - The refidgerator"
  print "2 - Behind the register counter"
  
  answer = raw_input("> ")
  
  if answer == "1":
    print "Yeah! you win!  Stay the night in the fidge, oh, but make sure to unplug it first...brrrr"
  else:
    dead("You did not survive the apocolypse")  

def dead(why):
  print why
  exit()

def start():
  print "Welcome the Zombie Land!"
  print "You are in the woods camping when you here the sounds of"
  print "The undead.  You begin running back to the lodge and see"
  print "a herd coming upon the Welcome center."
  print "What do you do?"
  print "1 - Run into the welcome center and grab a gun."
  print "2 - Run back to camp"
  
  answer = raw_input("> ")
  
  if answer == "2":
    dead("Before you get to camp you are eatin!!!")
  elif answer == "1":
    room_one()
  else:
    dead("Learn to pick one of the options!")

start()
