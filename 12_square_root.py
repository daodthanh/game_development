num = int(input("Input the number: "))
threshold = 0.1
temp = num

while temp *temp - num > threshold:
   temp = (temp + num/temp)/2

print(temp)



