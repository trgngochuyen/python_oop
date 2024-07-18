import string


class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def __call__(self, text):
        encrypted_text = ""
        for letter in text.lower():
            if letter in string.ascii_lowercase:
                alphabet_index = string.ascii_lowercase.index(letter)
                encrypted_alp_index = alphabet_index - self.key
                encrypted_text += string.ascii_lowercase[encrypted_alp_index]
            else:
                pass
        print(encrypted_text)

    def print_mapping(self):
        for letter in string.ascii_lowercase:
            print(f"{letter} -> {string.ascii_lowercase[string.ascii_lowercase.index(letter) - self.key]}")
        
    def decrypt(self, text):
        decrypted_text = ""
        for letter in text.lower():
            if letter in string.ascii_lowercase:
                decrypted_text += string.ascii_lowercase[string.ascii_lowercase.index(letter) + self.key]
            else:
                pass
        print(decrypted_text)

cipher = CaesarCipher(3)
cipher("hello world")
cipher.print_mapping()
cipher.decrypt('ebiiltloia')