"""
Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
"""

def cumul_sum(the_range):
    pr_num =0
    for i in range(the_range):
     
        print(f"Current Number {i} Previous Number {pr_num} sum {i+pr_num}")
        pr_num = i
    


cumul_sum(10)