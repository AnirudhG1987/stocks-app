from json import JSONEncoder
import json
import random
from worksheet import numeric
from sympy import *
from fractions import Fraction
from decimal import Decimal

def rules():
    # Opening JSON file
    f = open('rules.json', )

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data:
        #print(i)
        for j in data[i]:
            #print(j)
            for k in data[i][j]:
                print(k, end=" ")
            print()
        print()
    # Closing file
    f.close()

def simplequestion(operands):
    f = open('fraction.json',)
    data = json.load(f)
    for _ in range(20):
        num1,num2  = fractionsGenerator(data)
        l_sym, op_sym, op_func = random.choice(operands)
        answer = latex(op_func(num1,num2))
        q_latex = latex(num1)+l_sym+latex(num2)+'= ?'
    return  q_latex, answer

def multistepsquestion(operands,steps):
    num1 = Rational(random.randint(2,10),random.randint(2,10))
    q_latex = latex(num1)
    answer = str(eval(str(num1)))
    while steps >0:
        l_sym, op_sym, op_func = random.choice(operands)
        num2 = Rational(random.randint(2,10),random.randint(2,10))
        if random.randint(0,1)==0:
            q_latex =q_latex+l_sym+latex(num2)
            answer = answer + op_sym + str(eval(str(num2)))
            #answer = answer + op_func(num1,num2)
            #q_latex = q_latex + question
        else:
            q_latex = latex(num2)+l_sym+q_latex
            answer = str(eval(str(num2))) + op_sym + answer
            #answer += str(op_func(eval(str(num2)),answer))
            #answer = answer + op_func(num2, num1)
        steps -=1
    q_latex += '= ?'
    #print (q_latex)
    #print (answer)
    frac_answer = Fraction(eval(answer)).limit_denominator(10000)
    answer = latex(Rational(frac_answer.numerator,frac_answer.denominator))
    return q_latex, answer


