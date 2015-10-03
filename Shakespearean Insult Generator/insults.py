import random
import os
import yaml

insults = yaml.load(open(os.path.dirname(__file__) + '/insults.yml'))

def generateInsult():
    column1 = random.choice(insults['column1'])
    column2 = random.choice(insults['column2'])
    column3 = random.choice(insults['column3'])
    print("\n" + "Thou", column1, column2, column3)

numberOfInsults = int(input("How many insults would you like to generate? "))
while numberOfInsults > 0:
    generateInsult()
    numberOfInsults = numberOfInsults - 1
