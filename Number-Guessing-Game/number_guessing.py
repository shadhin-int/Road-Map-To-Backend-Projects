import random
import time


def print_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number within the allowed chances.")


def select_difficulty():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        return 10
    elif choice == 2:
        return 5
    elif choice == 3:
        return 3
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        return 5


def play_game():
    print_welcome_message()
    attempts = select_difficulty()
    number_to_guess = random.randint(1, 100)
    attempts_taken = 0

    start_time = time.time()

    while attempts > 0:
        user_guess = int(input("\n Enter your guess: "))
        attempts_taken += 1
        attempts -= 1

        if user_guess == number_to_guess:
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Congratulations! You guessed the correct number in {attempts_taken} attempts.")
            print(f"It took you {round(time_taken, 2)} seconds to guess the number.")
            return attempts_taken

        elif user_guess > number_to_guess:
            print(f"Incorrect! The number is less than {user_guess}.")

        else:
            print(f"Incorrect! The number is greater than {user_guess}.")

    print(f"\nSorry, you've run out of chances! The correct number was {number_to_guess}.")
    return None


def main():
    high_score = None
    
    while True:
        attempts_taken = play_game()

        if attempts_taken:
            if not high_score or attempts_taken < high_score:
                high_score = attempts_taken
                print(f"New high score! You guessed the number in {high_score} attempts.")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing the Number Guessing Game!")

    
if __name__ == '__main__':
    main()
