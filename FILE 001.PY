"""colors = ["red" , "blue" , "green" , "purple"]
print((colors[0]),(colors[-1]))"""

"""name = "Alice"
age = 30
print(name , age)"""

"""n = input("eneter the interger")
n1 = int(n)
n2 = int(n + n)
n3 = int(n + n + n)
sum = n1 + n2 + n3
print(sum)"""

"""i = "cat "*3
print(i)"""

"""txt = 'The best things in life are free!'
if 'free' in  txt:
  print('Yes, free is present in the text.')"""

"""a = "Hello, World!"
print(len(a))"""

"""for x in "banana":
  print(x)"""

"""i = 10
while i > 0:
    print(i)
    i -= 1
    if i == 0:
        continue
        print("liftoff!")"""
    
"""for i in range(1,20):
  if i % 2 == 0:
    continue
  print(i)"""

"""i = 0
while True:
  n = int(input("enter a number: "))
  if n == 0:
    break
  i += n
print(i)"""

"""name = "Owais"
age = int(36)
colour =  "blue"
print(f"My name is {name} , I am {age} years old , my favourite colour is {colour}")"""

"""name = input("name ?")
age = int(input("age ?"))
colour =  input("colour ?")
print(f"My name is {name} , I am {age} years old , my favourite colour is {colour}")"""

"""a = 10
b = 5
temp = a
a = b
b = temp
print(a,b)"""

""""a = "ace"
b = 10
c = 5.5
d = True
print(f"a is {type(a)}, b is {type(b)},c is {type(c)}, d is {type(d)}")"""

"""x = int(input("enter num1"))
y = int(input("enter num2"))
print((x+y)**2)"""

"""min_bal = 1000
c_bal = int(input("enter current balance :"))
month_names = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
months = 0
while c_bal < min_bal:
  p_charge = c_bal * 5/100
  c_bal += p_charge
  month_name = month_names[months % 12]
  months += 1
  print(f"{month_name} months: updated balance: is {c_bal}")"""

"""for x in range(4,10):
  sqr = x ** 2
  print(sqr)"""

"""first_num = float(input("enter a number :"))
operator = input("enter operator :")
second_num = float(input("enter a number :"))
if operator == "+":
  solve = first_num + second_num
elif operator == "-":
  solve = first_num - second_num
elif operator == "*":
  solve = first_num * second_num
elif operator == "/":
  if second_num != 0:
    solve = first_num / second_num
  else:
    solve = "error : canot divide by zero"
else:
  solve = "invalid error"
print(solve)"""

"""num = int(input("enter a number"))
factorial = 1
i = 1 
while i <= num:
  factorial *= i
  i += 1
print(factorial)"""

"""num = int(input("enter a number"))
i = 1
even_numbers = []
odd_numbers = []

while i <= num:
    if i%2 == 0:
      even_numbers.append(f"{i}")
    else:
      odd_numbers.append(f"{i}")
    i += 1

print("Even numbers :" ,even_numbers)
print("Odd numbers :" ,odd_numbers)"""

"""num = int(input("enter number:"))
i = 0
for i in range(num):
  i += 1
  i *= num
  print(i)
  need to check"""

"""name = ""
while name != "yourname":
  print("first, type your name")
  name = input()
print("thankyou, now go !")"""

"""n = 0
while n < 11:
    print(n)
    n += 1"""

"""for i in range(1, 11):
    print(i)"""

"""numlist = [5,4,1,10,8,2]
sum = 0
for n in numlist:
    sum += n
print(sum)"""

#Generate the multiplication table of a number using a loop.
"""num = int(input("enter a number :"))
for i in range(0,num*11,num):
  print(i)"""

#Using while, keep asking the user for input until they type quit.
"""while True:
  q = input("enter the passcode:")
  if q == "code47":
    print("correct !")
    break
  elif q == "quit":
    print("exiting...")
    break
  else:
    print("incorrect passcode, try again...")"""

"""n1 = int(input("enter first number :"))
n2 = int(input("enter second number :"))
n3 = int(input("enter third number :"))
if n1 == n2 == n3:
  print(3*(n1+n2+n3))
else:
  print(n1+n2+n3)"""

"""n = int(input("enter a number :"))
found = False
for i in range(0,100):
  if n == i:
    print("number within range")
    found = True
    break
if not found:
    print("number not found")"""

"""list = []
tsk1 = ("enter the task :")
tsk1 = list.append"""

"""num = int(input("enter the number"))
if num <= 1:
    print("not prime number")
for i in range(2,int(num**0.5)+1):
   if num % i == 0:
      print("not prime number")
      break 
else:
    print("is prime number")"""

"""def greet(name):
  print(f"hello {name}")
greet("Alex")"""

"""def doubled(num1, num2):
  for n in range(num1,num2):
    print(n**2)
doubled(2, 5)"""

"""def factorial(num):
  factorial = 1
  i = 1
  while i <= num:
    factorial *= i
    i += 1
  print(factorial)
factorial(5)"""

"""def even_odd(num):
  if num % 2 == 0:
    print("even")
  else:
    print("odd")
even_odd(7)"""

"""def table(num):
  for i in range(1,11):
    print(num*i)
table(8)"""

"""import random
def guess():
  print("guess the number")
  num_random = random.randint(1,100)
  attempts = 0
  while True:
    num_guess = int(input("enter your number :"))
    attempts += 1
    if num_guess == num_random:
        print(f"correct, in {attempts} attempts")
    elif num_guess < num_random:
        print("low")
    else:
        print("high")
guess()"""

"""def reverse():
 word = input("enter word to reverse :")
 print(word[::-1])
reverse()"""

"""sentence = "this a a red car"
vowels = "aeiou"
vowel_count = 0
for v in sentence:
  if v in vowels:
   vowel_count += 1
print(f"{vowel_count} vowels")"""

"""text = "abcdef"
print(text[7:9])
print(text[::-1])
print(text[-1:-5])"""

"""num = [1,5,8,7,"ball",12,64,"apple",15,23,98,3,"house",5,1,7,64,7,5,15,12]"""



"""num = [1,5,8,7,12,64,15,23,98,3,5,1,7,64,7,5,15,12]
num.sort()
print(num)
num.sort(reverse=True)
print(num)"""

"""num2 = [7,15,"apple",5]
common = []
for items in num:
  if items in num2 and items not in common:
    common.append(items)
print(common)

specific = num.count(5)
print(specific)

occur = {}
for item in num:
  if item in occur:
    occur[item] += 1
  else:
    occur[item] = 1
print(occur)

print((num[:3]), (num[-3:]))

if len(num) == 0:
  print("list is empty !")
else:
  print(f"{len(num)} items")

total = sum(num)
avg = total/len(num)
print(total , avg)

duplicates = []
for items in num:
  if num.count(items) > 1 and items not in duplicates:
    duplicates.append(items)
print(duplicates)

print(min(num))

print(max(num))

num.reverse()
print(num)"""



"""term = input("enter anything !")
num = "0123456789"
letters = "abcdefghijklmnopqrstvuxyz"
if term.isdigit():
  print("its a number")
elif term.isalpha():
  print("its a word")
else:
  print("its a bird, its a plane , i dont know!")"""

"""todolist = []
print("Welcome to TO-DO-LIST APP")
print("What you want to do ?")
op1 = "1.Add a task"
op2 = "2.Delete a task"
op3 = "3.Update a task"
op4 = "4.View list of tasks"
op5 = "5.Exit app"

print(op1)
print(op2)
print(op3)
print(op4)
print(op5)

option = int(input("Choose an option :"))
if option == 1:
  task = input("enter the task you want to add :")
  todolist.append(task)
  with open(r"D:\MY LIST L1.TXT", "a") as file:
    file.write(task + "\n")
elif option == 3:
  del_task = input("enter task to delete")
elif option == 4: 
  with open(r"D:\MY LIST L1.TXT", "r") as file:
    tasks = file.readlines()
    if tasks:
      print("Your To-Do List:")
      for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")
    else:
      print("no task found !")
else:
  print("goodbye")


elif option == 2:
  task = input("enter the task you want to delete :")
  todolist.pop(task)
elif option == 3:
  option = todolist.replace
elif option == 4:  
  print(todolist)
else: 
  print("goodbye")

Def cart_add
Cart = []
While cart.index <= 5
 Add_item = input("enter the item name")
 cart.append(add_item)
 Print(f"{add_item} has been added to your cart")
 If Add_item = 5:
Print("cart is already full")

Def cart_remove
Cart_remove = Cart.pop[index]
If Cart_remove not in cart:
 Print("item not found in cart")
Print(cart)

Def cart_view
Print(cart)

Def cart_clear
Cart.clear
Print(cart)"""

student_info = {"Emily Jackson":"B","Nathan Brooks":"C","Sarah Mitchell":"A","Oliver Harris":"D","Chloe Thompson":"F"}
student_info["Peter Parker"] = "A"
student_info.pop('Sarah Mitchell')
print(student_info)

    
