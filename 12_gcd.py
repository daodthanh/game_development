# gcd.py
def check_prime(num):
  is_prime = True
  if num > 2: 
    for i in range(2, num):
      if num % i == 0:
        is_prime = False
  return is_prime

def prime_factors(num):
  factors = []
  for i in range(2, num):
    if num % i == 0 and check_prime(i):
      factors.append(i)
  return factors

num1 = int(input("Input your number 1: "))
num2 = int(input("Input your number 2: "))
print(f"Divisors of {num1} are ", prime_factors(num1))
print(f"Divisors of {num2} are ", prime_factors(num2))