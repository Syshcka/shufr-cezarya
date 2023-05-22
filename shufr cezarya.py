def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            offset = (ord(char) - base + shift) % 26
            result += chr(base + offset)
        else:
            result += char
    return result

text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))

result = caesar_cipher(text, shift)

print("Результат шифрования:", result)
