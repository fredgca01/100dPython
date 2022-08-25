file = open("./day24/file.txt")
content = file.read()
print(content)
file.close()

with open("./day24/file.txt") as file:
    content = file.read()
    print(content)

with open("./day24/file.txt",mode="a") as file:
    file.write("\nBien ?")

    
with open("./day24/file.txt",mode="a") as file:
    file.write("\nBien ?")


with open("./day24/file2.txt",mode="w") as file:
    file.write("Nouveau FICHIIIIER")