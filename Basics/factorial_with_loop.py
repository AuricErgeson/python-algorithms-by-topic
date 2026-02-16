"""
This exercise explores “Mathematical Accumulation.” 
A factorial (e.g., 5! = 5*4*3*2*1) requires you to maintain a running product across multiple iterations, which is a core pattern in scientific computing.
"""

i = 1
factorial = 1
number = 5

"""while i<= number:
    factorial = factorial*i
    i = i+1

print(factorial)
"""

for n in range ( 1, number+1):
    factorial = factorial*n

print(f"the factorial of {number} is {factorial}")

