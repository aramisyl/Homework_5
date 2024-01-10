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

flipped_cipher = {value: key for key, value in cipher.items()}

def telegraph(text):
    text = text.upper()
    encrypted_text = ""
    for char in text:
        decrypted_char = flipped_cipher.get(char)
        encrypted_text += decrypted_char
    return encrypted_text

plaintext = input("Введите текст для шифрования.")

ciphertext = telegraph(plaintext)
print(ciphertext)