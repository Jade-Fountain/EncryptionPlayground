from mathtools import *
from RSA import *

# print("result = ", fast_exp(1233312,33112))
x = 121
n = 534231
p = 1343
print("result = ", fast_mod_exp(x,n,p) ==(x**n) %p)

a = 12
m = 13
a_inv_mod_m = multiplicative_mod_inv(a,n)

#TODO: fix broken
print("Mult mod inv(",a,",",m," = ", a_inv_mod_m, "  || a*a_inv mod m = ", (a * a_inv_mod_m) % m)

min_p = 17
crypto = RSAEncryptor(min_p)

message = 12

enc_message = crypto.encrypt(message)

dec_message = crypto.decrypt(enc_message)

print("message = ", message)
print("encrypted message = ", enc_message)
print("decrypted message = ", dec_message)
print("Success: ", message == dec_message)