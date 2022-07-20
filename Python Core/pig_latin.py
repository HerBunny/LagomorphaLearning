# Pig Latin

"""
The brief for this project is for a program that can take a word, or phrase
from the user, and translate it into "pig latin". This, however,
won't pass the 'Pig Latin' code coach. As this program capitalises the
first letter of each word, following a '.', '?' and '!'. 
"""

def punctuation(words, punct):
    """
    this function checks for punctuation at the end of words in a list. It then seperates them out as a seperate element in the list.
    """
    result = []

    for item in words:
        if item[-1] in punct:
            result.append(item[0:-1])
            result.append(item[-1])
        else:
            result.append(item)
    return result
        
def pig_latin(words, punct):
    """
    function to determine translate words in list, into Pig Latin.
    """
    queue = words
    trans_list = []
    word = ""


    while len(queue) > 0:
        word = queue.pop(0)
        num_check = word.isdigit()
            
        if num_check == True:
            trans_list.append(word)
        elif word in punct:
            trans_list.append(word)
        else:
            head = word[0]
            body = word[1:]
            translated = (body + head + "ay")
            trans_list.append(translated)              

    return trans_list

def str_stitcher(words, punct):
    """
    combine all list elements into a single output string.
    """
    result = ""
    word_queue = words

    while len(word_queue) > 0:
        word = word_queue.pop(0)
        
        if len(result) == 0 or result[-2] in punct[2:]:
            word = word[0].upper() + word[1:]
            
        if word in punct:
            result = result[:-1] + word + " "
        else:
            result += word + " "
    
    return result


if __name__ == "__main__":
    
    words = ""
    punct = ["'", ",", ".", "?", "!"]
    romans = "Alright, but apart from the sanitation, the medicine, education, wine, public order, irrigation, roads, the fresh-water system, and public health, what have the Romans ever done for us?"

    
    if __name__ == "__main__":

        initial_text_input = input("Please enter some text for translation, or 'quit' to exit, or hit enter: ") or romans

        words = initial_text_input
        print(f"\n Original: {words}")

        words = initial_text_input.lower()
        words = initial_text_input.split()
        words = punctuation(words, punct)
        words = pig_latin(words, punct)
        words = str_stitcher(words, punct)
        print(f"\n Translated: {words}")
