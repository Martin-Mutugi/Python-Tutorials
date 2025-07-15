num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

sum_result = num1 + num2

difference_result = num1 - num2

product_result = num1 * num2

if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Undefined (can't divide by zero!)"

if num2 !=0:
    module_result=num1 % num2
else:
    module_result= "undefined (can't divide by zero!)"
    
print("\n Here are your results! ")
print(f" Sum: {sum_result}")
print(f" Difference: {difference_result}")
print(f" Product: {product_result}")
print(f" Quotient: {quotient_result}")
print(f" Module: {module_result}")
