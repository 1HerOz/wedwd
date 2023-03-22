### Q1 ###
h = eval(input("Enter the height of rectangle: "))
w = eval(input("Enter the width of rectangle: "))

# Calculate the area and perimeter
area = h * w
perimeter = 2 * (h + w)

# Print the area and perimeter
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)



### Q 2 ###
# Prompt the user to input the principal amount, rate of interest, and number of years
PA = eval(input("Enter the Principal Amount: "))
RI = eval(input("Enter the Rate of Interest: "))
NY = eval(input("Enter the Number of years: "))

# Calculate the simple interest
SI = (PA * RI * NY) / 100

# Print the simple interest
print("The Simple Interest of loan is: ", SI)

### Q 3 ###
# Prompt the user to input two integers
numi1 = int(input("Enter the first number int: "))
numi2 = int(input("Enter the second number int: "))

# Calculate the sum
sum = (numi1 + numi2)

# Print the sum
print("The sum is:", sum)



### Q 4 ###
# Prompt the user to input three floats
numf1 = float(input("Enter the first number float: "))
numf2 = float(input("Enter the second number float: "))
numf3 = float(input("Enter the third number float3: "))

# Calculate the average
average = (numf1 + numf2 + numf3) / 3

# Print the average
print("The average is:", average)



### Q 5 ###
L=[4,7,2,8]
# Print the square of the third element
print(L[2]**2)



### Q 6 ###
# Concatenate two lists L1 and L2 into L3
L1 = ['Red', 'Blue', 'Green']
L2 = ['Black', 'White', 'Yellow']
L3 = L1 + L2

# Add the color Brown to L3 and sort L3
L3.append('Brown')
L3.sort()

# Print L3
print(L3)



### Q 7 ###
L = ["Python", "Java", "C ++", "Javascript"]

# Swap the first and last elements
L[0], L[-1] = L[-1], L[0]

print(L)  # Output: ["Javascript", "Java", "C ++", "Python"]



### Q 8 ###
fruits = {
    "Apple": 34,
    "Banana": 12,
    "Orange": 28,
    "Peach": 40
}
print(fruits) # Output: ['Apple': 34, 'Banana': 12, 'Orange': 28, 'Peach': 40]

# delete: ["Banana": 12]
del fruits["Banana"]
print(fruits) # Output: ['Apple': 34, 'Orange': 28, 'Peach': 40]

