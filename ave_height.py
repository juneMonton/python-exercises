# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height=0
for height in student_heights:
  total_height+=height
print(f"total height = {total_height}")

num_student=0
for student in student_heights:
  num_student+=1
print(f"number of students = {num_student}")
print (f"average height = {round(total_height/num_student)}")