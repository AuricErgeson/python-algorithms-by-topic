"""
Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, 
return their product; otherwise, return their sum.
"""

def product_or_sum(num1,num2):
    result = 0
    if num1 * num2 <= 1000:
        result = num1*num2
    else:
        result = num1+num2
    
    return result

print(product_or_sum(40,30))