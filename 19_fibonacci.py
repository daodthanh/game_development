# 19_fibonacci.py

print("Hello! Fibonnaci program")
print("This program will show the first ten number in Fibonaci series")
pre1 = 1
pre2 = 1
print(f"{pre1}, {pre2}", end=", ")
nxt = pre1 + pre2
for i in range(1,10):
  print(nxt, end=", ")
  pre1 = pre2
  pre2 = nxt
  nxt = pre1 + pre2
print()

