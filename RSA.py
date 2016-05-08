# RSAEncrypter
from mathtools import *

class RSAEncryptor:

	def __init__(self, min_p):
		self.n, self.e, self.d = generateRSAKeys(min_p)

	def getPublicKey(self):
		return (self.n,self.e)

	def decrypt(self, encrypted_message):
		return fast_mod_exp(encrypted_message, self.d, self.n)

	def encrypt(self, message):
		return fast_mod_exp(message, self.e, self.n)