from mathtools import *
from RSA import *

# print("result = ", fast_exp(1233312,33112))
x = 121
n = 534231
p = 1343
print("result = ", fast_mod_exp(x,n,p) ==(x**n) %p)

min_p = 2012113131341
crypto = RSAEncryptor(min_p)

message = 12

enc_message = crypto.encrypt(message)

dec_message = crypto.decrypt(message)

print("message = ", message)
print("encrypted message = ", enc_message)
print("decrypted message = ", dec_message)
print("Success: ", message == dec_message)