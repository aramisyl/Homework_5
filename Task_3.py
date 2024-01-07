text = input("Введите текст")
sentences = text[:-1].split(".")

i = 1
for sentence in sentences:
    words = len(sentence.split(" "))
    print("Sentence {} has {} words.".format(i, words))
    print(f"Sentence {i} has {words} words.")
    print("Sentence %d has %d words." % (i, words))
    i += 1