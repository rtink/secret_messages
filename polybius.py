from ciphers import Cipher


class Polybius(Cipher):
    '''Polybius cipher: each letter is
       represented by its coordinates in a 5x5 grid.
       A 5x5 array is created and letters in the message
       are mapped to the x,y coordinates.
    '''
    def __init__(self):
        self.alpha = map(chr, range(ord('a'), ord('z') + 1))
        self.letters = ''.join(self.alpha)
        self.coord = []

        for y in range(6):
            for x in range(6):
                self.coord.append(str(y) + str(x))

    def encrypt(self, message):
        '''Encrypts a message entered by a user'''
        output = []
        for char in message:
            try:
                message_index = self.letters.index(char)
                output.append(self.coord[message_index])
            except ValueError:
                output.append(char)
        print(''.join(output))

    def decrypt(self, message):
        '''Decrypts a message entered by a user'''
        output = []
        message = (str(message)).replace(" ", "  ")
        for i in range(0, len(message), 2):
            try:
                combined_letter = message[i] + message[i + 1]
                message_index = self.coord.index(combined_letter)
                output.append(self.letters[message_index])
            except ValueError:
                output.append(message[i])
        print(''.join(output))
