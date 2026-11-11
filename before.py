
# Original program to calculate average marks

marks = input("Enter marks separated by spaces: ")
marks = marks.split()

total = 0

for mark in marks:
    total = total + int(mark)

average = total / len(marks)

print("Average marks:", average)
