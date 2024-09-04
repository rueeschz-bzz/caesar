def vigenere_encrypt(plaintext, keyword):
    plaintext = plaintext.upper()
    keyword = keyword.upper()

    plaintext = ''.join(filter(str.isalpha, plaintext))

    ciphertext = []

    keyword_length = len(keyword)

    keyword_index = 0
    for char in plaintext:
        key_char = keyword[keyword_index % keyword_length]
        key_value = ord(key_char) - ord('A')

        char_value = ord(char) - ord('A')
        encrypted_value = (char_value + key_value) % 26
        encrypted_char = chr(encrypted_value + ord('A'))

        ciphertext.append(encrypted_char)

        keyword_index += 1

    return ''.join(ciphertext)


def main():
    plaintext = input("Geben Sie den Klartext ein: ")
    keyword = input("Geben Sie das Schlüsselwort ein: ")

    ciphertext = vigenere_encrypt(plaintext, keyword)
    print(f"Verschlüsselter Text: {ciphertext}")


if __name__ == "__main__":
    main()
