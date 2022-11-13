# import requirements for this program
import json
import time


CATEGORIES_LIST = ['movies', 'music', 'sport', 'television']

def ask_one_question(question):
    """
    Function to answering the queations, in lower OR upper case.
    """
    print("\n" + question)
    choice = input("Enter Your Choice [a/b/c/d]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Choose again")
            choice = input("Enter Choice [a/b/c/d]: ")      

def score_one_result(key, meta):
    """
    This will display the users response 
    in the correct or wrong answer.
    """

    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        print("Q.{0} Correct!\n".format(key))
        return 1
    else:
        print("Q.{0} Incorrect!".format(key))
        print("Correct Answer is ({0})".format(actual))
        return -1

def test(questions):
    """
    This will display a how the quiz works and score for each correct and wrong answer.
    """
    score = 0
    print("Instructions:\n1. Please enter only the choice letter to the correct answer.\n2. Each question carries 1 point\n3. Wrong answer, takes 1 point off.\nQuiz will start momentarily......... GOOD LUCK!\n")
    time.sleep(10)
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])

    print("\n-------------- RESULT ----------------\n")
    for key, meta in questions.items():
        score += score_one_result(key, meta)
    print("Your Score:", score, "/", 1 * len(questions))

def load_question(filename):
    """
    loads the questions from the JSON file into a Python dictionary and returns it
    """
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return questions


def play_quiz():

    """
    List of categories to choose from.
    """
    flag = False
    try:
        choice = int(input("Welcome to Today's Entertainment Quiz!\nChoose your Entertainment of interest:\n(1). Movies\n(2). Music\n(3). Sport\n(4). Television\nEnter Your Choice [1/2/3/4]: "))
        if choice > len(CATEGORIES_LIST) or choice < 1:
            print("Invalid Choice. Enter Again")
            flag = True
    except ValueError as e:
        print("Invalid Choice. Enter Again")
        flag = True

    if not flag:
        questions = load_question('categories/'+CATEGORIES_LIST[choice-1]+'.json')
        test(questions)
    else:
        play_quiz()

def user_begin_prompt():

    """
    Introduction function on testing your Entertainment Knowledge
    """
    print("Hi.... Want to test your Entertainment knowledge?\nA. Yes\nB. No")
    play = input()
    if play.lower() == 'a' or play.lower() ==  'y':
        play_quiz()
    elif play.lower() == 'b':
        print("Hope you come back soon!")
    else:
        print("I didn't quite understand that.\nPress A to play, or B to quit.")
        user_begin_prompt()

def execute():
    user_begin_prompt()

if __name__ == '__main__':
    execute()
