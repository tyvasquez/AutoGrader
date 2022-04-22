#Takes the grades from the grader class and generates a text file
# with the grades of each student

class Output:
    def __init__(self,grade):
        self.grade = grade

    def printGrade(self,grade):
        with open('Grades.txt' , 'w') as f:
            f.write('Student one scored ' + str(self.grade) + '% on the assignment \n')
