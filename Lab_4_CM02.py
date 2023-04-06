### Q 1 ###

n = int(input("Enter a number: "))
sum = 0
for i in range(2, n+1, 2):
    sum += i
    print(i, end=' ')
print("\nSum of even numbers up to", n, "is", sum)



### Q 2 ###

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1, 2):
    sum += i
print("Sum of odd numbers up to", n, "is", sum)



### Q 3 ###

x = int(input("Enter a number: "))
print("Multiplication Table of", x)
for i in range(1, 11):
    print(i, "x", x, "=", i*x)



### Q 4 ###

total = 0
count = 0
num = 0

while True:
    num = int(input("Enter a positive number (-1 to exit): "))
    if num == -1:
        break
    total += num
    count += 1

if count == 0:
    print("No positive numbers entered.")
else:
    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)



### Q 5 ###

max_num = float('-inf')
min_num = float('inf')
num = 0

while True:
    num = int(input("Enter a positive number (-1 to exit): "))
    if num == -1:
        break
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

if max_num == float('-inf') or min_num == float('inf'):
    print("No positive numbers entered.")
else:
    print("Maximum number entered:", max_num)
    print("Minimum number entered:", min_num)



### Q 6 ###

total = 0
num = 0

while True:
    num = int(input("Enter a number (-1 to exit): "))
    if num == -1:
        break
    if num % 2 == 0:
        continue
    total += num

print("Sum of odd numbers:", total)



### Q 7 ###

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

count = 0
total = 0

for num in range(low, high+1):
    if num % 2 == 0:
        count += 1
        total += num

print("Sum of even numbers between", low, "and", high, "is", total)
print("Total even numbers between", low, "and", high, "is", count)



### Q 8 ###

for num in range(1, 101):
    if num % 3 == 0 or num % 5 == 0:
        continue
    print(num)



### Q 9 ###

results = []

for i in range(10):
    num = int(input("Enter result for student " + str(i+1) + " (1 = pass, otherwise = fail): "))
    if num == 1:
        results.append("pass")
    else:
        results.append("fail")

print(results)



### Q 10 ###

residents = 2000
for year in range(2016, 2021):
    residents *= 1.03
    print("The number in " + str(year) + " = " + str(round(residents, 2)))
