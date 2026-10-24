#Task: Student Grade Management System

#Write a Python program using Object-Oriented Programming (OOP) to collect and calculate student marks.
#Your program should:
#Create a class named student.
#Include a method get_info() to accept the student's name, ID, and marks for 3 subjects via user input.
#Include a method cal_total() to calculate the total sum of the marks.
#Include a method cal_average() to calculate the average of the entered marks.
#Include a method display() to print the student's name, ID,
# individual marks for all three subjects, the total mark, and the average mark.

class student:
    def get_info(self):
        self.student_name = input('Enter student name: ').strip()
        self.student_id = int(input('Enter student id: ').strip())
        self.student_mark = []
        for i in range(3):
            self.students = float(input(f'Enter your {i+1} mark: ').strip())
            self.student_mark.append(self.students)

    def cal_total(self):
        self.total = sum(self.student_mark)
    def cal_average(self):
        self.average= self.total/len(self.student_mark)
    def display(self):
        print(f'Student name: {self.student_name}')
        print(f'Student Id: {self.student_id}')
        print(f'Student mark for first subject: {self.student_mark[0]}')
        print(f'Student mark for second subject: {self.student_mark[1]}')
        print(f'Student mark for third subject: {self.student_mark[-1]}')
        print(f'Total Mark: {self.total}')
        print(f'Average Mark: {self.average}')
s1= student()
s1.get_info()
s1.cal_total()
s1.cal_average()
s1.display()
