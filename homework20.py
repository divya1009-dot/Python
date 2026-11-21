
empty_list = []
print(empty_list)
marks = [85, 72, 90, 66, 78]
print("Student Marks:", marks)
sam_marks = [10, 20, 30] * 2
print("Repeated Sample Marks:", sam_marks)
print("Number of marks:", len(marks))
print("First mark:", marks[0])
print("Last mark:", marks[-1])
first_three_marks = marks[0:3]
print("First three marks:", first_three_marks)
rev_marks = marks[::-1]
print("Reversed Marks:", rev_marks)
def match_marks(marlst):
    count = 0
    matched_marks = []
    for mark in marlst:
        martext = str(mark)
        if len(martext) > 1 and martext[0] == martext[-1]:
            count += 1
            matched_marks.append(mark)
    print("Marks with first and last digit same:", matched_marks)
    return count
same_count = match_marks([88, 72, 99, 65, 77])
print("Number of matching marks:", same_count)
total = 0
for mark in marks:
    total += mark
avr = total / len(marks)
print("Sum of marks:", total)
print("Average marks:", avr)
marks.sort()
print("Smallest mark is:", marks[0])
print("Largest mark is:", marks[-1])
print("")
print("===== STUDENT MARKS LIST ANALYZER =====")
print("Sorted Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", avr)
print("Lowest Mark:", marks[0])
print("Highest Mark:", marks[-1])
print("=======================================")