import random
choices = ['rock', 'paper', 'scissors']
play = 'yes'

while play == 'yes':
    while True:
        choice = input("What do you pick? (Rock/Paper/Scissors) ").lower()
        if choice not in choices:
            print("This is not a valid choice!")
            continue
        else:
            print("You chose: " + choice.title())
            break
    aiChoice = choices[random.randrange(0, len(choices))]
    print("The computer chose: " + aiChoice.title())
    if choice == aiChoice:
        print("It's a draw!")
    elif choice == choices[0] and aiChoice == choices[1]:
        print("Paper beats rock.")
        print("The computer has won!")
    elif choice == choices[0] and aiChoice == choices[2]:
        print("Rock beats scissors.")
        print("You have won!")
    elif choice == choices[1] and aiChoice == choices[0]:
        print("Paper beats rock.")
        print("You have won!")
    elif choice == choices[1] and aiChoice == choices[2]:
        print("Scissors beats paper.")
        print("The computer has won!")
    elif choice == choices[2] and aiChoice == choices[0]:
        print("Rock beats scissors.")
        print("The computer has won!")
    elif choice == choices[2] and aiChoice == choices[1]:
        print("Scissors beats paper!")
        print("You have won!")
    while True:
        play = input("Do you want to play again? ").lower()
        if play != 'yes' and play != 'no':
            print("This is not a valid choice!")
            continue
        else:
            print("\n")
            break
    
    
