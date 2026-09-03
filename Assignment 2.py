# Program to find the largest number among three numbers

# Taking input from the user
num1, num2, num3 = map(float, input("Enter three numbers separated by spaces: ").split())

# Finding the largest number using the max() function
largestnum = max(num1, num2, num3)
print("The largest number among", num1, ",", num2, "and", num3, "is", largestnum)

# Another way to find the largest number using if-else statements
if (num1 >= num2) and (num1 >= num3):
    largestnum = num1
elif (num2 >= num1) and (num2 >= num3):
    largestnum = num2
else:
    largestnum = num3

print("The largest number among", num1, ",", num2, "and", num3, "is", largestnum)
