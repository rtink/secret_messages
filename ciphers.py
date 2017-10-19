class Cipher:
    def encrypt(self, message):
        self.message = message
        raise NotImplementedError()

    def decrypt(self, message):
        self.message = message  
        raise NotImplementedError()
