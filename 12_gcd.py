# gcd.py
import time
def check_prime(num):
  is_prime = True
  if num > 2: 
    for i in range(2, num):
      if num % i == 0:
        is_prime = False
  return is_prime

def prime_factors(num):
  factors = []
  temp = int(num)
  while temp > 1:
    for i in range(2, temp+1):
      if temp % i == 0 and check_prime(i):
        print(i)
        factors.append(i)
        temp = temp // i
        print(temp)
        break
  return factors

def common_factors(list1, list2):
  cf = []
  if len(list1) < len(list2):
    for e in list1:
      if e in list2:
        cf.append(e)
  else: 
    for e in list2:
      if e in list1:
        cf.append(e)
  return cf


num1 = int(input("Input your number 1: "))
num2 = int(input("Input your number 2: "))
# begin = system.time()
num1_factors = prime_factors(num1)
num2_factors = prime_factors(num2)
print(f"Divisors of {num1} are ", num1_factors)
print(f"Divisors of {num2} are ", num2_factors)
cf = common_factors(num1_factors, num2_factors)
print(cf)

