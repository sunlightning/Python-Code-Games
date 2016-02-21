#This is a "Guess the Number" game.
#The player wins if he/she guess it right within 6 tries.

#library import
import random

#player
playerHP = 120
print("What's your name, Chosen Guesser?")
playerName = input()
print("HP: " + str(playerHP))

#Iron Knight Puter
randomNumber = random.randint(1, 30)
swordDamage = 20

#Dialogue
print("======================================================================")
print("Nice to meet you, " + playerName + ". I'm Iron Knight Puter.")
print("======================================================================")
nextDialog = input()
print("I'll think of a random number and you must guess it.")
print("======================================================================")
nextDialog = input()
print("After each try, if you guess it wrong, I'll hit you with my sword.")
print("======================================================================")
nextDialog = input()
print("If you guess it right, I'll commit suicide and you can enter the castle.")
print("======================================================================")
nextDialog = input()
print("Get ready!")
print("======================================================================")
nextDialog = input()
print("I'm thinking of a number between 1 and 30. Good luck, faggot! MUHAHAH!")

#Game
while playerHP > 0:
    print("======================================================================")
    print("Take a guess now!")
    playerGuess = input("Your guess:")
    playerGuess = int(playerGuess)
    print("======================================================================")

    if playerGuess > randomNumber:
        print("Your guess's too high! HAHAH!")
        playerHP -= swordDamage
        print("You've taken damage! -20 HP")
        print("HP: " + str(playerHP))

    elif playerGuess < randomNumber:
        print("Your guess's too low! HAHAH!")
        playerHP -= swordDamage
        print("You've taken damage! -20 HP")
        print("HP: " + str(playerHP))

    else:
        print("I don't believe it... You won!... *dies*")
        print("VICTORY")
        break

    if playerHP == 0:
        print("MUHAHAHAH! #REKT #FAGGOT #GITGUD")
        print("I was thinking of " + str(randomNumber))
        print("YOU DIED")
        break
