import os

questions = {
 "What do elephants use their trunk for?: ": "D",
 "What element does the chemical symbol Au stand for?: ": "D",
 "What is the most visited tourist attraction in the world?: ": "A",
 "What is the only food that cannot go bad?: ": "D",
 "Who invented the gramophone?: ": "B"
 }

options = [["A. Smell", "B. Carry food", "C. Communication", "D. All of the above"],
          ["A. Silver", "B. Magnesium", "C. Salt", "D. Gold"],
          ["A. Eiffel Tower", "B. Statue of Liberty", "C. Great Wall of China", "D. Colosseum"],
          ["A. Dark chocolate","B. Peanut butter", "C. Canned tuna", "D. Honey"],
          ["A. Thomas Edison","B. Emile Berliner", "C. Albert Einstein", "D. Isaac Newton"],
          ]

player_name = input ("Please enter your name: \n")
print("\n")
print(f"Welcome {player_name}!! lets play the quiz")
print("\n")
os.system('cls' if os.name == 'nt' else 'clear')
print ("Here are your questions, wish you all the best")


def start_game():

    guesses= []
    correct_guesses = 0
    question_index = 1

    for key in questions:
        print()
        print(key)
        for i in options[question_index-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_index += 1    
    show_score(correct_guesses, guesses)
     

def check_answer(answer, guess):

    if answer == guess:
        print ("CORRECT")
        return 1
    else:
        print ("INCORRECT")
        return 0

def show_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end= "")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end = "")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "Yes":
        return True
    else:
        return False
    
start_game()

while play_again():
    start_game()

 


 
 



