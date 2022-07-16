# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
#     The highest score in the class is: x

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
maxScore=student_scores[0]
for score in student_scores:
    if maxScore<score:
        maxScore=score

print(f"The highest score in the class is: {maxScore}")

# alternate
maxScore=max(student_scores)
print(f"The highest score in the class is: {maxScore}")