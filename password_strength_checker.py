import re
import string

def check_password_strength():
    print("Welcome the check you word strength app")
    password = input("Please Enter your password without: ")
    score = 0

    while True:
        # check if password as space
        if check_as_space(password):
            print("Password cannot have space in it try again: ")
            password = input("Please Enter your password without: ")
        else:
            break 

    # check password length
    if password_length(password):
        score += 1

    # check password lowercase
    if lower_case_check(password):
        score += 1

    # check password uppercase
    if upper_case_check(password):
        score += 1
    
    # check password as number
    if number_check(password):
        score += 1

    # check password special char
    if special_char_check(password):
        score += 1
    

    print("Your score is: ", score)


def check_as_space(password):
    return any(ch in string.whitespace for ch in password)

def password_length(password):
   return len(password) >= 8

def lower_case_check(password):
   return any(letter.islower() for letter in password)

def upper_case_check(password):
   return re.search("[A-Z]", password)

def number_check(password):
    return re.search("[1-9]", password)

def special_char_check(password):
    return re.search("[^a-zA-Z0-9_]", password)


if __name__ == "__main__":
    check_password_strength()