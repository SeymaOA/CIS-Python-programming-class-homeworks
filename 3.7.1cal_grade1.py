#Calculates the overall grade for four equally weighted programming assignments,
# in which each assignment is graded out of 50 points.
# Hint: First calculate the percentage for each assignment (e.g., score / 50),
# then calculate the overall grade percentage (be sure to multiply the result by 100).
exam1_grade = float(input('Enter score on Exam 1 (out of 50): \n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 50):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 50):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 50):\n'))

overall_grade = (exam1_grade / 50 + exam2_grade / 50 + exam3_grade / 50 + exam4_grade / 50) / 4 * 100

print(f'Your overall grade is: {overall_grade}')