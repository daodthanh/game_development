# check_prime.py
def check_prime(num):
  is_prime = True

  if num > 2: 
    for i in range(2, num):
      if num % i == 0:
        print("Divisor: ", i)
        is_prime = False
  return is_prime

num = int(input("Input your number: "))
print(f"Is {num} a prime number? ", check_prime(num))
