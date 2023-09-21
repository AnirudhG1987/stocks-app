import json
from fractions import Fraction
from random import random

from sympy import *

from worksheet import numeric


# other stuff

def something():
    x,y,z = symbols('x y z')
    init_printing(use_latex=True)
    #print(Rational(6,5)+Rational(3,4))
    init_printing()
    #print(latex(Rational(6,5)))
    #print(latex(Integral(8*x**Rational(6, 5) - 7*x**Rational(3, 2),x)))

def pdf_pdfbytearray():
    file = open('code.txt', 'wb')
    for line in open('sample_test.pdf', 'rb').readlines():
        file.write(line)
    file.close()

def pdfbytearray_pdf():
    file = open('new.pdf', 'wb')
    for line in open('code.txt', 'rb').readlines():
        file.write(line)
    file.close()

#pdf_pdfbytearray()
#pdfbytearray_pdf()
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

def simplequestion(operands,data,no_of_ques):
    tex_ques = ""
    tex_ans = ""

    for i in range(no_of_ques):
        num1, num2 = numeric.fractionsGenerator(data)
        l_sym, op_sym, op_func = random.choice(operands)
        ans = latex(op_func(num1, num2))
        ques = latex(num1) + l_sym + latex(num2) + '= ?'
        tex_ques = tex_ques + "\\item $\\displaystyle " + str(ques) + " $ \\" + "\n"
        tex_ans = tex_ans + "\\item $\\displaystyle " + str(ans) + " $ \\" + "\n"

    return  tex_ques, tex_ans


f = open('../../static/json/grade5.json', )
data = json.load(f)
chapter_name = "Numbers"
for topic_name in data["Chapters"][chapter_name]:
    for difficulty in data["Chapters"][chapter_name][topic_name]:
        print(data["Chapters"][chapter_name][topic_name][difficulty])




def multistepquestion(number_type, operands,data,no_of_ques,steps):
    tex_ques = ""
    tex_ans = ""

    for i in range(no_of_ques):
        ques,ans = numeric.numericGenerator(number_type,data)
        ans_value = eval(ans)
        for i in range(steps):
            op_sym = random.choice(operands)
            l_sym = numeric.OPERATIONS[op_sym]
            if l_sym == '-':
                temp_latex = num2_latex
                temp_value = num2_value
                if eval(str(ans)) > num2_value:
                    num2_latex = ques
                    num2_value = ans
                    ques = temp_latex
                    ans = temp_value
            elif l_sym == '/':
                num2_latex, num2_value = numeric.numericGenerator(number_type, data)
            else:
                num2_latex,num2_value = numeric.numericGenerator(number_type,data)
            if l_sym == '-':
                temp_latex = num2_latex
                temp_value = num2_value
                if eval(str(ans)) > num2_value:
                    num2_latex = ques
                    num2_value = ans
                    ques = temp_latex
                    ans = temp_value
            elif l_sym == '/':
                pass
            ques = ques + l_sym + num2_latex
            ans = ans + op_sym + num2_value  # str(eval(str(num2)))
            #if random.randint(0,1)==0:
                #ques =ques +l_sym+num2_latex
                #ans = ans + op_sym + num2_value #str(eval(str(num2)))

            #else:
            #    ques = num2_latex + l_sym + ques
            #    ans = num2_value + op_sym + ans #str(eval(str(num2)))
        ques += '= ?'
        if ["fraction","surd"] not in number_type:
            ans = latex(round(eval(str(ans)), 3))
        elif "surd" not in number_type:
            frac_answer = Fraction(eval(ans)).limit_denominator(10000)
            ans = latex(Rational(frac_answer.numerator,frac_answer.denominator)) + '{ or }' + latex(round(eval(str(frac_answer)),3))

        tex_ques = tex_ques + "\\item $\\displaystyle " + str(ques) + " $ \\" + "\n"
        tex_ans = tex_ans + "\\item $\\displaystyle " + str(ans) + " $ \\" + "\n"

    return tex_ques, tex_ans


def fractionGenerator(json_data):
    denom_min = json_data['min']
    denom_max = json_data['max']
    denominator_1 = random.randint(denom_min, denom_max)
    #if frac_json["samedenominator"]:
    #    denominator_2 = denominator_1
    #else:
    #    denominator_2 = random.randint(denom_min, denom_max)
    if "improper" in json_data["frac_type"]:
        numerator_1 = random.randint(denominator_1+1, denom_max+1)
    #   numerator_2 = random.randint(denominator_2+1, denom_max+1)
    else:
        numerator_1 = random.randint(denom_min-1,denominator_1)
    #    numerator_2 = random.randint(denom_min-1,denominator_2)
    rational_num = Rational(numerator_1,denominator_1)
    if rational_num < 0:
        num_latex = '(' + latex(rational_num) + ')'
    else:
        num_latex = latex(rational_num)
    #num_value = str(eval(str(rational_num)))

    return  '{'+num_latex+'}', rational_num
    #Rational(numerator_1,denominator_1)#, Rational(numerator_2,denominator_2)

def decimalGenerator(json_data):
    precision = json_data['precision']
    deci_min = json_data['min']
    deci_max = json_data['max']
    decimal_1 = random.uniform(deci_min, deci_max)
    #decimal_2 = random.uniform(deci_min, deci_max)
    float_num = Float(decimal_1,precision)
    if float_num < 0:
        num_latex = '(' + latex(float_num) + ')'
    else:
        num_latex = latex(float_num)
    num_value = str(eval(str(float_num)))

    return '{'+num_latex+'}',num_value #Float(decimal_1,precision)#, Float(decimal_2,precision)

def numberGenerator(json_data):
    num_min = json_data['min']
    num_max = json_data['max']
    number_1 = random.randint(num_min, num_max)
    if number_1 < 0:
        num_latex = '(' + latex(number_1) + ')'
    else:
        num_latex = latex(number_1)
    #num_value = str(eval(str(number_1)))
    #number_2 = random.randint(num_min, num_max)
    return '{'+num_latex+'}', number_1#,number_2

def surdGenerator(json_data):
    num_min = json_data['min']
    num_max = json_data['max']
    number_1 = random.randint(num_min, num_max)
    if number_1 < 0:
        num_latex = '(' + latex(root(abs(number_1),2)) + ')'
    else:
        num_latex = latex(root(number_1,2))
    num_value = num_latex
    #number_2 = random.randint(num_min, num_max)
    return '{'+num_latex+'}', num_value #,number_2

def exponentGenerator(json_data):
    base_min = json_data['base_min']
    base_max = json_data['base_max']
    exp_min = json_data['exp_min']
    exp_max = json_data['exp_max']
    base = random.randint(base_min, base_max)
    expon = random.randint(exp_min, exp_max)
    num_value = Pow(base,expon)
    if num_value < 0:
        num_latex = '(' + str(base) + '^{' +str(expon) + '})'
    else:
        num_latex = str(base) + '^{' +str(expon) + '}'
    num_value = str(eval(str(num_value)))
    #number_2 = random.randint(num_min, num_max)
    return num_latex, str(num_value)#,number_2

