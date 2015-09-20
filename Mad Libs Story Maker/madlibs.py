# Determine whether to use he, she or they for pronouns in the story
def determineGender(gender):
    if (gender == "male"):
        return("he")
    elif (gender == "female"):
        return("she")
    else:
        return("they")

# Assemble story
story_name = input("Please enter a name: ").title()
story = story_name
gender = input("Gender (Male, Female, Other): ").lower()
story += " was walking down the road one day when {} saw a gigantic ".format(determineGender(gender))
story_object = input("Please enter an object: ")
story += story_object
story += " on the other side of the road. Everyone was staring at it!\n"
story += " {} was about to shout for the onlookers to move out of the way, but it was too late...".format(story_name)
story += " The massive {} had fizzed up and exploded! The onlookers had felt the rage of the evil villain, ".format(story_object)
story += input("Please enter a villain's name: ").title()
story += ". All was lost, there was no hope left.\n"
story += " Mmmm... {}...".format(story_object)

# Print the story
f = open('story.txt', 'w')
f.write(story)
f.close()
print(story)

print("{} was feeling happy.".format(story_name))
