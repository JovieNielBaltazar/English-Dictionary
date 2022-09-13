import json

data = json.load(open("data.json"))

def search_for_word(input1):
    if input1 in data:
        for item in range(len(data[input1])):
            print(data[input1][int(item)-1])
    else:
        print("the word cannot be found, please try again!")


input1 =input("Enter word to be searched: ")
search_for_word(input1)