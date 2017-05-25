print("What would you like to know?")
input()

import random
def getAnswer(answerNumber):
     if answerNumber == 1:
           return 'That will never happen'
       elif answerNumber == 2:
           return 'Try again later'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Maybe'
       elif answerNumber == 5:
           return 'Im tired of your questions, come back later'
       elif answerNumber == 6:
           return 'Yes'
       elif answerNumber == 7:
           return 'No'
       elif answerNumber == 8:
           return 'Not today'
       elif answerNumber == 9:
           return 'Thats a stupid question'

 r = random.randint(1, 9)
 fortune = getAnswer(random_int)
 print(fortune)
