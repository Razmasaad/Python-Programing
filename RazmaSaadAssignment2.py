import random
highest_value = 10
lowest_value = 1
print("I am gonna guess your number from {} to {}".format(lowest_value, highest_value))
input("Press enter to get me started")
guesses = 1
while True :
    print("\t guessing in the range of {} to {}".format(lowest_value, highest_value))
    guess = lowest_value+(highest_value-lowest_value)//2
    hilo = input("My guess is {}.tell me should I go higher,lower or it is correct".format(guess).casefold())
    if hilo == "higher":
        lowest_value = guess+1
    elif hilo == "lower":
        highest_value = guess-1
    elif hilo == "correct":
        print("I got the number in {} guesses!".format(guesses))
        break
    else:
        print("Please enter higher,lower or correct")
    guesses = guesses+1
print("")
#Medium Game
highest_value = 100
lowest_value = 1
print("I am gonna guess your number from {} to {}".format(lowest_value, highest_value))
input("Press enter to get me started")
guesses = 1
while True :
    print("\t guessing in the range of {} to {}".format(lowest_value, highest_value))
    guess = lowest_value+(highest_value-lowest_value)//2
    hilo = input("My guess is {}.tell me should I go higher,lower or it is correct".format(guess).casefold())
    if hilo == "higher":
        lowest_value = guess+1
    elif hilo == "lower":
        highest_value = guess-1
    elif hilo == "correct":
        print("I got the number in {} guesses!".format(guesses))
        break
    else:
        print("Please enter higher,lower or correct")
    guesses = guesses+1
print("")
#Hard game
highest_value = 500
lowest_value = 1
print("I am gonna guess your number from {} to {}".format(lowest_value, highest_value))
input("Press enter to get me started")
guesses = 1
while True :
    print("\t guessing in the range of {} to {}".format(lowest_value, highest_value))
    guess = lowest_value+(highest_value-lowest_value)//2
    hilo = input("My guess is {}.tell me should I go higher,lower or it is correct".format(guess).casefold())
    if hilo == "higher":
        lowest_value = guess+1
    elif hilo == "lower":
        highest_value = guess-1
    elif hilo == "correct":
        print("I got the number in {} guesses!".format(guesses))
        break
    else:
        print("Please enter higher,lower or correct")
    guesses = guesses+1
print("")
#Legendary Game
highest_value = 1000
lowest_value = 1
print("I am gonna guess your number from {} to {}".format(lowest_value, highest_value))
input("Press enter to get me started")
guesses = 1

while True :
    print("\t guessing in the range of {} to {}".format(lowest_value, highest_value))
    guess = lowest_value+(highest_value-lowest_value)//2
    hilo = input("My guess is {}.tell me should I go higher,lower or it is correct".format(guess).casefold())
    if hilo == "higher":
        lowest_value = guess+1
    elif hilo == "lower":
        highest_value = guess-1
    elif hilo == "correct":
        print("I got the number in {} guesses!".format(guesses))
        break

    else:
        print("Please enter higher,lower or correct")
    guesses = guesses+1








