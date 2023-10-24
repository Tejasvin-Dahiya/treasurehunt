print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the treasure hunt make your choices and get awesome treasure or die trying")
print("You are in a dark cave. The path is divided into two routes")
choice1=input('Type "left" to go left or type "right" to go right.').lower()
if choice1=='left':
  print("You fell into a burning pit and died. GAME OVER")
elif choice1=='right':
  print("You are out of the tunnel ")
  print("There is a lake ahead of you.")
  choice2=input('Type "swim" to swim across or type "wait" to wait for a boat').lower()
  if choice2=='swim':
    print("Crocodiles ate you. Game over")
  elif choice2=='wait':
    print("Good choice, you crossed the river")
    print("There are three doors infront of you")
    choice3=input('Type "red" "yellow" or "blue" to choose a door').lower()
    if choice3=='red':
      print("You were bitten by a snake and died. Game over")
    elif choice3=='yellow':
      print("Congratulations you found the tresure")
    elif choice3=='blue':
      print("You fell into a pit and died. Game over")
    else:
      print("Thats not an option you idiot")
      
  else:
    print("Thats not an option dont be over smart")
    
    
  
else:
  print("Dont act smart thats not an option")


