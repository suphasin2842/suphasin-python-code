"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""
passing_grade = 50
def input_students(num_students):
    the_dic =[  {
                    'name':"suphasin", 
                    'score':[57,89,60] 
                },
                {
                    'name': "first",
                    'score': [90,100,87]
                }
            ]
    return the_dic

def calculate_averages(students):
    for student in students:
        sum_score = sum(student['score'])
        student['average'] = sum_score / len(student['score'])
        
    return students

def display_results(students):
    print("Student Details: ")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Average Score: {student['average']}")
        if student['average'] > passing_grade:
            print("Status: PASS")
        else:
            print("Status: FAIL")


students = input_students(2)
students = calculate_averages(students)
display_results(students)
    