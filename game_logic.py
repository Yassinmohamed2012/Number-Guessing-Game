from random_no_generator import generate_random_number
from get_user_guess import get_user_guess

def play_game():
    print("welcome to the number guessing game ")
    random_number=generate_random_number()
    attemps=0
    while True:
        guess=get_user_guess()
        attemps += 1
        if guess < random_number:
            print("too low...")
        elif guess > random_number:
            print("too high...")
        else:
            print(f"congratulations you guessed the no. in {attemps} attemps")
            break

play_game()