questions = {
 "What do elephants use their trunk for?: ": "D",
 "What element does the chemical symbol Au stand for?: ": "D",
 "What is the most visited tourist attraction in the world?: ": "A",
 "What is the only food that cannot go bad?: ": "D",
 "Who invented the gramophone?: ": "B",
 "What is the world’s smallest bird?: ": "D",
 "What is the capital city of India?: ": "B",
 "Who founded Amazon?: ": "C",
 "What animal features in the logo for the World Wildlife Fund?: ": "D",
 "What is the national bird of India?: ": "C"
}

options = [["A. Smell", "B. Carry food", "C. Communication", "D. All of the above"],
          ["A. Silver", "B. Magnesium", "C. Salt", "D. Gold"],
          ["A. Eiffel Tower", "B. Statue of Liberty", "C. Great Wall of China", "D. Colosseum"],
          ["A. Dark chocolate","B. Peanut butter", "C. Canned tuna", "D. Honey"],
          ["A. Thomas Edison","B. Emile Berliner", "C. Albert Einstein", "D. Isaac Newton"],
          ["A. Peacock","B. Pigeon", "C. Bee Hummingbird", "D. Eagle"],
          ["A. Bangalore","B. Delhi", "C. Chennai", "D. Kerala"],
          ["A. Elon Musk","B. Richard Branson", "C. Jeff Bezos", "D. Narayan Murthy"],
          ["A. Elephant","B. Tiger", "C. Lion", "D. Panda"],
          ["A. Elephant","B. Tiger", "C. Lion", "D. Panda"],
          ["A. Eagle","B. Pigeon", "C. Peacock", "D. Rooster"]]

def start_game():

    guesses= []
    score = 0
    question_index = 0

    for key in questions:
        print()
        print(key)
        for i in options[question_index]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        score += check_answer(questions.get(key), guess)
        question_index += 1    
    show_score(score, guesses)


def check_answer():

    if answer == guess:
        print ('CORRECT')
        return 1
    else:
        print ('INCORRECT')
        return 0


def show_score(score, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end = "")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():
    pass
start_game()
 



