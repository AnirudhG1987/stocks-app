from fractions import Fraction
from decimal import Decimal
from numbers import Integral,Number
import operator

NUMBER_TYPE = {
    'fraction': Fraction,
    'decimal': Decimal,
    'nnumber': Number,
    'integer':Integral
}

OPERATIONS = [
    ('+', '+',operator.add),
    ('-', '-', operator.sub),
    ('\\times', '*', operator.mul),
    ('\div','/', operator.truediv),
]

class Numeric:
    def generateNumeric(self,number_type,low,high):
        return NUMBER_TYPE[number_type](low,high)


#print(n.generateNumeric('fraction',4,5))