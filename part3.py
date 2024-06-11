temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])   #task 1 Extract the temperatures for the second week (7 days) of the month.
print(temperatures.index(100))
print(temperatures[23:])  #Task 2: Extract all the temperatures above 100.
temperatures_updated = (list(reversed(temperatures)))   #Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
print(temperatures_updated)
print(temperatures_updated[4:9])