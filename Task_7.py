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
def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None
def telegraph(text):
    global encrypted_char
    text = text.upper()
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_char = get_key_by_value(cipher, char)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Введите текст для шифрования.")

ciphertext = telegraph(plaintext)
print(ciphertext)