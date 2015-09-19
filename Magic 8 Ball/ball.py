import random
import time

responses = ["Almost definitely!", "Yeah, good luck with that...", "Definitely not.", "YES, IT'S CERTAIN!",
             "No chance.", "There's a strong possibility!", "I'm not too sure.", "I doubt that.", "Nope, move along.",
             "I really don't think so.", "Nope.", "Yeah!", "No, just no.", "I don't think so.", "I'm just a ball, what do you want from me?",
             "You're asking a ball a question, sound logical?", "How am I supposed to know?", "It's 99.9% certain!", "N.O.P.E.", "IT'S 100% CERTAIN!"]

def ballInput():
        question = 'What do you need to know, stranger?'
        print(question)
        things = input("QUESTION: ")
 
        print("\nThinking..\n")
        time.sleep(random.randint(1,4))
        print(random.choice(responses), "\n")
        time.sleep(2)
        quitOrAsk()

def quitOrAsk():
        print("Do you want to:")
        print("[1] Quit")
        print("[2] Ask another question")
        response = input("> ")

        if (response == "1"):
            quit()
        elif (response == "2"):
            ballInput()
        else:
            print("Sorry, I don't think that option exists.")

ballInput()

        
