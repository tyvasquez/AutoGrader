#Check the input matches the expected output and genereates
#a grade for each assignment

class Grader:
    def __init__(self,ans1,ans2,ans3,ans4,exp1,exp2,exp3,exp4,grade):
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4
        self.grade = 0

    def checkMatching(self,ans1,ann2,ans3,ans4,exp1,exp2,exp3,exp4):
        '''
        # Takes in the 3 answers from the assignment and the 3 expected outputs from the text file.
        # tests if the values are equal to each other and if so adds points to the total grade
        :param ans1:
        :param ann2:
        :param ans3:
        :param exp1:
        :param exp2:
        :param exp3:
        :return:
        '''
        if self.ans1 == int(self.exp1):
            self.grade += 25

        if self.ans2 == int(self.exp2):
            self.grade =+ 25 +self.grade

        if str(self.ans3) == (self.exp3):
            self.grade =+ 25 +self.grade

        if str(self.ans4) == (self.exp4):
            self.grade=+ 25 +self.grade

        else:
            self.grade =+ 0 + self.grade
        return self.grade