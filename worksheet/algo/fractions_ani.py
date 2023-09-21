from random import randint
import json


def fraction_add_same_den(a,b,noOfQ):

    questionsList = {}
    for i in range(noOfQ):

        denominator = randint((a+b)/2,b)
        numerator1 = randint(a+1,denominator)
        numerator2 = randint(a+1, denominator)
        question = "%d/%d + %d/%d"%(numerator1,denominator,numerator2,denominator)
        solution = (numerator1+numerator2)
        answer = "%d/%d"%(solution,denominator)
        options={}

        for j in range(3):
           option = "%d/%d" % (randint(solution - 5, solution + 5), denominator)
           options[j] = option
        options[3] = answer
        #print options
        q = Question(question, answer, options, False,"")
        questionsList[i] = q
    f = open('out.txt', 'w')
    print >> f, json.dumps(questionsList,default=obj_dict,indent=4, sort_keys=True)
    f.close()


a = int(input("Enter a:"))
b = int(input("Enter b:"))

fraction_add_same_den(a,b,20)


