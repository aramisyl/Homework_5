initial_word = input("Please provide a word in singular.").lower()
def pluralize(word):
    match word[-1]:
        case "s" | "x" | "z" | "ch" | "sh":
            word = word[:-1] + 'es'
            return word
        case "y":
            if word[-2] in ["a", "e", "i", "o", "u"]:
                word = word + "s"
            else:
                word = word[:-1] + "ies"
            return word

print(pluralize(initial_word))