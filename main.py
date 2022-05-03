#Importing of other classes
import Assignment as assignment
import Grader as grader
import Output as output

#These are the values for the assignment

q1 = assignment.max([1,8,3])
q2 = assignment.length('Hello World')
q3 = assignment.palindrome('racecar')
q4 = assignment.closest([10,3,7,8,15],4)

#Our expected output for first question
with open('ExpectedOutputs.txt') as f:
    exp1 = f.readline()

#Expected output for second question
with open('ExpectedOutputs.txt' )as f:
    exp2 = f.readlines()[1]
#Expected output for third question
with open('ExpectedOutputs.txt')as f:
    exp3 = f.readlines()[2]

with open('ExpectedOutputs.txt')as f:
    exp4 = f.readlines()[3]



#Calls the Grader Class
a = grader.Grader(q1,q2,q3,q4,exp1,exp2,exp3,exp4,0)
grade = (a.checkMatching(q1,q2,q3,q4,exp1,exp2,exp3,exp4))

#Calls the Output Class
b = output.Output(grade)
final = (b.printGrade(grade))





