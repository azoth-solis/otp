import random

class OTP:

    def __init__(self, data):
        self.data = ''.join('{0:b}'.format(ord(_)).zfill(8) for _ in data)
        self.secret = ''.join('{0:b}'.format(_).zfill(8) for _ in random.randbytes(len(self.data) // 8))
        
    def plaintext(self):
        return self.data
        
    def key(self):
        return self.secret
        
    def ciphertext(self):
        return ''.join(str(int(i) ^ int(j)) for i, j in zip(self.data, self.secret))
        
