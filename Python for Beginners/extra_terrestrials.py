# Extra-Terrestrials

phrase = input()

human_words = []
alien_words = []
punctuations = [",", "."]
output = ""
x = ""

for char in phrase:
    if char != " " and char != "," and char != ".":
        x += char
    elif char == " " or char == "," or char == ".":
        if len(x) > 0:
            human_words.append(x)
        x = ""
        human_words.append(char)

for items in human_words:
    y = items[::-1]
    alien_words.append(y)

for items in alien_words:
    output += items

print(human_words)
print(alien_words)
print(output)
