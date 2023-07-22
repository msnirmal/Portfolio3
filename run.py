import os
import time

questions = {
 "What do elephants use their trunk for?: ": "D",
 "What element does the chemical symbol Au stand for?: ": "D",
 "What is the most visited tourist attraction in the world?: ": "A",
 "What is the only food that cannot go bad?: ": "D",
 "Who invented the gramophone?: ": "B"
 }

options = [["A. Smell", "B. Carry food", "C. Communication", 
            "D. All of the above"],
           ["A. Silver", "B. Magnesium", "C. Salt", "D. Gold"],
           ["A. Eiffel Tower", "B. Statue of Liberty",  
            "C. Great Wall of China", "D. Colosseum"],
           ["A. Dark chocolate", "B. Peanut butter", "C. Canned tuna", 
            "D. Honey"],
           ["A. Thomas Edison", "B. Emile Berliner", "C. Albert Einstein", 
            "D. Isaac Newton"],
           ]


def clear():
    if os.name == 'nt':
        os.system('cls')     
    else:
        os.system('clear')


print("GENERAL KNOWLEDGE QUIZ")
print("\n")
time.sleep(1)
player_name = input("Enter your name or press 'enter' key:\n").capitalize()
time.sleep(1)
clear()
print(f"Welcome {player_name}, lets play :-)")
time.sleep(3)
print("\n")
print("Here are your questions, wish you all the best....")
time.sleep(3)
clear()


def initiate_game():

    guesses = []
    correct_guesses = 0
    question_num = 1 

    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D):\n")
        guess = guess.upper()       
        guesses.append(guess)       
        correct_guesses += check_answer(questions.get(key), guess)
        time.sleep(2)
        clear()
        question_num += 1
    show_score(correct_guesses, guesses)


def check_answer(answer, guess):  

    if answer == guess:
        print("\n")
        print("Yayy that's CORRECT!")
        return 1         
    else:
        print("\n")
        print("Oops that's INCORRECT!")
        return 0         


def show_score(correct_guesses, guesses):
    print("********************************************************")
    print("See below your guesses against correct answers and score")
    print("********************************************************")

    print("Correct Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Your Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("You have scored: "+str(score)+"%")


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        time.sleep(2)
        clear()
        return True
    else:
        return False


initiate_game()    

while play_again():
    initiate_game()

print("Thank you for playing the quiz game")
quit()
