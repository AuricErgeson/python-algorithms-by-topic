"""
Display only those characters which are present at an even index number in given string
"""

text = "pynative"

for index,letter in enumerate(text):
    if index % 2 == 0:
        print(letter)

for letter in text[0::2]:
    print(letter)

