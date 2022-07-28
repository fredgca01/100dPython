# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, 
# you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. 
# The final version of the student_grades dictionary will be checked.

# This is the scoring criteria:
#     Scores 91 - 100: Grade = "Outstanding"
#     Scores 81 - 90: Grade = "Exceeds Expectations"
#     Scores 71 - 80: Grade = "Acceptable"
#     Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

def graduate(score):
    if score<=70:
        return "Fail"
    elif score<=80:
        return "Acceptable"
    elif score <=90:
        return "Exceeds Exceptations"
    else:
        return "Outstanding"

for key in student_scores:
    score = int(student_scores[key])
    result = graduate(score)
    student_grades[key]=result

print(student_scores)
print(student_grades)
