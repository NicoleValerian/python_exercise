# For a list of words, print out each word on a separate line, but in all uppercase. 

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

# For example:

# # this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})

def print_uppercased_words(words):
    """Print out each word on a separate line, uppercased"""

    for word in words:
        print(word.upper())

def print_uppercased_words_e(words):
    """Print out only words starting with "e"/"E" on a separate line, uppercased"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_uppercased_chosen_letter(words, must_start_with):
    """Print out only words starting with input letter on a separate line, uppercased"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


