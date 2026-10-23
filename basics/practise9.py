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
