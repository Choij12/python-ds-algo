# from data_structures.hashtable import Hashtable
import re

def first_repeated_word(string):
    set1 = set()
    string = re.sub(r'[^\w\s]','', string)
    string = re.sub(r'\n', '', string)
    string = string.split(" ")

    print(string)
    for word in string:
        if word and word.lower() in set1:
            return word.lower()
        else:
            set1.add(word.lower())
            print(set1)
