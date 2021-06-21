from tkinter import *
import random

root = Tk()
root.geometry("700x700")
root.title("Welcome To Ithuba Lotto")
root.config(bg="#FFC107")


number = random.randint(1, 100)
tries = 0

name = input("What's your Name? ")
name = name.strip()

print("Hello " + name + ", I'm looking for a friend.")
print("Would you like to play a game with me?")
print("1) Yes I would!")
print("2) No I'm boring")

option = input("Are we going to be friends? ")
option = int(option)

if option != 1 or 2:
    pass

if option == 1:
    print("Wow you're already amazing, thank you for saying yes")
    print("I'm thinking of a number between 1 and 100")
    print("You have 5 guesses")
    print("Let The Guessing Begin!")

    guess = input("Your first guess: ")
    guess = int(guess)
    tries += 1

    if guess > number:
        print("I can't count that far, go lower")
    if guess < number:
        print("I can count a bit more than that, go higher")

    while guess != number and tries < 5:
        guess = input("You can go again: ")
        guess = int(guess)
        tries += 1

        if guess > number:
            print("Just a bit lower my friend")
        if guess < number:
            print("Just a bit higher my friend")

    if guess == number:
        print("WELL DONE my friend!!!")
        print("You only tried: " + str(tries) + " times and completed the challenge")
        print("THANKS FOR PLAYING WITH ME")

    else:
        print("I'm sorry my friend")
        print("The number was " + str(number))
        print("You ran out of guesses")
        print("GAME OVER")


elif option == 2:
    print("Thanks for speaking to me " + name + " have a good day!")

else:
    print("You were just supposed to say yes or no " + name)
    print("It's simple, 1 is yes,be my friend."
          " 2 is no, I have enough friends")

# c = MiniGameScreen(root)
root.mainloop()
