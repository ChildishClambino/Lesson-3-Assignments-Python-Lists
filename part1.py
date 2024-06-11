grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)    #task 1 sort list in descending order
print(grades)

avg_grade = sum(grades) / len(grades)   #task 2 calculate the avg. grade and display it
print("the average grade is:", avg_grade)

grades[7] = "Failed"       # task 3 replace the values under 80 with "Failed3w2"
grades[8] = "Failed"
grades[9] = "Failed"
print(grades)