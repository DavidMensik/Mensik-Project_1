'''
author = David Mensik
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

SEPARATOR = "-" * 65
REGISTERED_USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

print(SEPARATOR)
print("Welcome to the app. Please log in: ")

username = input("USERNAME: ")
password = input("PASSWORD: ")

attempt = 3

while REGISTERED_USERS.get(username) != password:
    print("Wrong username or password. You have " + str(attempt) + "/3 attempts left.")
    attempt = attempt - 1
    if attempt == -1:
        print("You ran out of attempts!")
        quit()
    username = input("USERNAME: ")
    password = input("PASSWORD: ")

print(SEPARATOR)
print("We have 3 texts to be analyzed.")
choice = input("Enter a number btw. 1 and 3 to select: ")

while choice not in ["1","2","3"]:
    print("You must enter number between 1 and 3!")
    choice = input("Enter a number btw. 1 and 3 to select: ")

print(SEPARATOR)

choice = int(choice)
words_split = TEXTS[choice - 1].split()
words_count = len(words_split)

words_titlecase = 0
words_uppercase = 0
words_lowercase = 0
words_numeric = 0

while words_split:
    words_pop = words_split.pop()
    if words_pop.istitle():
        words_titlecase = words_titlecase + 1
    else:
        words_titlecase = words_titlecase
    if words_pop.isupper():
        words_uppercase = words_uppercase + 1
    else:
        words_uppercase = words_uppercase
    if words_pop.islower():
        words_lowercase = words_lowercase + 1
    else:
        words_lowercase = words_lowercase
    if words_pop.isnumeric():
        words_numeric = words_numeric + 1
    else:
        words_numeric = words_numeric

print("There are " + str(words_count) + " words in the selected text.")
print("There are " + str(words_titlecase) + " titlecase words.")
print("There are " + str(words_uppercase) + " uppercase words.")
print("There are " + str(words_lowercase) + " lowercase words.")
print("There are " + str(words_numeric) + " numeric strings.")

print(SEPARATOR)

words_split = TEXTS[choice - 1].split()

bar = []

while words_split:
    comma_dot_del = words_split.pop()
    comma_dot_del = comma_dot_del.replace(",", "")
    comma_dot_del = comma_dot_del.replace(".", "")
    length_count = len(comma_dot_del)
    bar.append(length_count)

word_count = 1

while word_count <= max(bar):
    if bar.count(word_count) > 0:
        print(str(word_count) + " " + "*" * bar.count(word_count) + " " + str(bar.count(word_count)))
        word_count = word_count + 1
    else:
        word_count = word_count + 1

words_split = TEXTS[choice - 1].split()
numeric_words = []

while words_split:
    num_word = words_split.pop()
    if num_word.isnumeric():
        num_word = float(num_word)
        numeric_words.append(num_word)
    else:
        num_word = num_word

print(SEPARATOR)
print("If we summed all the numbers in this text we would get: " + str(sum(numeric_words)))
print(SEPARATOR)


