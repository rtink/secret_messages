from ciphers import Cipher


class Atbash(Cipher):
    '''The Atbash Cipher method maps the alphabet to its reverse
    for ex. the last letter becomes the first
    the second letter becomes the second to last, etc'''
    def __init__(self):
        self.alpha = map(chr, range(ord('a'), ord('z') + 1))
        self.letters = ''.join(self.alpha)
        self.cipher_list = self.letters[::-1]

    def encrypt(self, message):
        """Encrypts message entered by a user."""
        output = []
        for char in message:
            try:
                message_index = self.letters.index(char)
                output.append(self.cipher_list[message_index])
            except ValueError:
                output.append(char)
        print(''.join(output))

    def decrypt(self, message):
        """Decrypts message entered by a user"""
        output = []
        for char in message:
            try:
                message_index = self.cipher_list.index(char)
                output.append(self.letters[message_index])
            except ValueError:
                output.append(char)
        print(''.join(output))
