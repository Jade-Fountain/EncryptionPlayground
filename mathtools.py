#mathtools.py

def fast_exp(x,n):
	if n == 1:
		return x
	if n % 2 == 0:
		return fast_exp(x**2,n/2)
	else:
		return x * fast_exp(x**2,(n-1)/2)

def fast_mod_exp(x,n,p):
	if n == 1:
		return x % p
	if n % 2 == 0:
		return fast_mod_exp(x**2 % p,n/2,p)
	else:	
		return (x % p) * fast_mod_exp(x**2 % p,(n-1)/2,p)

# print("result = ", fast_exp(1233312,33112))
x = 121
n = 52
p = 1343
print("result = ", fast_mod_exp(x,n,p) ==(x**n) %p)


