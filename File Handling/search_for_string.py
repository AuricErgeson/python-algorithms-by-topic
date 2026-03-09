def find_str(file_path, word):
    with open(file_path,"r") as file:

        for index, line in enumerate(file):

            if word in line:
                    print(f"The word '{word}' is in the file")
                    print(index)

find_str("./demo.txt","ye")