# CTI-110 
# P5HW1 - Test Average and Grades
# Omar Roman
# 7/5/2018
#

def main():
    # Get the grades for the 5 Tests.
    score1 = float (input ("Enter the score of the 1st test: "))
    score2 = float (input ("Enter the score of the 2nd test: "))
    score3 = float (input ("Enter the score of the 3rd test: "))
    score4 = float (input ("Enter the score of the 4th test: "))
    score5 = float (input ("Enter the score of the 5th test: "))

    printResults(score1, score2, score3, score4, score5)

    print ('\nThe average score is', calc_Average(score1, score2, score3, score4, score5))
    
def calc_Average(score1, score2, score3, score4, score5):

    # Calculate the average of the test scores.
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

def determine_Grade(score):

    # system uses 10-point grading scale
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def printResults(score1, score2, score3, score4, score5):
        print ( "Score\t\tLetter Grade" )
        print (str (score1) + "\t\t" + determine_Grade(score1), \
               str (score2) + "\t\t" + determine_Grade(score2), \
               str (score3) + "\t\t" + determine_Grade(score3), \
               str (score4) + "\t\t" + determine_Grade(score4), \
               str (score5) + "\t\t" + determine_Grade(score5), sep = "\n" )

main()
