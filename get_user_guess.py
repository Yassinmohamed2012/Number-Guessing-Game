def get_user_guess():
    while True:
        try:
            guess= int(input("enter your guess from (1-100)"))
            if guess >=1 and guess<=100:
                return guess

            else:
                print("please enter a number between 1 and 100 ")
        except ValueError:
            print("invalid input!!! please enter a valid no. ")
get_user_guess()
