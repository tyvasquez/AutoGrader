#Check the input matches the expected output and genereates
#a grade for each assignment

class Grader:
    def __init__(self,ans1,ans2,ans3,exp1,exp2,exp3,grade):
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.grade = 0

    def checkMatching(self,ans1,ann2,ans3,exp1,exp2,exp3):
        if self.ans1 == int(self.exp1):
            self.grade += 33

        if self.ans2 == int(self.exp2):
            self.grade =+ 33 +self.grade

        if str(self.ans3) == (self.exp3):
            self.grade =+ 34 +self.grade

        else:
            self.grade =+ 0 + self.grade
        return self.grade


