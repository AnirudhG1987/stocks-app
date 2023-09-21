

from sympy import Rational, latex, Pow, root, Integer, symbols, Poly, I
import random
from sympy.abc import x

NUMBER_TYPE = ['fraction','decimal','number','exponent','surd',
               'complex']

OPERATIONS = [('**',''),('/', '\div'),('*', '\\times'),("+", "+"),("-", "-")]

def check_the_symbols(symbols_sample):
    for i in range(len(symbols_sample)-1):
        if symbols_sample[i][0]=='/' and symbols_sample[i+1][0]=='/':
            return True
    return False

def equation_array_creator(operations,no_of_steps):
    op_index = [i for i in range(len(OPERATIONS)) if OPERATIONS[i][0] in operations]
    symbols_sample = ['/','/']
    while check_the_symbols(symbols_sample):
        symbols_sample = [
            OPERATIONS[i] for i in random.choices(op_index,k= no_of_steps)
        ]
    equation_array = [symbols_sample[(i-1)//2][0] if i%2!=0 else "" for i in range(2*len(symbols_sample)+1)]
    equation_array_latex = [symbols_sample[(i - 1) // 2][1] if i % 2 != 0 else "" for i in range(2 * len(symbols_sample) + 1)]
    return equation_array, equation_array_latex

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
        numerator_1 = random.randint(denom_min-1,denominator_1-1)
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
    digits = random.choice(range(1,precision))
    float_num = round(decimal_1,digits)
    if float_num < 0:
        num_latex = '(' + latex(float_num) + ')'
    else:
        num_latex = latex(float_num)
    #num_value = str(eval(str(float_num)))

    return '{'+num_latex+'}',float_num #Float(decimal_1,precision)#, Float(decimal_2,precision)

def numberGenerator(json_data,zero_allowed = False):
    num_min = json_data['min']
    num_max = json_data['max']
    #print(json_data)
    number_1 = Integer(random.choice(range(num_min, num_max)))
    if number_1 ==0:
        if not zero_allowed:
            number_1 = Integer(random.choice(range(1,num_max)))
    if number_1 < 0:
        num_latex = '(' + latex(number_1) + ')'
    else:
        num_latex = latex(number_1)
    #num_value = str(eval(str(number_1)))
    #number_2 = random.randint(num_min, num_max)
    return '{'+num_latex+'}', number_1#,number_2

def polynomialGenerator(json_data):
    degree = json_data["degree"]
    min_coeff = json_data["min_coeff"]
    max_coeff = json_data["max_coeff"]
    const_term = json_data["const_term"]
    sym_list = symbols(json_data["variables"])
    expr = 0
    for i in range(1,degree+1):
        for sym in sym_list:
            expr = expr+random.randint(min_coeff,max_coeff)*sym**i
    if const_term:
        expr = expr + random.randint(min_coeff,max_coeff)
    # this is to avoid just a number. Make it an expression.
    if isinstance(expr, Integer):
        expr = expr + random.choice(sym_list)
    #print(expr)
    return '{'+latex(expr)+'}', Poly(expr)



def surdGenerator(json_data):
    num_min = json_data['min']
    num_max = json_data['max']
    number_1 = random.randint(num_min, num_max)
    if number_1 < 0:
        num_latex = '(' + latex(-root(abs(number_1),2)) + ')'
        num_value = -root(abs(number_1),2)
    else:
        num_latex = latex(root(number_1,2))
        num_value = root(number_1,2)
    #num_value = num_latex
    #number_2 = random.randint(num_min, num_max)
    #print(num_value,num_latex)
    return '{'+num_latex+'}', num_value #,number_2

def complexGenerator(json_data):
    num_min = json_data['min']
    num_max = json_data['max']
    number_1 = random.randint(num_min, num_max)
    number_2 = random.randint(num_min, num_max)
    if number_1 == 0 and number_2==0:
        number_1 = random.randint(num_min, num_max)
        number_2 = random.randint(num_min, num_max)
    complex = number_1 + I * number_2
    return '{ ('+latex(complex)+') }', complex #,number_2

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
    #num_value = str(eval(str(num_value)))
    #number_2 = random.randint(num_min, num_max)
    return num_latex, num_value#,number_2

#def getNumericParameters():


def numericGenerator(number_type,json_data):
    num_type= random.choice(number_type)
    #parameters
    #return fractionsGenerator(json_data[num_type])
    if "fraction" == num_type:
        return fractionGenerator(json_data[num_type])
    elif "decimal" == num_type:
        return decimalGenerator(json_data[num_type])
    elif "number" == num_type:
        return numberGenerator(json_data[num_type])
    elif "exponent" == num_type:
        return exponentGenerator(json_data[num_type])
    elif "surd" == num_type:
        return surdGenerator(json_data[num_type])
    elif "polynomial" == num_type:
        return polynomialGenerator(json_data[num_type])
    elif "complex" == num_type:
        return complexGenerator(json_data[num_type])



