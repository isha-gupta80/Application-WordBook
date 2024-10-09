import json
from difflib import get_close_matches
elements = json.load(open("wordbook.json"))
 
def findmeaning(word):
    word = word.lower()
    if word.lower() in elements:
        return elements[word.lower()]
    elif word.upper() in elements:
        return elements[word.upper()]
    elif word.title() in elements:
        return elements[word.title()]
    elif len(get_close_matches(word,elements.keys())) > 0:
        closematches = (get_close_matches(word,elements.keys())[0])
        user_decision = input("Are you looking for %s instead?[y/n]" % closematches)
        
        if user_decision =="y":
            return elements[get_close_matches(word,elements.keys())[0]]
        elif user_decision =="n":
            
            return "I can't find your word,I'm sorry."
        else:
        
            return "sorry ! I cannot find your word."
    else:
        return "I can't find this word. please look for spelling mistakes"
word = input("Type Any word Here:")

output = findmeaning(word)      

if type(output) == list:
   for i in output:
    print(i)
else:
    print(output)