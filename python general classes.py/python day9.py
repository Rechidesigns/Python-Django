# ### class work

# ## write a prohram to calculate the mean, median, mode,
# #  standard deviation and veeriance of a given array of students ages. 
# # log the report to a text file after evry calculation.


# ######## mean

# # def calculate_mean(students_age):
# #     total_age = sum(students_age)
# #     number_of_students = len(students_age)
# #     mean_answer = total_age/number_of_students
# #     return mean_answer


# # students_age = [25, 31, 27, 18, 22]
# # mean_answer = calculate_mean(students_age)
# # print(mean_answer)

# #### mean2

# def mean(arr):
#     return sum(arr)/len(arr)
# test_arr = [29, 17, 28, 6, 14, 7, 4, 27, 21, 15, 10, 16, 24, 26, 3, 11, 13, 8,

# 23, 9, 0, 22, 12, 2, 18, 19, 5, 1, 20, 25]

# mean(test_arr)

# def median(students_age):

#     """Return the median (middle value) of numeric data.
#     When the number of data points is odd, return the middle data point.
#     When the number of data points is even, the median is interpolated by
#     taking the average of the two middle values:
# """
#     sorted_data = sorted(test_arr)
#     n = len(sorted_data)
#     if n == 0:
#         return "no median for empty dataset"
#     if n%2 == 1: #check if the total num of elements in array is odd
#         return sorted_data[n//2]
#     else: #check if it is even
#         i = n//2
#     return (sorted_data[i - 1] + sorted_data[i])/2
# sorted_data = median(test_arr)
# print(sorted_data)




###############################################

   ## correctiion

  


# #### standard deviation
# def std_dev(arr):
#     mean_ = mean(arr)
#     numerator = sum([(x-mean_)**2 for x in arr])
#     standard_dev = (numerator/len(arr)) ** 0.5
#     return standard_dev
# std_dev(test_arr)







# with open("reportdata.txt", "w") as file:
#     fie.write(str(mean_answer))
#     file.write(str(sorted_data))



