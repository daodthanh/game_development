# real_cal.py
a = input("a: ")
b = input("b: ")
operation = input("operation: ")
command = "result = " + a + " " + operation + " " + b + "; print('Result: ', result)"
exec(command)
# print(result)