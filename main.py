import numpy as np
number_of_students = 13
w = np.ones(8)
# grades_vector = np.zeros(number_of_students)
# grades_vector[0] = 9.5
# grades_vector[1] = 10
# grades_vector[2] = 9.33
# grades_vector[3] = 9.33
# grades_vector[4] = 0
# grades_vector[5] = 9.5
# grades_vector[6] = 9.5
# grades_vector[7] = 9.33
# grades_vector[8] = 9.33
# grades_vector[9] = 9.33
# grades_vector[10] = 9.25
# grades_vector[11] = 9.25
# grades_vector[12] = 9.33
# grades_vector[13] = 9.33
# grades_vector[14] = 8.64

array = [
[10,	9.5,	9.5,	7.89,	8.80,	9.17,	120,	2],
[10,	10,	9.17,	7.75,	8.17,	9.00,	119,	1.5],
[10,	9.33,	9.43,	8.17,	8.67,	9.33,	114,	0],
[10,	9.33,	9,	9.75,	8.86,	9.25,	119.8,	2],
# [10,	0,	0,	5.88,	0.00,	0.00,	0,	0,	0],
[10,	9.5,	9.5,	7.89,	8.80,	9.17,	116.5,	0],
[10,	9.5,	9.5,	7.89,	8.80,	9.17,	120,	0],
[10,	9.33,	9.43,	8.17,	8.67,	9.33,	119,	2],
[10,	9.33,	9,	9.75,	8.86,	9.25,	120,	0],
[10,	9.33,	9.43,	8.17,	8.67,	9.33,	118.6,	2],
[10,	9.25,	9.6,	8.90,	9.00,	9.33,	120,	2.5],
[10,	9.25,	9.6,	8.90,	9.00,	9.33,	118.3,	2],
[10,	9.33,	9.2,	8.36,	8.67,	8.33,	119.5,	2],
[10,	9.33,	9.2,	8.36,	8.67,	8.33,	120,	1.5],
]
grades_vector = np.array(array)
grades_vector = grades_vector.T
for i in range(len(grades_vector)):
    for j in range(len(grades_vector[0])):
        grades_vector[i][j] /= np.max(grades_vector[i])
# grades_vector[6] /= 120
for i in range(len(grades_vector)):
    for j in range(len(grades_vector[0])):
        w[i] *= (1+np.abs(np.mean(grades_vector[i]) - grades_vector[i][j]))/(1+np.mean(grades_vector[i]))

w /= np.sum(w)
w[7] /= 500
w /= np.sum(w)
print(w)
# grades_vector = np.array(array)
# grades_vector = grades_vector.T
# for i in range(len(grades_vector)):
#     for j in range(len(grades_vector[0])):
#         grades_vector[i][j] /= np.max(grades_vector[i])
# grades_vector = grades_vector.T
# print(grades_vector)
# final_grades = np.zeros(number_of_students)
# for i in range(len(grades_vector)):
#     for j in range(len(grades_vector[0])):
#         final_grades[i] += (w[j] * grades_vector[i][j])
#     final_grades[i] *= 20
# for i in range(len(final_grades)):
#     final_grades[i] /= np.max(final_grades)
#     final_grades[i] *= 20
# for i in range(len(final_grades)):
#     print("%.2f" % final_grades[i])

# print(np.mean(final_grades))

