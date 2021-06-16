TEXT = [
    '''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive  
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',
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


TEXTS = [TEXT[0], TEXT[1], TEXT[2]]
divider = '-' * 50
text_dict = {}
for i, text in enumerate(TEXTS, 0):
    text_dict[i] = {"words": len([t for t in text.split(" ") if t not in " .,"]),
                    "title_case": len([word for word in text.split(" ") if word.istitle()]),
                    "uppercase": len([uppercase for uppercase in text.split(" ") if uppercase.isupper()]),
                    "lowercase": len([lowercase for lowercase in text.split(" ") if lowercase.islower()]),
                    "number": len(([number for number in text.split(" ") if number.isdigit()])),
                    "sum": sum([int(n) for n in text.split(" ") if n.isdigit()]),
                    "clean_text": text.replace('.', ' ').replace(',', ' ')
                    }

# format string
f = "{:5}|{:20}|{:5}"

# register users
register_users = {'bob': 123, 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

username = input('username: ')

if username in register_users:  # registration check
    user_password = input("password: ")
    print(divider)

    # login control
    if username in register_users.keys() and user_password == str(register_users[username]):
        print(f"Welcome in the app {username},\nWe have {len(TEXTS)} texts to be analyzed.")
        print(divider)

        number_text = input("Enter a number btw. 1 and 3 to select: ")
        print(divider)
        if number_text.isalpha():  # number control
            print('Enter a number, not a letter!')
        else:
            number_text = int(number_text)
            if number_text == 1:
                print(f"There are {text_dict[0].get('words')} words in the selected text.")
                print(f"There are {text_dict[0].get('title_case')} title_case words.")
                print(f"There are {text_dict[0].get('uppercase')} uppercase words.")
                print(f"There are {text_dict[0].get('lowercase')} lowercase words.")
                print(f"There are {text_dict[0].get('number')} numeric strings.")
                print(f"The sum of all numbers {text_dict[0].get('sum')}")
                print(divider)
                print(f.format("LEN", "     OCCURRENCES     ", "NR."))
                print(divider)
                counts = {}
                for i in text_dict[0].get('clean_text').split():
                    if len(i) not in counts:
                        counts[len(i)] = 1
                    else:
                        counts[len(i)] += 1
                sorted_counts = sorted(counts.items())
                for i, j in sorted_counts:
                    print(f.format(i, j * '*', j))

            elif number_text == 2:
                print(f"There are {text_dict[1].get('words')} words in the selected text.")
                print(f"There are {text_dict[1].get('title_case')} title_case words.")
                print(f"There are {text_dict[1].get('uppercase')} uppercase words.")
                print(f"There are {text_dict[1].get('lowercase')} lowercase words.")
                print(f"There are {text_dict[1].get('number')} numeric strings.")
                print(f"The sum of all numbers {text_dict[1].get('sum')}")
                print(divider)
                print(f.format("LEN", "     OCCURRENCES     ", "NR."))
                print(divider)
                counts = {}
                for i in text_dict[1].get('clean_text').split():
                    if len(i) not in counts:
                        counts[len(i)] = 1
                    else:
                        counts[len(i)] += 1
                sorted_counts = sorted(counts.items())
                for i, j in sorted_counts:
                    print(f.format(i, j * '*', j))

            elif number_text == 3:
                print(f"There are {text_dict[2].get('words')} words in the selected text.")
                print(f"There are {text_dict[2].get('title_case')} title_case words.")
                print(f"There are {text_dict[2].get('uppercase')} uppercase words.")
                print(f"There are {text_dict[2].get('lowercase')} lowercase words.")
                print(f"There are {text_dict[2].get('number')} numeric strings.")
                print(f"The sum of all numbers {text_dict[2].get('sum')}")
                print(divider)
                print(f.format("LEN", "     OCCURRENCES     ", "NR."))
                print(divider)
                counts = {}
                for i in text_dict[2].get('clean_text').split():
                    if len(i) not in counts:
                        counts[len(i)] = 1
                    else:
                        counts[len(i)] += 1
                sorted_counts = sorted(counts.items())
                for i, j in sorted_counts:
                    print(f.format(i, j * '*', j))
            else:
                print('Wrong number entered')

    else:
        print("Wrong password!")

else:
    print("You are not registered!")
