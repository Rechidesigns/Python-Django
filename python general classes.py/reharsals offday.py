# list = [23, 35, 576, 66, 677, 45]

# def mean(list):
#     total_figure = sum(list)
#     legnth = len(list)

#     combined = total_figure / legnth
#     return combined
# combined = (mean(list))
# print(combined)


marks = [55, 64, 75, 80, 65]

def exam_grades(marks):
    total_marks = sum(marks)
    number_of_courses = len(marks)
    average = total_marks / number_of_courses
    return average

average = exam_grades(marks)
print(average)

if average > 80:
    Grade = "A"
elif average > 60:
        Grade = "B"
elif average > 50:
            Grade = "C"
else:
    Grade = 'Fail'

print("your Grade is", Grade)
