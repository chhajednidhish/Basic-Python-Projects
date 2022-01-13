'''
                Created by : Nidhish Ajay Chhajed
                Copyrighted content.

'''

storyToBeUsed = ""

def Story1():
    # Taking the inputs
    vegetable = input("Enter name of any vegetable: ")
    desert = input("Enter name of any desert you like: ")
    fast_food = input("Enter name of any fast food: ")
    flavor = input("Enter any flavor you like: ")

    musical_instrument = input("Enter name of any musical instrument: ")
    animal_sound = input("Enter an animal sound: ")

    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")

    magical_words = input("Enter any one of the three magical words: ")
    # Creating the story using the inputs given by user
    story = f"""\nEveryone Farts! It's a fact!
Some people have farts that sounds like a {musical_instrument} while some people have farts that sounds like {animal_sound}.
Some farts smell like {flavor}, while others smell like {vegetable}.
If you eat too many {fast_food} your farts may {verb} right out of you and smell like rotted {desert}.
Some farts are silent but {adjective}.
Whatever kind of fart you {verb} out of yourself, be sure to say {magical_words}."""
    return story


def main():
    # Introuducing madlibs to users
    print("\t --- This is a MadLibs Game where you provide some words and we create a story for you! --- \n")
    storyToBeUsed = Story1()
    print(storyToBeUsed)


if __name__ == "__main__":
    main()




