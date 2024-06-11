submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
combined_students = submitted + attended


print(combined_students.count("Alice"))     #task 1 students who appear 2x on the combined list 
print(combined_students.count("Bob"))
print(combined_students.count("Charlie"))
print(combined_students.count("David"))
print(combined_students.count("Eve"))
print(combined_students.count("Frank"))

print(set(submitted) == set(attended))   #task 2 checking if lists are identical regardless of order

attended.remove("Eve")
attended.remove("Frank")

print(attended)  #Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.