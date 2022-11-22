# 13_euclid_gcd.py
num1 = int(input("Please input the dividend: "))
num2 = int(input("Please input the divisor: "))

if num1 % num2 == 0:
  print("The GCD: ",num2)
else:
  while num1 % num2 > 0:
    modular = num1 % num2
    num1 = num2
    num2 = modular

print("The GCD: ",num2)
