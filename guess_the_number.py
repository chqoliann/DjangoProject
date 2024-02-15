import random


def welcome():
    print("\033[94mhi!\033[0m")


def get_user_name():
    name = input("\033[92mEnter your name:\033[0m")
    print(f"\033[94m welcome to game 'guess the number!'{name}\033[0m")


def generator_random_number():
    return random.randint(1, 10)


def guess_the_number():
    number_to_guess = generator_random_number()
    attempts = 0
    max_attempts = 5
    print("\033[91m I thought of a number from 1 to 10. Try to guess!\033[0m")

    while attempts < max_attempts:
        user_guess = int(input("\033[92m enter your variant:\033[0m"))
        attempts += 1

        if user_guess <= 10:
            if user_guess == number_to_guess:
                print("\033[94m you are guess!Congratulations!\033[0m")
                break
            else:
                print("\033[94m try again!\033[0m")
        else:
            print("\033[91m your number biggest! please enter number in range 1-10\033[0m")

    if attempts == max_attempts:
        print(f"\033[94m Unfortunately, you have exhausted all {max_attempts} attempts. The hidden number was {number_to_guess}\033[0m")


def play_again():
    while True:
        answer = input("\033[92m Do you want to play again? (yes/no):\033[0m")
        if answer == "yes":
            guess_the_number()
        elif answer == "no":
            print("\033[91mThanks for playing! Goodbye.\033[0m")
            break
        elif answer != "yes" or "no":
            print("\033[91m please enter yes or no\033[0m")


def main():
    welcome()
    get_user_name()
    guess_the_number()
    play_again()


if __name__ == "__main__":
    main()
