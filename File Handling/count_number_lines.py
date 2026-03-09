with open("./demo.txt","r") as fic:
    content = fic.read()
    print(content)


with open("./demo.txt","r") as fic:
    count = 0
    for line in fic:
        count +=1

print(f" \nThe number of lines in the file including blank space  are: {count}")


with open("./demo.txt","r") as fic:
    count = 0
    for line in fic:
        if line != "\n":
            count +=1

print(f" \nThe number of lines in the file without blank space  are: {count}")