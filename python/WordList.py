''''
This program will take a user's input, put it into a list, 
and let the user choose what to do with that list.
Author: Lauren White
Assignments: 10, CS120
Date: 11/24/24
'''
# List to hold all user words
word_list = []
# Joiner lists within functions
joiner = ", "

# Print all capital letters from the user_words list
def capital_letters():
    upper_list = []
    print("The capitalized letters are: ")
    # Goes through each letter in each element to find capital letters
    for item in word_list:
        for letter in item:
            if letter == letter.upper():
                upper_list.append(letter)
    # Prints capital letters
    print(joiner.join(upper_list))

# Gets every second letter from a word
def second_letter():
    letter_list = []
    print("The second letter for each word is: ")
    # Adds every second letter to letter_list
    for item in word_list:
        letter_list.append(item[1])
    # Prints all second letters
    print(joiner.join(letter_list))
                
# Counts vowels
def count_vowels():
    counter = 0
    # Goes through each letter in each element to count every vowel
    for item in word_list:
        for letter in item:
            letter = letter.lower()
            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                counter += 1
    # Prints the counted vowels
    print("There are", counter, "vowels in the entire list.")

# Replaces vowels with underscores
def underscores():
    underscores_list = []
    print("Every word with all the vowels replaced are: ")
    # Breaks apart each element and puts it into a list
    for item in word_list:
        position = 0
        letter_list = []
        for letter in item:
            letter_list.append(letter)
        # Replaces the vowels in letter_list
        for unit in letter_list:
            unit = unit.lower()
            if unit == "a" or unit == "e" or unit == "i" or unit == "o" or unit == "u":
                letter_list[position] = "_"
            position += 1
        # Joins the letter list and adds the underscored word to the new list
        new_item = "".join(letter_list)
        underscores_list.append(new_item)
    # Prints every word with replaced vowels
    print(joiner.join(underscores_list))

# Gets position of each vowel
def vowel_position():
    item_position = 0
    print("Every word with all the vowels replaced are: ")
    # Goes through each list item
    for item in word_list:
        position_list = []
        letter_position = 0
        for letter in item:
            letter = letter.lower()
            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                position_list.append(letter_position)
            letter_position += 1
        # Prints the vowel position for each element in the list
        print("The vowel position(s) for", item, "is/are", position_list)
        item_position += 1

# Gets user input and holds the execution of the other functions
def main():
    # Prints instructions
    print("Create a list. After finishing it, choose what action you want for that list.")
    print("Enter 'exit' to finish the list.")
    # Lets user add elements to word_list
    while True:
       entry = input("Enter something into the list: ")
       if entry.lower() == 'exit':
           break
       word_list.append(entry)
    # Prints new instructions and lets the user choose which function to execute
    print("Options: find capital, second letter, count vowels, replace vowels, vowel postion")
    answer = input("Choose: ")
    if answer.lower() == "find capital":
       capital_letters()
    elif answer.lower() == "second letter":
       second_letter()
    elif answer.lower() == "count vowels":
       count_vowels()
    elif answer.lower() == "replace vowels":
        underscores()
    elif answer.lower() == "vowel position":
        vowel_position()

# Output
if __name__ == '__main__':
    main()