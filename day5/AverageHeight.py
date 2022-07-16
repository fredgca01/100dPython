# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. 
# You should try to replicate their functionality using what you have learnt about for loops.

student_heights = [180, 124, 165, 173, 189, 169, 146]
globalSum=0
count=0
for height in student_heights:
    globalSum+=int(height)
    count+=1
print(f"{count} {globalSum}")
average = globalSum/count
average = "{:.2f}".format(average)
print(average)

# alternate
average = sum(student_heights)/len(student_heights)
average = "{:.2f}".format(average)
print(f"Alternate {average}")