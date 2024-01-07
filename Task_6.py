def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

plaintext = input("Please, provide text to cipher.")
shift = 3

ciphertext = caesar_cipher(plaintext, shift)
print(ciphertext)