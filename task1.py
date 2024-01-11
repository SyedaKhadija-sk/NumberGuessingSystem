

# Hello! I'm excited to share my first task, a Number Guessing Game. 🎉

# Here's the code: let's breakdown the code


# Import the 'random' module to generate random numbers
import random
# Import the 'sys' module to exit the program
import sys


# Function to print a rule with a ✔ symbol
def print_rule(line):
    print("✔", line)

# Constants for the number of attempts in different difficulty levels
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

# Function to set the number of attempts based on the chosen difficulty level
def set_level(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        print("You have entered the wrong Difficulty Level... Set Again!\n")
        return None

# Function to check the player's answer and provide feedback
def check_answer(guessed_number, answer, attempts):
    black = "\033[30m"
    yellow = "\033[93m"
    end_format = "\033[0m"
    if guessed_number < answer:
        print(f"{black}Too low! Try again.{end_format}")
        return attempts - 1, False
    elif guessed_number > answer:
        print(f"{black}Too high! Try again.{end_format}")
        return attempts - 1, False
    else:
        print(f"{yellow}Congratulations! Your guess is right... The answer was {black}{answer}{end_format}.{end_format}")
        return 0, True  # Return 0 to indicate a correct guess

# Function to display a welcome message and explain the rules
def welcome():
    # ANSI escape codes for formatting and color
    bold = "\033[1m"
    red = "\033[91m"
    green = "\033[92m"
    orange = "\033[33m"
    purple = "\033[35m"
    white = "\033[97m"
    end_format = "\033[0m"

    print(f"{bold}{green}Number Guessing Game{end_format}\n")
    print(f"{bold}{green}Welcome to the Number Guessing Game!{end_format}")
    
    print(f"{red}I'm your Game Master.{end_format} What's your name?")
    user_name = input("Name: ")

    print(f"Hello, {red}{user_name}{end_format}! Here are the rules: \n")
    print_rule(f"\t{orange}I will think of a random number between 1 and 100.{end_format}")
    print_rule(f"\t{orange}You have to guess the number within 10 attempts.{end_format}")
    print_rule(f"\t{orange}I will provide feedback after each guess, letting you know if it's too high or too low.\n{end_format}")
    print(f"{purple}Let's get started!{end_format}")

    while True:
        level = input(f"{green}Choose Level Of Difficulty...Type{end_format} {white}'Easy'{end_format} or {white}'Hard'{end_format}{green}:{end_format} ")
        attempts = set_level(level)
        if attempts is not None:
            break   
    
    return random.randint(1, 100), attempts

# Function to handle the main game loop
def play_game(answer, attempts):
    blue = "\033[94m"
    yellow = "\033[93m"
    end_format = "\033[0m"
    guessed_number = 0
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number.")
        guessed_number = int(input(f"{blue}Guess a number:  {end_format}"))

        attempts, correct_guess = check_answer(guessed_number, answer, attempts)

        if correct_guess:
            return

        if attempts == 0:
            print(f"{yellow}You are out of guesses...You lose!...  The answer was {blue}{answer}{end_format}{end_format}")
            return

# Main function to initiate the game
def main():
    answer, attempts = welcome()

    while True:
        play_game(answer, attempts)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            sys.exit()
            
# Run the main function if the script is executed
if __name__ == "__main__":
    main()





# Happy coding! 
# Bye-bye! 
# See you on my next task.!🚀😊


