def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


text = input("Geben Sie den Text ein, den Sie verschlüsseln/entschlüsseln möchten: ")
shift = int(input("Geben Sie die Verschiebung ein (eine ganze Zahl): "))
mode = input("Möchten Sie verschlüsseln oder entschlüsseln? (geben Sie 'encrypt' oder 'decrypt' ein): ").strip().lower()

if mode not in ['encrypt', 'decrypt']:
    print("Ungültige Eingabe! Bitte geben Sie 'encrypt' oder 'decrypt' ein.")
else:
    result = caesar_cipher(text, shift, mode)
    print(f"Ergebnis: {result}")
