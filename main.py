import json
import difflib
import keyboard

data = json.load(open("data.json"))

def search_for_word(word):
    closest_words = difflib.get_close_matches(word, data.keys())
    if word in data.keys():
        list_to_paragraph(data[word])
    elif len(closest_words) > 0:
        input1 = input(f"Do you mean the word {closest_words[0]}? \nYes/No: ")
        if input1 in ["no", "n"]:
            print("Sorry I cant find your word.")
        elif input1 in ["yes", "y"]:
            list_to_paragraph(data[closest_words[0]])
    else:
        print("There is no such word!")

def list_to_paragraph(list_of_meanings):
    for sentence in list_of_meanings:
        print(sentence)

app_activation = input("search for a word? \nYes/No: ").lower()

if app_activation in ["yes", "y"]:
    while True:
        word =input("Enter word to be searched: ").lower()
        search_for_word(word)
        confirm_exit = input("\nSearch another word (yes/no)? Enter no to exit: ")
        if confirm_exit in ["no", "n"]:
            break
        else:
            continue
else:
    print("Invalid input!")

