sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = [len(word.strip(".,")) for word in sentence.split(" ")] 
print(words)
