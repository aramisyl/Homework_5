from collections import Counter

text = input("Введите текст")
sentences = text[:-1].split(".")
C = Counter(sentences)
print(C.values())
print(C.keys())
index = 1;
while index < Counter.total(C):
    for key in C.keys():
        words = len(key.split(" "))
        print("Sentence {} has {} words.".format(index, words))
        print(f"Sentence {index} has {words} words.")
        print("Sentence %d has %d words." % (index, words))
        index += 1