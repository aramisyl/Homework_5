initial_word = input("Please provide a word in singular.").lower()
def pluralize(word):
    match word[-1]:
        case "s" | "x" | "z":
            word = word + 'es'
            return word
        case "h":
            if word [-2] in ('s', 'c'):
                word = word + 'es'
            else:
                word = word + "s"
            return word
        case "y":
            if word[-2] in ["a", "e", "i", "o", "u"]:
                word = word + "s"
            else:
                word = word[:-1] + "ies"
            return word
        case _:
            return word + "s"



print(pluralize(initial_word))