
def madlib():

    
    ''' Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price.
    It consists of one player prompting others for a list of words to substitute for 
    blanks in a story before reading aloud.
    The game is frequently played as a party game or as a pastime.'''




    from turtle import color
    print(" Welcome to Cutting-Edge Technology Madlib Game")
    print("Put your guess in the next to the given world ")
    print(" Enjoy the game")

    person_in_room1 = input("Person In Room: ")
    number1 = input("Number: ")
    part_of_the_body1 = input("Part Of the Body(PLURAL): ")
    aplace = input("A Place: ")
    adjectives = input("Adjectives: ")
    part_of_the_body2 = input("Part Of the Body(PLURAL): ")
    person_in_room2 = input("Person In Room: ")
    nolin = input("Nolin: ")
    plural_nolin1 = input("Plural Nolin: ")
    number2 = input("Number: ")
    plural_nolin2 = input("Plural Nolin: ")
    article_of_clothing = input("Article of Clothing")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    color = input("Color:")

    madlib = f"This week only, {person_in_room1}'s Discount Tech is holding \
    a/an {number1}percent off sale! Get your {part_of_the_body1} on the coolest \
    gadgets of 1990s. \
    Dicman: Don't get caught walking around (the) {aplace} without this {adjectives} \
    portable CD player. Batteries and {part_of_the_body2}-phones not included.\
    Mobile Phone: Now you can gossip with {person_in_room2} without being plugged in to \
    a/an {nolin}.\
    Floppy {plural_nolin1} Save all your {plural_nolin1} on these storage discut that \
    hold up to {number2} megabytes.\
    Pagers: Stay connected to family and {plural_nolin2} with \
    communication you can clip on your {article_of_clothing}.\
    Sony {verb1}-Station:{verb2} your favorite video games \
    on this console that'll turn your friends {color} with envy."


    print(madlib)

if __name__ == '__main__':
    madlib()