# Initial list of scores
scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]
# filtering the scores to only include scores that are above 60
passed = [score for score in scores if score > 60]
print(passed)
# output = [78, 88, 90, 62, 99, 70]

# creating rankings based on the initial scores list where anything >= 50 is Pass else it is Fail
rankings = ["Pass" if score >= 50 else "Fail" for score in scores]
print(rankings)
# output = ['Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass']

# List of student names
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
# Corresponding marks for each student
marks = [82, 48, 79, 65, 91]
# Combining the list of students with their corresponding marks using dictionary comprehension
# zip pairs each student with their mark
student_marks = {student: mark for student, mark in zip(students, marks)}
print(student_marks)
# output = {'Alice': 82, 'Bob': 48, 'Charlie': 79, 'Diana': 65, 'Eve': 91}


# creating a dictionary where only students who scored above 70 are displayed
over_70 = {student: mark for student, mark in zip(students, marks) if mark > 70}
print(over_70)
# output = {'Alice': 82, 'Charlie': 79, 'Eve': 91}

# creating rankings based on the initial marks list where anything >= 50 is Pass else it is Fail
grade_ranking = {student: "Pass" if mark >= 50 else "Fail" for student, mark in zip(students, marks)}
print(grade_ranking)
# output = {'Alice': 'Pass', 'Bob': 'Fail', 'Charlie': 'Pass', 'Diana': 'Pass', 'Eve': 'Pass'}

# A string
sentence = "Data science is fun and insightful"
# creating a list of words from the string using the split function
words = sentence.split()
print(words)
# output = ['Data', 'science', 'is', 'fun', 'and', 'insightful']

# creating a dictionary where we pair the words with their specific lengths
word_length = {word: len(word) for word in words}
print(word_length)
# output = {'Data': 4, 'science': 7, 'is': 2, 'fun': 3, 'and': 3, 'insightful': 10}
