# square_root.py
def root(x):
  y =  x
  for i in range(20):
    y = (y + x/y) / 2.0
  return y

x = int(input("Input x: "))
print(root(x))