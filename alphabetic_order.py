words = input("Ender your words here: ")


words = words.split()
words.sort()

for word in words:
    print(word)