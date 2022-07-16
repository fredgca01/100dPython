# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# This is to try and simulate the coordinates on a real map.
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical column number and the second digit is the horizontal row number

row1=['⬜️', '⬜️', '⬜️']
row2=['⬜️', '⬜️', '⬜️']
row3=['⬜️', '⬜️', '⬜️']
map = [row1,row2,row3]
print(f" {row1} \n {row2} \n {row3}")
coord = input("Where do you want to hide the treasure ? (first digit is the vertical column number and the second digit is the horizontal row number): ")
coordXY = coord.split(",")
row = map[int(coordXY[1])-1]
row[int(coordXY[0])-1]="X"

print(f" {row1} \n {row2} \n {row3}")

