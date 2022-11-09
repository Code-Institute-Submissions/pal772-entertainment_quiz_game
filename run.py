import json
import time

CATEGORIES_LIST = ['movies', 'music', 'sport', 'television'] 

def ask_one_question(question):
    print("\n" + question)
    choice = input("Enter Your Choice [a/b/c/d]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Choose again")
            choice = input("Enter Choice [a/b/c/d]: ")