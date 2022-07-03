sounds = input()
words = sounds.split()
identity = ""


for item in words:
    if item == "Grr":
        identity += "Lion"
    if item == "Rawr":
        identity += "Tiger"
    if item == "Ssss":
        identity += "Snake"
    if item == "Chirp":
        identity += "Bird"
    
    identity += " "


print(identity)
