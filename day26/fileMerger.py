#You are going to create a list called result which contains the numbers 
# that are common in both files. 

with open("./day26/file1.txt",mode="r") as file1:
    with open("./day26/file2.txt",mode="r") as file2:
        data = file2.readlines()
        merged = [int(number.strip()) for number in file1.readlines() if number in data]
        print(merged)
