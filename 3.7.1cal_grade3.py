#Calculates the overall grade for a course with three equally weighted exams
# (graded out of 100 points) that account for 60% of the overall grade,
# and four equally weighted programming assignments (graded out of 50 points) that account for 40% of the overall grade.
# Hint: The overall grade can be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.
exam1_grade = float(input('Enter score on Exam 1 (out of 100): \n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 50):\n'))
exam5_grade = float(input('Enter score on Exam 5 (out of 50):\n'))
exam6_grade = float(input('Enter score on Exam 6 (out of 50):\n'))
exam7_grade = float(input('Enter score on Exam 7 (out of 50):\n'))

averageExamScore = (exam1_grade + exam2_grade + exam3_grade) / 3
averageProgScore = ((exam4_grade + exam5_grade + exam6_grade + exam7_grade) / 4 ) * 2
overall_grade = (averageExamScore * 0.6) + (averageProgScore * 0.4)


print(f'Your overall grade is: {overall_grade}')