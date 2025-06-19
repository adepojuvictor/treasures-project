#i created a treasure island

print("welcome to treasure island")
print("your mission is to find the treasure")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right" ')

if choice1 == "left":
    choice2 = input('you have come to a lake. there is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across :')

    if choice2 == "wait":
        #third choice
     choice3 = input('You arrive at the island unharmed. There is a house with 3 doors : red, yellow, and blue. Which color do you choose? ')
     if choice3 == "yellow" :
       print("you found the treasure ! You win!")
     elif choice3 == "red":
       print("you were burned by fire. Game over")
     elif choice3 == "blue":
       print("you were eaten by beasts. Game over")
     else :
       print("Game over ! Invalid choice.")
    else:
     print("you were attacked by a trout. Game over !")
else:
  print("you fell into a hole. Game over.")