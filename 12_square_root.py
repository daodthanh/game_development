num = int(input("Input the number: "))
threshold = 0.1
temp = num / 2

while temp *temp - num > threshold:
   temp = (temp + num/temp)/2

print(temp)



