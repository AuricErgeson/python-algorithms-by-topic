"""
Write a function to remove characters from a string starting from index 0 up to n and return a new string.
"""

strng = "pynative"


def slice_str (text:str,range:int):
    new_str = text[range:]
    print(new_str)
    

slice_str(strng,2)
