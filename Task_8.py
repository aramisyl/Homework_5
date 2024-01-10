cipher = {
    '.-  ': 'А', '-...': 'Б', '- --': 'В', '--. ': 'Г',
    '-.. ': 'Д', '.   ': 'Е', '...-': 'Ж', '--..': 'З',
    '..  ': 'И', '.---': 'Й', '-.- ': 'К', '.-..': 'Л',
    '--  ': 'М', '-.  ': 'Н', '--- ': 'О', '.--.': 'П',
    '.-. ': 'Р', '... ': 'С', '-   ': 'Т', '..- ': 'У',
    '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
    '----': 'Ш', '--.-': 'Щ', '-. -': 'Ъ', '-.--': 'Ы',
    '-..-': 'Ь', '. -.': 'Э', '..--': 'Ю', '.-.-': 'Я',
}

plaintext = input("Введите текст для шифрования.")
symbols_to_keep = ["-", ".", " "]

def strip_symbols_except(text):
    stripped_text = ''
    for char in text:
        if char in symbols_to_keep or char.isspace():
            stripped_text += char

    return stripped_text

def split_string(text):
    return [text[i: i + 4] for i in range(0, len(text), 4)]

def decipher(text):
    decrypted_text = ''
    cleaned_text = strip_symbols_except(plaintext)
    for item in split_string(cleaned_text):
        decrypted_text += cipher.get(item, "?")
    return decrypted_text

print(decipher(plaintext))




