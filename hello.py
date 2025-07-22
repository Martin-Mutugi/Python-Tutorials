# Step 1: Ask the user to input the first number
# We're using 'float()' to make sure our numbers can have decimals too. Fancy, right? ✨
num1 = float(input("Enter the first number: "))

# Step 2: Ask the user to input the second number
# Same trick here—using 'float()' for decimal magic! 🧙‍♂
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2

# Subtract the second number from the first (Negative vibes, but necessary! 😜) ➖
difference_result = num1 - num2

# Multiply the two numbers (More bang for your buck! 💥) ✖
product_result = num1 * num2
if num2 !=0:
    Division_result = num1/num2
else :
    Division_result="You can't divide any number by 0" 
#Finding the Modulus of the first and the second number
if num2 !=0:
    Modulus_result = num1%num2  
else :
    Modulus_result="You can't find the modulus of the number"     
#Division_result = num1/num2
# Divide the first number by the second (Be careful with zero here, no math disasters! 😅) ➗
# We'll assume the user is being responsible and not dividing by zero for✖
print(f"The sum is : {sum_result}")
print(f"The difference is : {difference_result}")
print(f"The product is : {product_result}")
print(f"The division is : {Division_result}")
print(f"The modulus is : {Modulus_result}")