### Q 1 ###

n = eval(input("Enter a value: "))

if n == 0:
    print("Zero value")
elif n > 0 or n < 0:
    print("Nonzero value")



### Q 2 ###

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))

if a > b:
    print(a, "is the largest number.")
else:
    print(b, "is the largest number.")



### Q 3 ###

num = eval(input("Enter the number: "))

if num < 0:
    print("The number is negative")
else:
    print("The number is positive")



### Q 4 ###

char = input("Enter a character: ")

if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")



### Q 5 ###

grade = eval(input("Enter the student's grade: "))

if grade >= 90:
    print("Excellent performance")
elif grade >= 80:
    print("Very good performance")
elif grade >= 70:
    print("Good performance")
elif grade >= 60:
    print("Average performance")
else:
    print("Poor performance")



### Q 6 ###

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))

if a >= b and a >= c:
    print(a, "is the largest number.")
elif b >= a and b >= c:
    print(b, "is the largest number.")
else:
    print(c, "is the largest number.")



### Q 7 ###

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))

if a <= b and a <= c:
    print(a, "is the smallest number.")
elif b <= a and b <= c:
    print(b, "is the smallest number.")
else:
    print(c, "is the smallest number.")



### Q 8 ###

num = int(input("Enter a number: "))

if num % 2 == 0:
    if num < 0:
        print(num, "is negative and even.")
    else:
        print(num, "is positive and even.")
else:
    if num < 0:
        print(num, "is negative and odd.")
    else:
        print(num, "is positive and odd.")



### Q 9 ###

marital_status = input("Enter marital status: ")
gender = input("Enter gender: ")
age = int(input("Enter age: "))

if marital_status == "married":
    print("The driver is insured.")
elif gender == "Male" and age > 30:
    print("The driver is insured.")
elif gender == "Female" and age > 25:
    print("The driver is insured.")
else:
    print("The driver is not insured.")



### Q 10 ###

try:
    marital_status = input("Enter marital status: ")
    gender = input("Enter gender: ")
    age = input("Enter age: ")
    age = int(age)
    
    if marital_status == "married":
        print("The driver is insured.")
    elif gender == "Male" and age > 30:
        print("The driver is insured.")
    elif gender == "Female" and age > 25:
        print("The driver is insured.")
    else:
        print("The driver is not insured.")

except ValueError:
    print("Age must be integer")

finally:
    print("The end")