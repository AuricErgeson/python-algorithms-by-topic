import os

old_name = "./data_write.txt"
new_name = "./data_write2.txt"

os.remove(new_name)
os.rename(old_name, new_name)