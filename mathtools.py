#mathtools.py
import random


def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def extended_gcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0:
        quotient = old_r / r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    # output "Bezout coefficients:", (old_s, old_t)
    # output "greatest common divisor:", old_r
    # output "quotients by the gcd:", (t, s)
    return (old_s, old_t, old_r, t, s)


def multiplicative_mod_inv(a,n):
	#compute b : a*b = 1 mod n
	x, y, gcd, t,s = extended_gcd(a,n)

	return x

def fast_exp(x,e):
	if e == 1:
		return x
	if e % 2 == 0:
		return fast_exp(x**2,e/2)
	else:
		return x * fast_exp(x**2,(e-1)/2)

def fast_mod_exp(x,e,n):
	if e == 1:
		return x % n
	if e % 2 == 0:
		return (fast_mod_exp(x, e/2, n) ** 2) % n
	else:	
		return (x * (fast_mod_exp(x,(e-1)/2,n) ** 2 )) % n

def is_prime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i*i <= n:
		#search through integers of form 6k+-1
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i = i + 6
	return True

def get_next_prime(min_p):
	#todo: optimise
	p = min_p
	while not is_prime(p):
		# print(p, "is NOT prime")
		if p%2 == 0:
			p += 1
		else:
			p+=2
	return p

def get_next_coprime(min_p,q):
	#todo: optimise
	p = min_p
	while (gcd(p,q) != 1):
		print(p, "is NOT co-prime to ", q)
		p += 1
		if p > q:
			return 1
	return p

#count coprimes of n
def eulers_totient(n):
	print("Eulers totient:" ,n)
	i = 1
	count = 1 #always count 1 and n
	# while i < n:
	# 	i = get_next_coprime(i + 1,n)
	# 	count += 1
	# 	print("Eulers totient = ", 	count)
	return count

def generateRSAKeys(min_p):
	#generate n
	p = get_next_prime(min_p)
	#todo: improve generation of q
	q = get_next_prime(p + 1)
	n = p * q
	print("n =", n, " = ", p, " * ", q)

	#Euler's Totient
	phi_n = n - (p+q+1)

	#generate e st gcd(e,phi_n) == 1
	#TODO: minimise bit-length and hamming weight of e
	e_start = random.randint(1,phi_n)
	e = get_next_coprime(e_start, phi_n)
	print("e = ", e)

	#d is s.t. d*e = 1 mod phi_n 
	d = multiplicative_mod_inv(e,phi_n)
	return n,e,d