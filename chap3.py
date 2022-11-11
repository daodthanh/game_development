# chap3.py
#String
# seqence of character
name = "John Doe"
address = "121 Second Street"
print("length of name: ", len(name))
print(name[0])
for i in range(0, len(name)):
  print(name[i])

print(name[0] == address[0])

# Compare strings
print("abcd" < "abce")
print("123" < "345")
print("ab" < "abc")


a = "J"
b = "j"
c = "1"
if b < c:
  print("Lcase < numbers")
else:
  print("Lcase > numbesr")

if a < b:
  print("Ucase < Lcase")
else:
  print("Ucase > Lcase")

if a < c:
  print("Ucase < numbers")
else:
  print("Ucase > numbers")

city = input("Input the city: ")

if city < "Denver":
  print("The name given comes before Denver in an alphabetic list")
elif city > "Denve":
  print("The name given comes after Denver in an alphabetic list")
else:
  print("The name given was Denver")

# Slicing
statement = "print"
if statement[0:5] == "print":
  print("print statement")

if statement[:5] == "print":
  print("print statement too")

str = "Hello"
# str[3] = "#"
fname = "image"
print(fname)
fname = fname + ".jpeg"
print(fname)

if fname[len(fname)-4:len(fname)] == '.jpg':
  print("This is an image file")

if fname[len(fname) - 5:] == ".jpeg":
  print(fname)
  print("It should be change to .jpg")
  fname = fname[0:len(fname)-5]
  fname += ".jpg"
  print(fname)

print(city)
k = len(city)
city_reverse = ""
for i in range(0, len(city)):
  city = city + city[k-i-1]
  city_reverse += city[k-i-1]
print(city)
city = city[len(city)//2:]
print(city)
print(city_reverse)

str = "This string has 30 characters."
print(len(str))
print(str[0:30:2])
print(str[::-2])
print(str[:])

s = "chap3.py"

if s[len(s)-3:len(s)].upper() == '.PY':
  print("This is a Python program.")
else:
  print("This is not a Python program")

s = "hello to you all."
print(s)
print("Capitalize", s.capitalize())
print("Count ll", s.count("ll"))
print("Endswith ll",s.endswith("ll."))
print("Find you",s.find("you"))
print("Index you", s.index("you"))
print("Is digit", s.isdigit())
print("Is lower", s.islower())
print("Is upper", s.isupper())
print("Is space", s.isspace())
print("lower(): ", s.lower())
print("upper(): ", s.upper())
print("replace: ", s.replace("you all", "class"))
print("split: ", s.split(" "))
print(" split lines", s.splitlines())

poem = ''' 
           She walks in beauty like the night
           Of cloudless climes and starry skies,
           And all that's best of dark and bright
           Meets in her aspect and her eyes;
           Thus mellow's to that tender light
           Which Heaven to gaudy day denies.'''
print(poem)

program = '''list = [1,2,4,7,12,15,21]
for i in list:
  print(i, i * 2) '''
exec(program)

for i in range(0, len(name)):
  print(name[i], end='')
print()

print(name)

# Byte type
s = 'this is a string'
b = b'this is a string'
print(s[0])
print(b[0])

# same methods to string type but new one
b.decode("utf-8")

# TUPLE
tup1 = (2,3,5,7,11,13,17,19)
tup2 = ("Hydrogen", "Hellium", "Lithium", "Beryllium", "Boron", "Carbon")
tup3 = 'hi', 'ohio', 'salut'
tup4 = ("one",)
tup5 = "two",
tup6 = tup4 + tup5
print(tup1)
# tup1 = 6
# tup3[1]  ='bonjour'

for i in tup2:
  print(i)

atoms = ("Hydrogen",1, "Hellium",2, "Lithium",3, "Beryllium", 4,"Boron",5,"Carbon",6)
for i in atoms:
  print(i)

for i in atoms:
  if isinstance(i, int):
    j = i * 2
    print("has ", i, "protons and ", j, " neutrons. ")
  else:
    print("Element ", i)

for i in range(len(atoms)):
  if i % 2 == 1:
    j = atoms[i] * 2
    print("has ", atoms[i], "protons and ", j, " neutrons. ")
  else:
    print("Element ", atoms[i])

A = ()
for i in range(0, 51):
  A = A + (i*2, )
B= () #4,9,16,25,36,49,64,81,100
for i in range(0, 11):
  B = B + (i*i,)
C = ()
print(A)
print(B)
for i in A:
  if i in B:
    C += (i, )
print(C)

for i in range(0, len(atoms)):
  if atoms[i] == "Lithium":
    break;
  else:
    i = -1
print(atoms)

# Delete
'''
if i > 0:
  atoms = atoms[0:i] + atoms[i+2:]
print(atoms)
'''

# Update
newtuple = ('Oxygen', 8)
if i >= 0:
  atoms = atoms[0:i] + newtuple + atoms[i+2:]
else:
  atoms = atoms + newtuple

print(atoms)

# Assignment
student_record = ('Parker', 'Jim', 1980, "Math 550", 'C+', 'Cpsc 302', 'A+')
(fname, lname, year, cmin, gmin, cmax, gmax) = student_record
print(student_record)
print(fname, lname, year, cmin, gmin, cmax, gmax)
(a, b, c, d, e) = (1,2,3,4,5)
(f,g,h,i,j) = (a, b, c,d,e)
print(f,g,h,i,j)
# (f,g,h,i,j) = 2 ** (a, b, c,d,e)
# (f,g,h,i,j) = (2,2,2,2,2) ** (a, b, c,d,e)
# print(f,g,h,i,j)
print("C: ", C)
print(len(C))
print(max(C))
print(min(C))
print(A > B)
print(B > C)
print(A > C)
t1 = 1,2,3,"4", "5"
t2 = -1, 2, 4,5,7
print(t1>t2)

#LIST
list1 = [2,3,5,7,11,13,17,19]
list2 = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
list3 = ["hi", "ohio", "salut"]
list4 = []
print(list1)
print(list2)
print(list3)
print(list4)
print("list1[2:4]", list1[2:4])
list6 = list1 + [23,31]
print("list6", list6)
print("list1", list1)
list1[2] = 6
print("list1", list1)
list3[1:] = "bonjour"
print(list3)
list3[1:] = ["bonjour"]
print(list3)
list1[2] = [6,7,8]
print(list1)

list1 = [2,3,5,7,11,13,17,19]
print(list1)
# sum = 0

# for i in list1:
  # sum += i
# mean = sum / len(list1)
mean = sum(list1) / len(list1)
print("list1 mean: ", mean)

print(list2)
list2[0] = "Nitrogen"
print(list2)
list2[0] = ["Hydrogen", "Nitrogen"]
print(list2)
list2.insert(0, "Nitrogen")
print(list2)
list2.insert(len(list2), "Nitrogen")
print(list2)
list2.insert(-1, "Nitrogen")
print(list2)
list2.append("Carbon")
print(list2)
list2 += ["Oxygen"]
print(list2)
a = [1,2,3,4,5]
b = [6,7,8,9,10]
print("a",a)
print("b",b)
print("a+b", a + b)
print("a extend b ", a.extend(b))
print(a)
a.append(b)
print("a append b: ",a)
print(list2)
list2.remove("Nitrogen")
list2.remove("Nitrogen")

list2.remove("Nitrogen")
# list2.remove("Nitrogen")

print(list2)
print("index of Boron: ", list2.index("Boron"))
print(list2.pop())
list2 = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
print(list2)
list2.sort()
print(list2)
z = [["Hydrogen", 3],["Helium",2],["Lithium", 1],["Beryllium",4],["Boron",5],["Carbon", 6]]
print(z)
z.sort()
print(z)
print(z.reverse())
print(z)
q = [5,6,1,5,4,9,9,1,5,6,3]
print(5, q.count(5))

t = []
for i in range(0,10):
  t += [i*i]
print(t)

t2 = [i**2 for i in range(10)]
print(t2)
import random
t3 = [random.randint(0,100) for i in range(10)]
print(t3)
ss = [i.upper() for i in list2]
print(ss)
print(list2)
# if "Helium" in list2:
#   list2.remove("Helium")
# print(list2)

try:
  list2.remove("Helium")
except:
  print("can't find " + "Helium")
print(list2)

set1 = {1,3,5,7,9}
set2 = set(range(1,10))
print(set1)
print(set2)
print("set1 < set2 ", set1<set2)
print("set1 & set2 ", set1&set2)
print("set1 | set2 ", set1|set2)
print("set2 - set1 ", set2-set2)
set1.add(11)
print(set1)
set1.remove(11)
print(set1)
set1.add(12)
print(set1)
set1.discard(12)
print(set1)






