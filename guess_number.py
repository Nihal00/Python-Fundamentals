import random

def guess_number_game():
    print("Welcome to the guess the number game")
    print("I have selected the number between 1 to 100 guess the number")

    select_random_num = random.randint(1, 100)
    attempt = 0

    # Go through while loop
    while True:
        try:
            user_guess = int(input("Write the number you guessed: "))
            attempt += 1

            if select_random_num < user_guess:
                print("You are higher to the guess number")
            elif select_random_num > user_guess:
                print("You are lower to the guess number")
            else:
                print("Congratulation you have guessed the correct number")
                print("this is the number to attempts you tried", attempt)
                break
        except ValueError:
            print("You can only select number")




if __name__ == "__main__":
    guess_number_game()
