# Search Engine

def lower_text(text, word):
    """
    Takes the two inputs, and coverts 
    them to lowercase.
    """
    text = text.lower()
    word = word.lower()
    
    search(text, word) 
    # Passes values to search function.

def search(text, word):
    """
    Searches for the specified word, in 
    the source text.
    """
    if word in text:
        print("Word found")
    else:
        print("Word not found")

if __name__ == "__main__":
    text = input()
    word = input()
    
    lower_text(text, word)