from ciphers import Cipher


class Keyword_cipher(Cipher):
    '''A keyword is used, repeated letters of the keyword
       are removed, the cipher alpabet is generated with
       the keyword matching the beginning of the alphabet
       until the keyword is used up, the rest of the
       alphabet remaing the same except for those
       letters matching the keyword. User selects
       keyword that will be used.
    '''
    def __init__(self, user_keyword):
        self.cipher_text = []
        self.alpha = map(chr, range(ord('a'), ord('z') + 1))
        self.letters = ''.join(self.alpha)
        self.keyword = user_keyword
        self.new_letters = ''.join(
            [x for x in self.letters if x not in self.keyword]
            )
        self.combo = self.keyword + self.new_letters
        for letter in self.combo:
            if letter not in self.cipher_text:
                self.cipher_text.append(letter)

    def encrypt(self, message):
        '''Encrypts a message entered by a user'''
        output = []
        for char in message:
            try:
                message_index = self.letters.index(char)
                output.append(self.cipher_text[message_index])
            except ValueError:
                output.append(char)
        print(''.join(output))

    def decrypt(self, message):
        '''Decrypts a message entered by a user'''
        output = []
        for char in message:
            try:
                message_index = self.cipher_text.index(char)
                output.append(self.letters[message_index])
            except ValueError:
                output.append(char)

        print(''.join(output))
