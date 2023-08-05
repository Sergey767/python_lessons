import os

file = open('/Users/sergey_goryachev/Desktop/homeworkPython/lesson_004/lecture_snippets/05_builtin.py', 'r')
# current_directory = os.getcwd()
#
# # 👇️ /home/borislav/Desktop/bobbyhadz_python
# print(current_directory)
for line in file:
    print(line, end='')
file.close()




