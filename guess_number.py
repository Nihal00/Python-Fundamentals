import random

def guess_number_game():
    print("Welcome to the guess the number game")
    print("I have selected the number between 1 to 100 guess the number")
    min_value = int(input("Enter the minimum value: "))   
    max_value = int(input("Enter the maximum value: "))
    num_attempts = int(input("Enter the number of attempts you want to have: "))

    select_random_num = random.randint(min_value, max_value)
    attempt = 0

    # Go through while loop
    while True:
        try:
            user_guess = int(input("Write the number you guessed: "))
            attempt += 1

            if attempt > num_attempts:
                print("You have reached the limit")
                break
            elif select_random_num < user_guess:
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
