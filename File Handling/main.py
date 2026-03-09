""""
Important parameters

r : Read(only read)
w:  Write(write new file)
a:  Append (overwrite)
x:  Read and write
r+: Read and write in the same file

read  : read (), readline(), readlines()
write : write ()
"""

f = open("./data.txt","r")
#print(f.read())
one_line = f.readline()
#print(one_line)
f.close()

print("====================================================================================")
"""
Best structure is to use with and we will not need anymore to write close
"""

with open("./data.txt","r") as f:
    content = f.read()
    print(content)

print("=====================================Writing===============================================")

with open("./data_write.txt","w") as f:
    f.write("My Name is : \n")
    f.write("Auric Ergeson Nitonde")

with open("./data_write.txt","r") as f:
    content = f.read()
    print(content)