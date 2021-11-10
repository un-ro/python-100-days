# Day 5: Highest Score

student_scores = input("Input a list of student scores ").split()

highest_score = 0

for n in range(0, len(student_scores)):
    if highest_score < int(student_scores[n]):
        highest_score = int(student_scores[n])

print(f"The highest score in the class is: {highest_score}")
