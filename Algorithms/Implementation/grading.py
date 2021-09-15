

def next_multiple(number):
    max_multiple = True
    start = 1
    while (max_multiple):
        if (start * 5) > number:
            max_multiple = False
        else:
            start += 1
    return start

# Function that rounds the students' grades
def solve(grades):
    new_grades = []
    for i in range(len(grades)):
        if grades[i] >= 38: 
            new_value = (next_multiple(grades[i]) * 5) - grades[i]
            if new_value < 3:
                new_grades.append(grades[i] + new_value)
                continue
        new_grades.append(grades[i])
    return new_grades

# Get data
n = int(input().strip())
grades = []
for grades_i in range(n):
   grades.append(int(input().strip()))

# Resolve the problem and show on the screen
result = solve(grades)
print ("\n".join(map(str, result)))