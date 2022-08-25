# file = open("./day24/file.txt")
# content = file.read()
# print(content)
# file.close()

# with open("./day24/file.txt") as file:
#     content = file.read()
#     print(content)

# with open("./day24/file.txt",mode="a") as file:
#     file.write("\nBien ?")

    
# with open("./day24/file.txt",mode="a") as file:
#     file.write("\nBien ?")


# with open("./day24/file2.txt",mode="w") as file:
#     file.write("Nouveau FICHIIIIER")


with open("./day24/Input/Letters/starting_letter.txt",mode="r") as template:
    template_content = template.read()

with open("./day24/Input/Names/invited_names.txt",mode="r") as names:
    for name in names:
        name = name.strip()
        letter = template_content.replace("[name]",name)
        with open(f"./day24/Output/ReadyToSend/{name}.txt",mode="w") as result:
            result.write(letter)
        






