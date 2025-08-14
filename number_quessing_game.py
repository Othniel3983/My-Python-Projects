import random as ran

def easy():
    print("\nLEVEL : EASY")
    
    secretNumber = ran.randint(1, 50)
    attempts = 0

    while True:
        guess=input("\nGuess a number between 1 and 50: ")

        if not guess.isdigit():
            print("Invalid number! Please quess the number again")
            continue

        guess=int(guess)
        if guess > 50:
            print("Invalid input! Number not in range.")
            continue

        attempts +=1
        if attempts == 3:
            print("\nGame Over! You have exusted your attempts, the secret number is %d" %secretNumber)
            break

        if guess < secretNumber:
            print("Too low! Try again")
        elif guess > secretNumber:
            print("Too high!Try again")
        else:
            print("Congratulations! You guessed the number in %d attempts." %attempts)
            break

def difficult():
    print("\nLEVEL : DIFFICULT")
    
    secretNumber = ran.randint(1, 100)
    attempts = 0

    while True:
        guess=input("\nGuess a number between 1 and 100: ")

        if not guess.isdigit():
            print("Invalid number! Please quess the number again")
            continue

        guess=int(guess)
        if guess > 100:
            print("Invalid input! Number not in range.")
            continue

        attempts +=1
        if attempts == 5:
            print("\nGame Over! You have exusted your attempts, the secret number is %d" %secretNumber)
            break

        if guess < secretNumber:
            print("Too low! Try again")
        elif guess > secretNumber:
            print("Too high!Try again")
        else:
            print("Congratulations! You guessed the number in %d attempts." %attempts)
            break


def start():
    print("Welcome to YAYA KK's Number Quessing Game")
    print("Choose Level: \n" \
    "1. Easy \n" \
    "2. Difficult")

    level=input("> ")
    if level == '1':
        easy()

    elif level == '2':
        difficult()

    else:
        print("Invalid input!")
        start()

start()


