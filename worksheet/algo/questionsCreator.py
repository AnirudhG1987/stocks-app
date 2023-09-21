import copy
from fractions import Fraction
from sympy.parsing.sympy_parser import parse_expr
from sympy import Poly, Rational, Integer, gcd, lcm, reduce_inequalities, solve_univariate_inequality
import numpy as np

from sympy import Symbol, simplify, latex, Add, symbols, expand, diff, \
    Eq, solve, SeqFormula, factorint, sqrt, randprime, Point, Line, Segment
from worksheet.algo.numeric import equation_array_creator,numericGenerator
from sympy.abc import x,y,n
import random


def makeFormatting(s):
    return "{:,}".format(s)


def latexQuestionAnsPackager(question,ans,dollar=True):
    if dollar:
        question = "\\item $\\displaystyle " + question + " $ \\" + " \n"
        ans = "\\item $\\displaystyle " + ans + " $ \\" + " \n"
    else:
        question = "\\item " + question  + " \n"
        ans = "\\item " + ans + " \n"
    return question, ans


class ShapesQuestion():

    def __init__(self):
        self.getShapeDict = {
            "Circle": self.getCircleDict,
            "Square": self.getSquareDict,
            "Rectangle":self.getRectangleDict,
            "Cuboid": self.getCuboidDict,
            "Cube": self.getCubeDict,
            "Cylinder": self.getCylinderDict,
            "Sphere": self.getSphereDict,
            # "Trapezoid": ["Surface Area", "Volume"],
            # "Prism": ["Surface Area", "Volume"],
            "Triangle": self.getTriangleDict,
            "Trapezium": self.getTrapeziumDict,

        }

        self.getShapeBlanks = {
            "Circle":2,
            "Square":2,
            "Rectangle":2,
            "Cuboid":["Surface Area", "Volume"],
            "Cube":2,
            "Cylinder": ["Total Surface Area","Lateral Surface Area", "Volume"],
            "Sphere": 2,
            "HemiSphere": 2,
            #"Trapezoid": ["Surface Area", "Volume"],
            #"Prism": ["Surface Area", "Volume"],
            "Triangle":1,
            "Trapezium": 1,

        }

    def getSquareDict(self,noofQuestions):
        square_dict_list = []
        side_list = random.sample(range(1,100),k=noofQuestions)
        side_list.sort()
        for side in side_list:
            square_dict = {}
            square_dict["Side"]= side
            square_dict["Area"] = makeFormatting(round(square_dict["Side"]**2,2))
            square_dict["Perimeter"] = makeFormatting(round(4*square_dict["Side"],2))
            square_dict["Side"] = str(side)
            square_dict_list.append(square_dict)
        return square_dict_list

    def getCubeDict(self,noofQuestions):
        cube_dict_list = []
        side_list = random.sample(range(1,50),k=noofQuestions)
        side_list.sort()
        for side in side_list:
            cube_dict = {}
            cube_dict["Side"]= side
            cube_dict["Surface Area"] = makeFormatting(round(6*cube_dict["Side"]**2,2))
            cube_dict["Volume"] = makeFormatting(round(cube_dict["Side"]**3,2))
            cube_dict["Side"] = str(side)
            cube_dict_list.append(cube_dict)
        return cube_dict_list

    def getTriangleDict(self,noofQuestions):
        tri_dict_list = []
        base_list = random.sample(range(1,100),k=noofQuestions)
        height_list = random.sample(range(1, 100), k=noofQuestions)

        for i in  range(noofQuestions):
            tri_dict = {}
            tri_dict["Base"]= base_list[i]
            tri_dict["Height"] = height_list[i]
            tri_dict["Area"] = makeFormatting(round(0.5*tri_dict["Base"]*tri_dict["Base"],2))
            tri_dict["Base"] = str(base_list[i])
            tri_dict["Height"] = str(height_list[i])
            tri_dict_list.append(tri_dict)
        return tri_dict_list

    def getRectangleDict(self,noofQuestions):
        rec_dict_list = []
        a_list = random.sample(range(1,100),k=noofQuestions)
        b_list = random.sample(range(1, 100), k=noofQuestions)
        for i in  range(noofQuestions):
            rec_dict = {}
            rec_dict["a"]= a_list[i]
            rec_dict["b"]= b_list[i]
            rec_dict["Area"] = makeFormatting(round(rec_dict["a"]*rec_dict["b"],2))
            rec_dict["Perimeter"] = makeFormatting(round(2*(rec_dict["a"]+rec_dict["b"]),2))
            rec_dict["a"] = str(rec_dict["a"])
            rec_dict["b"] = str(rec_dict["b"])
            rec_dict_list.append(rec_dict)
        return rec_dict_list

    def getTrapeziumDict(self,noofQuestions):
        trap_dict_list = []
        a_list = random.sample(range(1,100),k=noofQuestions)
        b_list = random.sample(range(1, 100), k=noofQuestions)
        h_list = random.sample(range(1, 100), k=noofQuestions)

        for i in  range(noofQuestions):
            trap_dict = {}
            trap_dict["a"]= a_list[i]
            trap_dict["b"]= b_list[i]
            trap_dict["h"] = h_list[i]
            trap_dict["Area"] = makeFormatting(round(0.5*trap_dict["h"]*(trap_dict["a"]+trap_dict["b"]),2))
            trap_dict["a"] = str(trap_dict["a"])
            trap_dict["h"] = str(trap_dict["h"])
            trap_dict["b"] = str(trap_dict["b"])
            trap_dict_list.append(trap_dict)
        return trap_dict_list

    def getCuboidDict(self,noofQuestions):
        cuboid_dict_list = []
        a_list = random.sample(range(1,100),k=noofQuestions)
        b_list = random.sample(range(1, 100), k=noofQuestions)
        c_list = random.sample(range(1, 100), k=noofQuestions)

        for i in  range(noofQuestions):
            cuboid_dict = {}
            cuboid_dict["a"]= a_list[i]
            cuboid_dict["b"]= b_list[i]
            cuboid_dict["c"] = c_list[i]
            cuboid_dict["Surface Area"] = makeFormatting(
                round((cuboid_dict["a"] * cuboid_dict["b"])
                      + (cuboid_dict["b"] * cuboid_dict["c"])
                         + (cuboid_dict["a"] * cuboid_dict["c"])))
            cuboid_dict["Volume"] = makeFormatting(
                round(cuboid_dict["c"] * cuboid_dict["a"] * cuboid_dict["b"]))
            cuboid_dict["a"] = str(a_list[i])
            cuboid_dict["b"] = str(b_list[i])
            cuboid_dict["c"] = str(c_list[i])
            cuboid_dict_list.append(cuboid_dict)
        return cuboid_dict_list

    def getCylinderDict(self,noofQuestions):
        cylin_dict_list = []
        radius_list = random.choices(range(1,20),k=noofQuestions)
        height_list = random.choices(range(1, 20), k=noofQuestions)

        for i in  range(noofQuestions):
            cylin_dict = {}
            cylin_dict["Radius"]= radius_list[i]
            cylin_dict["Height"]= height_list[i]
            cylin_dict["Total Surface Area"] = makeFormatting(
                round(2*3.14*cylin_dict["Radius"] * (cylin_dict["Radius"]+cylin_dict["Height"]),2))
            cylin_dict["Lateral Surface Area"] = makeFormatting(
                round(2*3.14*cylin_dict["Radius"] * cylin_dict["Height"],2))
            cylin_dict["Volume"] = makeFormatting(
                round(3.14*cylin_dict["Radius"]**2 * cylin_dict["Height"],2))
            cylin_dict["Radius"] = str(radius_list[i])
            cylin_dict["Height"] = str(height_list[i])
            cylin_dict_list.append(cylin_dict)
        return cylin_dict_list

    def getCircleDict(self,noofQuestions):
        circle_dict_list = []
        radius_list = random.sample(range(1,100),k=noofQuestions)
        radius_list.sort()
        for radius in radius_list:
            circle_dict = {}
            circle_dict["Radius"]= radius
            circle_dict["Area"] = makeFormatting(round(3.14*circle_dict["Radius"]**2,2))
            circle_dict["Perimeter"] = makeFormatting(round(2*3.14*circle_dict["Radius"],2))
            circle_dict["Radius"] = str(radius)
            circle_dict_list.append(circle_dict)
        return circle_dict_list

    def getSphereDict(self,noofQuestions):
        sphere_dict_list = []
        radius_list = random.sample(range(1,50),k=noofQuestions)
        radius_list.sort()
        for radius in radius_list:
            sphere_dict = {}
            sphere_dict["Radius"]= radius
            sphere_dict["Surface Area"] = makeFormatting(round(4*3.14*sphere_dict["Radius"]**2,2))
            sphere_dict["Volume"] = makeFormatting(round(4/3*3.14*sphere_dict["Radius"]**3,2))
            sphere_dict["Radius"] = str(radius)
            sphere_dict_list.append(sphere_dict)
        return sphere_dict_list

    def getQuestion(self,data,noofQuestions):
        tex_ques = ""
        tex_ans = ""
        shape = data["Shape"]
        shape_dict_list = self.getShapeDict[shape](noofQuestions)
        for i in range(noofQuestions):
            shape_dict = shape_dict_list[i]
            if isinstance(self.getShapeBlanks[shape],int):
            # MAKE SURE TO CHANGE THE VALUE OF k depending on the type of shape.
                ans_key = random.sample(shape_dict.keys(),k=self.getShapeBlanks[shape])
            else:
                ans_key = self.getShapeBlanks[shape]
            ans = ""
            for k in ans_key:
                ans = ans + k + " : " + shape_dict[k] + "\\\\"
            ques = ""
            for key in shape_dict.keys():
                if key in ans_key:
                    ques = ques + key + ": \\underline{\\hspace{1cm}}" + "\\\\"
                else:
                    ques = ques + key + ": " + shape_dict[key] + "\\\\"
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans


class OperationsQuestion():

    def multistepquestion(self, data, no_of_ques):
        tex_ques = ""
        tex_ans = ""
        steps = data["noofsteps"]
        operations = data["operation"]
        number_type = data["num_type"]
        noofQuestions = data["noofQuestions"]
        for i in range(no_of_ques):
            equation_array, equation_array_latex = equation_array_creator(operations, steps)

            for i in range((len(equation_array) + 1) // 2):
                num_latex, num_value = numericGenerator(number_type, data)
                equation_array_latex[2 * i] = num_latex
                #print(num_value)
                equation_array[2 * i] = eval(str(num_value))

            sym_indexes = np.where(np.array(equation_array) == '/')[0]
            for i in sym_indexes[::-1]:
                #if type(equation_array[i + 1]) == Rational:

                #    num_left_value = Rational(equation_array[i + 1] * random.randint(2, 10))

                #    equation_array[i - 1] = num_left_value
                #    equation_array_latex[i - 1] = latex(num_left_value)
                #    print(equation_array)
                #print("hi i am here")
                type_val = type(equation_array[i + 1])
                if  type_val == Integer or type_val == int:
                    num_left_value = equation_array[i + 1] * numericGenerator(['number'], data)[1]
                    equation_array[i - 1] = num_left_value
                    equation_array_latex[i - 1] = latex(num_left_value)
                elif type_val == Poly:
                    num_left_value = equation_array[i + 1] * numericGenerator(['polynomial'], data)[1]
                    equation_array[i - 1] = num_left_value
                    equation_array_latex[i - 1] = '{('+latex(num_left_value.expr)+')}'
                elif "decimal" in number_type:

                    temp = numericGenerator(['decimal'], data)[1]
                    num_left_value = equation_array[i + 1] * temp
                    equation_array[i - 1] = num_left_value
                    equation_array_latex[i - 1] = latex(num_left_value)

            for i in range((len(equation_array) + 1) // 2):
                equation_array[2 * i] = str(equation_array[2 * i])

            ans = "".join(equation_array)
            #print(ans)
            if "polynomial" in number_type:
                ans = latex(simplify(ans))
            elif "fraction" in number_type and "decimal" not in number_type:
                #print(equation_array)
                frac_answer = Fraction(eval(ans)).limit_denominator(10000)
                ans = latex(Rational(frac_answer.numerator, frac_answer.denominator))
            elif "complex" in number_type:
                ans = latex(simplify(ans))
            else:
                ans = latex(round(eval(ans), 3))
            question, ans = latexQuestionAnsPackager(''.join(equation_array_latex), str(ans))
            tex_ques = tex_ques + question
            tex_ans = tex_ans + ans

        return tex_ques, tex_ans


class CoordinateGeometry():

    def __init__(self):
        self.getQuestion = {
            "Distance between two Points": self.getDistanceBetweenPointsQuestion,
            "Slope between two Points": self.getSlopeBetweenPointsQuestion,
            "Equation of Line joining two Points": self.getLineBetweenPointsQuestion,
            "Equation of Line slope point form": self.getLinePointSlopeQuestion,
            "Equation of Line point line form": self.getLinePointLineQuestion,
            "Point of intersection between two lines": self.getPointBetweenLinesQuestion,
            "Equation of Perpendicular Bisector between two Points": self.getPerpendicularBisectorPointsQuestion,
            "Distance of Point from Line": self.getDistancePointLineQuestion,
            "Midpoint of two points": self.getMidPointQuestion,
        }

    def getTwoPoints(self,data):
        num1_latex, num1 = numericGenerator(["number"], data)
        num2_latex, num2 = numericGenerator(["number"], data)
        p1 = Point(num1, num2)
        num3_latex, num3 = numericGenerator(["number"], data)
        num4_latex, num4 = numericGenerator(["number"], data)
        p2 = Point(num3, num4)
        while p1==p2 :
            num3_latex, num3 = numericGenerator(["number"], data)
            num4_latex, num4 = numericGenerator(["number"], data)
            p2 = Point(num3, num4)

        return p1,p2

    def getTwoLines(self,data):
        p1, p2 = self.getTwoPoints(data)
        p3, p4 = self.getTwoPoints(data)
        l1 = Line(p1,p2)
        l2 = Line(p3, p4)
        return l1,l2

    def getMidPointQuestion(self, data, noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            p1, p2 = self.getTwoPoints(data)
            #print(l1,l2)
            mid = Segment(p1,p2).midpoint
            points_list = {"A":p1,"B":p2,"Mid":mid}
            #choose
            ans_key = random.choice(list(points_list.keys()))
            ques = ""
            for key in points_list.keys():
                if key == ans_key:
                    ques = ques + key + ": \\underline{\\hspace{1cm}}" + "\\\\"
                else:
                    ques = ques + key + ": $" + latex(points_list[key].coordinates) + "$\\\\"
            ans =  "$" + latex(points_list[ans_key].coordinates) + " $"
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getPerpendicularBisectorPointsQuestion(self, data, noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            p1, p2 = self.getTwoPoints(data)
            #print(l1,l2)
            s = Segment(p1,p2)
            ans =  "$" + latex(s.perpendicular_bisector().equation()) + "=0 $"
            ques = "A: $"+latex(p1.coordinates)+"$ and B: $"+latex(p2.coordinates)
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getDistancePointLineQuestion(self, data, noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            l1, l2 = self.getTwoLines(data)
            p1,p2 = self.getTwoPoints(data)
            ans =  "$" + latex(p1.distance(l1)) + "$"
            ques = "Point A: "+latex(p1.coordinates)+"$ Line l:$" + latex(l1.equation()) + "=0 $"
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getPointBetweenLinesQuestion(self, data, noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            l1, l2 = self.getTwoLines(data)
            #print(l1,l2)
            int_point = l1.intersection(l2)
            #print(int_point)
            if len(int_point)==0:
                ans = " No point of intersection"
            else:
                ans = "$"+latex(int_point.coordinates)+"$"
            # print(ans)
            ques = "Find the point of intersection between the lines: " + "$" + latex(l1.equation()) + "=0 $"\
                   + " and " + "$" + latex(l2.equation()) + "=0 $"
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getDistanceBetweenPointsQuestion(self,data,noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            p1,p2 = self.getTwoPoints(data)
            ans = "$"+latex(p1.distance(p2))+"$"
            #print(ans)
            ques = "A: $"+latex(p1.coordinates)+"$ and B: $"+latex(p2.coordinates)+"$"
            ques, ans = latexQuestionAnsPackager(ques, ans,False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getSlopeBetweenPointsQuestion(self,data,noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            p1, p2 = self.getTwoPoints(data)
            l = Line(p1, p2)
            ans = "$"+latex(l.slope)+"$"
            #print(ans)
            ques = "A: $"+latex(p1.coordinates)+"$ and B: $"+latex(p2.coordinates)+"$"
            ques, ans = latexQuestionAnsPackager(ques, ans,False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getLineBetweenPointsQuestion(self,data,noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            p1,p2 = self.getTwoPoints(data)
            l = Line(p1,p2)

            ans = "$"+latex(l.equation())+"=0 $"
            #print(ans)
            ques = "A: $"+latex(p1.coordinates)+"$ and B: $"+latex(p2.coordinates)+"$"
            ques, ans = latexQuestionAnsPackager(ques, ans,False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getLinePointSlopeQuestion(self,data,noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            p1,p2 = self.getTwoPoints(data)
            l = Line(p1,p2)

            ans = "$"+latex(l.equation())+"=0 $"
            #print(ans)
            ques = "Equation of Line passing through $"+latex(p1.coordinates)+"$ and having slope " + str(l.slope)
            ques, ans = latexQuestionAnsPackager(ques, ans,False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getLinePointLineQuestion(self,data,noofQuestions):

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            p1,p2 = self.getTwoPoints(data)
            l = Line(p1,p2)
            p3,p4= self.getTwoPoints(data)
            choice = random.choice([-1,1])
            if choice==-1:
                ans_l = l.perpendicular_line(p3)
                ans = "$"+latex(ans_l.equation(x,y))+"=0 $"
                ques = "Equation of Line passing through $"+latex(p3.coordinates)+"$ and perpendicular to $" + latex(l.equation())+"=0 $"
            else:
                ans_l = Line(p3, slope=l.slope)
                ans = "$" + latex(ans_l.equation()) + "=0 $"
                ques = "Equation of Line passing through $"+latex(p3.coordinates)+"$ and parallel to $" + latex(l.equation())+"=0 $"

            ques, ans = latexQuestionAnsPackager(ques, ans,False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

class NumbersQuestion():

    def __init__(self):
        self.getQuestion = {
            "Prime Factorization": self.getPrimeFactorizationQuestion,
            "LCM HCF": self.getLCMHCFQuestion,
            "Addition of Numbers": self.getOperatorQuestion,
            "Subtraction of Numbers": self.getOperatorQuestion,
            "Division of Numbers": self.getOperatorQuestion,
            "Multiplication of Numbers": self.getOperatorQuestion,
            "Mixed Operation of Numbers": self.getOperatorQuestion,
        }

    def getOperatorQuestion(self, data, noofQuestions):
        opq = OperationsQuestion()
        tex_ques, tex_ans = opq.multistepquestion(data, noofQuestions)
        return tex_ques, tex_ans

    def isPrime(self,num):
        if num > 1:

            # Iterate from 2 to n / 2
            for i in range(2, int(num / 2) + 1):

                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    return False
                    break
            else:
                return True
        else:
            return False

    def getLCMHCFDict(self,max):
        lh_dict = {}
        num_1 = random.randint(1,max)
        lh_dict["a"] = random.randint(1,max)*num_1
        lh_dict["b"] = random.randint(1,max)*num_1
        lh_dict["LCM"] = str(lcm(lh_dict["a"],lh_dict["b"]))
        lh_dict["HCF"] = str(gcd(lh_dict["a"],lh_dict["b"]))
        lh_dict["a"] = str(lh_dict["a"])
        lh_dict["b"] = str(lh_dict["b"])

        return lh_dict

    def getLCMHCFQuestion(self,data,noofQuestions):
        tex_ques = ""
        tex_ans = ""

        primes = [i for i in range(2, max) if self.isPrime(i)]
        for i in range(noofQuestions):

            lcm_dict = self.getLCMHCFQuestion(data)
            ans_key = random.choice(["Initial Value", "Percentage", "Final Value"])
            ans = ans_key + " : " + lcm_dict[ans_key] + "\\\\"
            lcm_dict[ans_key] = "\\underline{\\hspace{1cm}}"
            if lcm_dict["Change"].find('-') == -1:
                ques = lcm_dict["Initial Value"] + " increased by " + lcm_dict["Percentage"] + " is " + pl_dict["Final Value"]
            else:
                ques = lcm_dict["Initial Value"] + " decreased by " + lcm_dict["Percentage"].replace('-', '') + " is " + \
                       lcm_dict["Final Value"]
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans

        return tex_ques, tex_ans

    def getPrimeFactorizationQuestion(self,data,noofQuesitons):
        tex_ques = ""
        tex_ans = ""
        noofsteps = data["noofsteps"]
        max = data["number"]["max"]
        #creating factor dictionary

        primes = [i for i in range(2, max) if self.isPrime(i)]
        #print(primes)
        for i in range(noofQuesitons):
            #print(num_min,num_max)
            fact_dict = {}

            for i in range(noofsteps):

                n = random.choice(primes)
                fact_dict[n] = random.randint(1, 3)

            # number
            question = latex(simplify(factorint(fact_dict)))
            ans = latex(factorint(fact_dict,visual=True))

            question, ans = latexQuestionAnsPackager(question,ans)
            tex_ques = tex_ques + question
            tex_ans = tex_ans + ans

        return tex_ques, tex_ans

    def getLCMHCFQuestion(self,data,noofQuesitons):
        tex_ques = ""
        tex_ans = ""
        noofsteps = data["noofsteps"]
        max = data["number"]["max"]
        #creating factor dictionary

        for i in range(noofQuesitons):
            pl_dict = self.getLCMHCFDict(max)
            ans_key = ["HCF","LCM"]
            ans = ""
            for k in ans_key:
                ans = ans + k + " : " + pl_dict[k] + "\\\\"
            ques = ""
            for key in pl_dict.keys():
                if key in ans_key:
                    ques = ques + key + ": \\underline{\\hspace{1cm}}" + "\\\\"
                else:
                    ques = ques + key + ": " + pl_dict[key] + "\\\\"

            ques, ans = latexQuestionAnsPackager(ques,ans)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans

        return tex_ques, tex_ans


class SurdQuestion():


    def surdGenerator(self,prime):
        radical = prime*random.randint(1,9)**2
        surd_val = sqrt(radical)
        surd_latex = "\\sqrt{"+str(radical)+"}"
        return surd_latex, surd_val

    def questionCreator(self,data,noofQuesitons):
        tex_ques = ""
        tex_ans = ""
        operations = data["operation"]
        steps = data["noofsteps"]

        for i in range(noofQuesitons):
            equation_array, equation_array_latex = equation_array_creator(operations, steps)
            num_min = data["surd"]['min']
            num_max = data["surd"]['max']
            #print(num_min,num_max)
            number_1 = randprime(num_min,num_max)
            for i in range((len(equation_array) + 1) // 2):
                num_latex, num_value = self.surdGenerator(number_1)
                equation_array_latex[2 * i] = num_latex
                equation_array[2 * i] = num_value

            for i in range((len(equation_array) + 1) // 2):
                equation_array[2 * i] = str(equation_array[2 * i])

            # print(equation_array)
            # print(equation_array_latex)l
            ans = "".join(equation_array)
            #print(ans)
            ans = latex(simplify(ans))
            question, ans = latexQuestionAnsPackager(''.join(equation_array_latex), str(ans))
            tex_ques = tex_ques + question
            tex_ans = tex_ans + ans

        return tex_ques, tex_ans

class PercentageQuestion():


    def getSimpleInterestDict(self):
        si_dict = {}
        si_dict["Principal"] = random.randint(1,1000)*1000
        si_dict["Rate"] = random.randint(1,10) * random.randint(1,10)
        si_dict["Time"] = random.randint(1,10)
        si_dict["Interest"] = si_dict["Principal"] *si_dict["Rate"]*si_dict["Time"]/100
        si_dict["Amount"] = si_dict["Interest"] +  si_dict["Principal"]

        return si_dict


    def getPercentageDict(self):
        p_dict = {}
        p_dict["Initial Value"] = random.randint(1,100)*100
        #to change increase or decrease
        p_dict["Percentage"] = random.choice([1,2,4,5,10,15,20,25,30,40,50,75,100])*random.choice([-1,1])
        p_dict["Change"] = p_dict["Initial Value"] * p_dict["Percentage"] / 100
        p_dict["Final Value"] = makeFormatting(p_dict["Initial Value"] + p_dict["Change"])
        p_dict["Percentage"] =str(p_dict["Percentage"])+"\\%"
        p_dict["Initial Value"]=makeFormatting(p_dict["Initial Value"] )
        p_dict["Change"]= makeFormatting(p_dict["Change"])

        return p_dict


    def getCompoundInterestDict(self):
        ci_dict = {}
        ci_dict["Principal"] = random.randint(1,1000)*1000
        ci_dict["Rate"] = random.choice([1,2,4,5,10,15,20,25,30])
        ci_dict["Time"] = random.randint(1,5)
        ci_dict["Freq"] = random.choice([1,2,4,12])
        ci_dict["Amount"] = round(ci_dict["Principal"] *(1+ci_dict["Rate"]/(100*ci_dict["Freq"]))**(ci_dict["Time"]*ci_dict["Freq"]),2)
        ci_dict["Interest"] = round(ci_dict["Amount"] -  ci_dict["Principal"],2)

        return ci_dict

    def junk(self):
        self.principal = Symbol('p')
        self.freq = Symbol('n')
        self.rate = Symbol('r')
        self.time = Symbol('t')
        self.interest = Symbol('i')
        self.value = Symbol('f')

        self.simple_interest_eq = Eq(self.principal * self.rate * self.time / 100, self.interest)
        self.final_value_eq = Eq(self.interest + self.principal, self.value)
        self.compound_interest_eq = Eq(
            self.principal * (1 + self.rate / (self.freq * 100) ** (self.time * self.freq), self.value))

    def __init__(self):

        self.freq_dict = {
            1: "Annual",
            2: "Semi-Annual",
            4: "Quarterly",
            12: "Monthly"
        }

        self.getQuestion = {
            "Percentage Increase Decrease": self.getIncreaseDecreaseQuestion,
            "Find Missing Value": self.getMissingValueQuestion,
            "Profit Loss": self.getProfitLossQuestion,
            "Simple Interest": self.getSimpleInterestQuestion,
            "Compound Interest": self.getCompoundInterestQuestion
        }



    def getMissingValueQuestion(self,data,noofQuestions):
        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            pl_dict = self.getPercentageDict()
            if pl_dict["Change"].find('-')!=-1:
                pl_dict["Percentage"]=pl_dict["Percentage"].replace("-","")
                pl_dict["Change"]=pl_dict["Change"].replace("-","")
            ans_key = random.choice(["Initial Value", "Percentage", "Change"])

            ans = pl_dict[ans_key] + "\\\\"
            pl_dict[ans_key] = "\\underline{\\hspace{1cm}}"
            ques = pl_dict["Percentage"] + " of " + pl_dict["Initial Value"] + " is " + pl_dict["Change"]
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getIncreaseDecreaseQuestion(self, data, noofQuestions):
        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            pl_dict = self.getPercentageDict()
            ans_key = random.choice(["Initial Value","Percentage","Final Value"])
            ans = ans_key + " : " + pl_dict[ans_key] + "\\\\"
            pl_dict[ans_key]= "\\underline{\\hspace{1cm}}"
            if pl_dict["Change"].find('-')==-1:
                ques = pl_dict["Initial Value"] + " increased by " + pl_dict["Percentage"] + " is " + pl_dict["Final Value"]
            else:
                ques = pl_dict["Initial Value"] + " decreased by " + pl_dict["Percentage"].replace('-','') + " is " + pl_dict["Final Value"]
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getProfitLossQuestion(self, data, noofQuestions):
        tex_ques = ""
        tex_ans = ""

        pl_terms_dict = {
            "Initial Value": "Cost Price",
            "Percentage": "P/L Percentage",
            "Change" : "Profit or Loss",
            "Final Value" : "Sale Price"
        }

        for i in range(noofQuestions):
            pl_dict = self.getPercentageDict()
            ans_key = random.sample(list(pl_dict.keys()),k=2)
            ans = ""
            for k in ans_key:
                ans = ans + pl_terms_dict[k] + " : " + pl_dict[k] + "\\\\"
            ques = ""
            for key in pl_dict.keys():
                if key in ans_key:
                    ques = ques + pl_terms_dict[key] + ": \\underline{\\hspace{1cm}}" + "\\\\"
                else:
                    ques = ques + pl_terms_dict[key] + ": " + pl_dict[key] + "\\\\"
            ques, ans = latexQuestionAnsPackager(ques, ans,False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getSimpleInterestQuestion(self, data, noofQuestions):
        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            si_dict = self.getSimpleInterestDict()
            ans_key = random.choice(list(si_dict.keys()))
            ans = ans_key + " : "+str(si_dict[ans_key])
            ques = ""
            for key in si_dict.keys():
                if key == ans_key:
                    ques = ques +  key + ": \\underline{\\hspace{1cm}}" + "\\\\"
                else:
                    ques = ques + key + ": "+ str(si_dict[key]) + "\\\\"
            ques, ans = latexQuestionAnsPackager(ques, ans, False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getCompoundInterestQuestion(self, data, noofQuestions):
        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            ci_dict = self.getCompoundInterestDict()
            ans_key = random.choice(list(ci_dict.keys()))
            if ans_key == "Freq":
                ans = ans_key + " : " + self.freq_dict[ci_dict[ans_key]]
            else:
                ans = ans_key + " : " + "{:,}".format(ci_dict[ans_key])
            ques = ""
            for key in ci_dict.keys():
                if key == ans_key:
                    ques = ques + key + ": \\underline{\\hspace{1cm}}" + "\\\\"
                else:
                    if key == "Freq":
                        ques = ques + key + ": " + self.freq_dict[ci_dict[key]] + "\\\\"
                    else:
                        ques = ques + key + ": " + "{:,}".format(ci_dict[key]) + "\\\\"
            ques, ans = latexQuestionAnsPackager(ques, ans,False)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

class SequenceSeriesQuestion():

    def __init__(self):
        self.getQuestion = {
            "Find Nth Term": self.getFindNthTerm,
            "Find Missing Terms in Arithmetic Series": self.getFindMissingTerms,
            "Find Missing Terms in Geometric Series": self.getFindMissingTerms,
            "Find Nth Term Quadratic": self.getFindNthTerm,
            "Find Nth Term in Geometric Series": self.getFindNthTerm,
            "Find Missing Terms Quadratic": self.getFindMissingTerms
        }

    def getFindNthTerm(self,data,noofQuestions):
        series_type = data["type"]
        #print(series_type)
        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            num_latex, num1 = numericGenerator(["number"], data)
            num_latex, num2 = numericGenerator(["number"], data)
            #op_sym = random.choice(operations)
            if series_type == "linear":
                s = SeqFormula(num1 * n + num2, (n, 1, 5))
            elif series_type == "geometric":
                s = SeqFormula(num2 * num1 ** n, (n, 1, 5))
            elif series_type == "quadratic":
                num_latex, num3 = numericGenerator(["number"], data)
                # op_sym = random.choice(operations)
                s = SeqFormula(num3 * n ** 2 + num1 * n + num2, (n, 1, 5))
            seq_list = list(s)
            ans = s.formula
            ques, ans = latexQuestionAnsPackager(latex(seq_list), latex(ans))
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans


    def getFindMissingTerms(self,data,noofQuestions):
        #operations = data["operation"]
        series_type = data["type"]
        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            num_latex, num1 = numericGenerator(["number"], data)
            num_latex, num2 = numericGenerator(["number"], data)
            #op_sym = random.choice(operations)
            missing_terms = 3
            if series_type == "linear":
                s = SeqFormula(num1 * n + num2, (n, 1, 10))
            elif series_type == "geometric":
                s = SeqFormula(num2 * num1 ** n, (n, 1, 6))
                missing_terms = 2
            elif series_type == "quadratic":
                num_latex, num3 = numericGenerator(["number"], data)
                # op_sym = random.choice(operations)
                s = SeqFormula(num3 * n ** 2 + num1 * n + num2, (n, 1, 10))
            seq_list = list(s)
            #print(seq_list)
            missing_index = random.sample(range(len(seq_list)),k=missing_terms)
            missing_index.sort()

            #print(missing_index)
            ans_list = [seq_list[i] for i in missing_index]
            seq_list = ["___" if i in missing_index else seq_list[i] for i in range(len(seq_list))]
            #print(seq_list)
            ques, ans = latexQuestionAnsPackager(latex(seq_list) , latex(ans_list))
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

class CalculusQuestion():
    def __init__(self):
        self.x = Symbol('x')
        self.y = Symbol('y')

    def integrate_expr(self,data,noofQuestions):
        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            exp_latex, exp_val = numericGenerator(["polynomial"],data)
            ans = exp_val.integrate(self.x)
            question, ans = latexQuestionAnsPackager("\int" +exp_latex +"\,dx", latex(ans.expr) +"+ c")
            tex_ques = tex_ques +question
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def differentiate_expr(self,data,noofQuestions):
        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            exp_latex, exp_val = numericGenerator(["polynomial"],data)
            ans = diff(exp_val,self.x)
            question, ans = latexQuestionAnsPackager("\\frac{\,d}{\,dx} " + exp_latex, latex(ans.expr))
            tex_ques = tex_ques + question
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

class ExponentsQuestion:

    def __init__(self):
        self.getQuestion = {
            "Indices Formulas": self.getIndicesFormulaQuestion,
        }

    def getIndicesFormulaQuestion(self,data, noofQuestions):
        tex_ques = ""
        tex_ans = ""
        no_of_steps = data["noofsteps"]

        for i in range(noofQuestions):
            equation_array, equation_array_latex = equation_array_creator(['**', '/', '*'], no_of_steps)
            for i in range((len(equation_array) + 1) // 2):
                num_latex, num_value = numberGenerator(data["number"],True)
                #equation_array[2*i] = x**num_value
                equation_array[2 * i] = num_value
                equation_array_latex[2 * i] = latex(num_value)
                #equation_array[2 * i] = Pow(x, num_value)
            expr = x**equation_array[0]
            expr_latex = latex(expr)
            for i in range(1,len(equation_array)):
                if isinstance(equation_array[i],str):
                    expr = '(' + str(expr) + ')' + equation_array[i]
                    expr_latex = " "+'(' + expr_latex + ')' + equation_array_latex[i]
                else:
                    if equation_array[i-1]=='**':
                        expr = str(expr) + str(equation_array[i])
                        expr_latex = expr_latex +" "+ "^{"+str(equation_array[i])+"}"
                    else:
                        expr = str(expr) + str(x**equation_array[i])
                        expr_latex = expr_latex +" " + latex(x**equation_array[i])


            #for j in range(len(equation_array)):
            #    expr = str(expr) + str(equation_array[j])
            #print(expr)
            #print(expr_latex)
            ans = simplify(expr)
            #print(ans)
            #ans = powsimp(expr)
            #question, ans = latexQuestionAnsPackager("".join(equation_array_latex) + '=?', str(ans))
            question, ans = latexQuestionAnsPackager(expr_latex + '=?', latex(ans))
            tex_ques = tex_ques + question
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

class AlgebraQuestion:

    def __init__(self):
        self.getQuestion = {
            "Addition of Variables": self.getOperatorQuestion,
            "Subtraction of Variables": self.getOperatorQuestion,
            "Expansion": self.getOperatorQuestion,
            "Division": self.getOperatorQuestion,
            "Linear Equations": self.getLinearEquationInequalityQuestion,
            "Linear Inequality": self.getLinearEquationInequalityQuestion,
            "System of Linear Equations": self.getSystemofLinearEquationQuestion,
            "Quadratic Factorization": self.getQuadraticFactorizationQuestion,
            "Quadratic Equation": self.getQuadraticEquationInequalityQuestion,
            "Quadratic Inequality": self.getQuadraticEquationInequalityQuestion,
            "Making Subject": self.getMakingSubjectQuestion,
            "Substitution of values": self.getSubstitutionQuestion,
           # "Algebraic Expression Description": self.getAlgebraExpressionDescriptionQuestion
        }


    def getOperatorQuestion(self,data,noofQuestions):
        opq = OperationsQuestion()
        tex_ques, tex_ans = opq.multistepquestion(data, noofQuestions)
        return tex_ques,tex_ans

    def getLinearEquationInequalityQuestion(self, data, noofQuestions):
        tex_ques = ""
        tex_ans = ""
        operations = data['operation']
        leading_coeff = data["polynomial"]["leading_coeff"]
        min_num = data["polynomial"]["min_coeff"]
        max_num = data["polynomial"]["max_coeff"]

        for i in range(noofQuestions):
            #equation_array, equation_array_latex = equation_array_creator(operations, 2)
            #num_latex, num_value = numericGenerator(["number"], data)
            #equation_array[0] = num_value
            #equation_array_latex[0] = num_latex
            #num_latex, num_value = numericGenerator(["number"], data)
            #equation_array[4] = num_value
            #equation_array_latex[4] = num_latex
            #equation_array[2] = x
            #equation_array_latex[2] = latex(x)
            #expr_str = "".join([str(x) for x in equation_array])
            rela = random.choice(operations)
            expr_latex,expr_str = self.linearExpression(data, 1,['x'], leading_coeff, True)
            #print(expr)
            substitution_val = random.randint(min_num,max_num)
            rhs = expr_str.subs(x, substitution_val)
            #inequality = random.choice(['<','>','>=','<='])
            question = latex(expr_str.expr) + rela + latex(rhs)
            if rela=='=':
                # equation and selection of the first answer
                ans = str(solve(Eq(expr_str.expr,rhs))[0])
            else:
                expr_str = str(expr_str.expr) + rela + str(rhs)
                ans = str(simplify(reduce_inequalities(expr_str,[]))).replace('&','\&')
            question, ans = latexQuestionAnsPackager(question,(ans))
            tex_ques = tex_ques + question
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getLinearEquationInequalityAdvancedQuestion(self, data, noofQuestions):
        tex_ques = ""
        tex_ans = ""
        operations = data['operation']
        leading_coeff = data["polynomial"]["leading_coeff"]
        for i in range(noofQuestions):
            # equation_array, equation_array_latex = equation_array_creator(operations, 2)
            # num_latex, num_value = numericGenerator(["number"], data)
            # equation_array[0] = num_value
            # equation_array_latex[0] = num_latex
            # num_latex, num_value = numericGenerator(["number"], data)
            # equation_array[4] = num_value
            # equation_array_latex[4] = num_latex
            # equation_array[2] = x
            # equation_array_latex[2] = latex(x)
            # expr_str = "".join([str(x) for x in equation_array])
            rela = random.choice(operations)
            expr_1 = self.linearExpression(data, 1,['x'], leading_coeff, True)
            expr_2 = self.linearExpression(data, 1,['x'], leading_coeff, True)
            #num_latex, substitution_val = numericGenerator(["number"], data)
            #rhs = expr.subs(x, substitution_val)
            # inequality = random.choice(['<','>','>=','<='])
            question = latex(expr_1) + rela + latex(expr_2)
            expr_str = str(expr_1) + rela + str(expr_2)
            if rela == '=':
                # equation and selection of the first answer
                ans = str(solve(Eq(expr, rhs))[0])
            else:
                ans = str(simplify(reduce_inequalities(expr_str, []))).replace('&', '\&')
            question, ans = latexQuestionAnsPackager(question, (ans))
            tex_ques = tex_ques + question
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def linearExpression(self,data,degree,variables,leading_coeff = False, const_term = False):
        #symbols_list = symbols(variables)
        #if const_term:
        #    expr = numericGenerator(["number"], data)[1]
        #else:
        #    expr = 0
        #for symbol in symbols_list:
        #    if leading_coeff:
        #        x_latex, coeff_value = numericGenerator(["number"], data)
        #        expr = Add(expr,coeff_value*symbol)
        #    else:
        #        expr = Add(expr, symbol)
        data["polynomial"]["degree"]=degree
        data["polynomial"]["variables"] = variables
        data["polynomial"]["const_term"] = const_term
        #print(data)
        expr_latex,expr = numericGenerator(["polynomial"],data)
        return expr_latex,expr

    def getSubstitutionQuestion(self,data, noofQuestions):
        no_of_steps = data["noofsteps"]//2
        operations = data["operation"]
        degree = data["polynomial"]["degree"]

        # Make right hand side of the equation with half the operations
        #ans_op_array = random.choices(operations, k=no_of_steps // 2)

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            op_array = random.choices(operations, k=no_of_steps)
            variables = copy.deepcopy(data["polynomial"]["variables"])
            # print(variables)
            #subject_variable = Symbol(random.choice(variables))
            #variables.remove(subject_variable.name)
            expr_1 = str(self.getSingleTerm(variables, degree, data))
            #expr_2 = subject_variable
            for op_sym in op_array:
                expr_1 = '(' + str(expr_1) + ')' + op_sym + '(' + str(self.getSingleTerm(variables, degree, data)) + ')'
            #print(expr_1)
            sub_vals =[]
            sub_expr = ""
            expr_1 = simplify(expr_1)
            for var in expr_1.free_symbols:
                num1 = numericGenerator(["number"], data)[1]
                sub_vals.append((var,num1))
                sub_expr = sub_expr+ str(var)+"="+str(num1)+","
            #print(sub_vals)
            ans = expr_1.subs(sub_vals)
            #print(ans)
            ques, ans = latexQuestionAnsPackager(latex(expr_1) + "; \\ \n Substitution:" + sub_expr,str(ans) )
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getSingleTerm(self,variables,degree,data):
        num_latex, num_val = numericGenerator(["number"],data)
        #no_of_variables = random.choice(range(len(variables)))
        # add functionality to generate 5y^2z etc
        var = Symbol(random.choice(variables))
        deg = random.choice(range(1,degree+1))
        const_term = data["polynomial"]["const_term"]
        if const_term:
            const = numericGenerator(["number"], data)[1]
        else:
            const = 0
        return num_val*var**deg + const



    def getMakingSubjectQuestion(self,data, noofQuestions):
        no_of_steps = data["noofsteps"]
        operations = data["operation"]
        degree = data["polynomial"]["degree"]
        op_array = random.choices(operations,k=no_of_steps)
        #Make right hand side of the equation with half the operations
        ans_op_array = random.choices(operations, k=no_of_steps//2)

        tex_ques = ""
        tex_ans = ""

        for i in range(noofQuestions):
            variables = copy.deepcopy(data["polynomial"]["variables"])
            #print(variables)
            subject_variable = Symbol(random.choice(variables))
            variables.remove(subject_variable.name)
            expr_1 = subject_variable
            expr_2 = subject_variable
            for op_sym in op_array:
                expr_1 = '('+str(expr_1)+')' + op_sym + '('+ str(self.getSingleTerm(variables,degree,data)) + ')'
            #print(expr_1)
            for op_sym in ans_op_array:
                expr_2 = '('+str(expr_2)+')'+ op_sym + '('+ str(self.getSingleTerm(variables, degree, data))+ ')'
            #print(expr_2)
            equ = Eq(simplify(expr_1),simplify(expr_2))
            #print(equ)
            ans = latex(subject_variable)+ " = " + latex(solve(equ,subject_variable))
            #print(ans)
            ques, ans = latexQuestionAnsPackager(latex(equ) + ";" + latex(subject_variable) + "= ?", ans)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getSystemofLinearEquationQuestion(self,data, noofQuestions):
        tex_ques = ""
        tex_ans = ""
        min_num = data["polynomial"]["min_coeff"]
        max_num = data["polynomial"]["max_coeff"]
        for i in range(noofQuestions):
            expr1_latex, exp_1 = self.linearExpression(data,1,['x', 'y'],const_term=False)
            expr2_latex, exp_2 = self.linearExpression(data,1,['x', 'y'],const_term=False)
            #print("this is my expr",exp_3)
            x_sub = random.randint(min_num,max_num)
            y_sub = random.randint(min_num,max_num)
            #y_sub_latex, y_sub = numericGenerator(["number"], data)
            ans_1 = exp_1.subs([(x, x_sub), (y, y_sub)])
            ans_2 = exp_2.subs([(x, x_sub), (y, y_sub)])
            equ_1 = expr1_latex + "=" + str(ans_1)
            equ_2 = expr2_latex + "=" + str(ans_2)
            ans = "x = " + str(x_sub) + " ; "+ "y = " + str(y_sub)
            ques, ans = latexQuestionAnsPackager(equ_1+" ; "+equ_2,ans)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans

        return tex_ques, tex_ans

    def getQuadraticFactorizationQuestion(self,data, noofQuestions):
        tex_ques = ""
        tex_ans = ""
        leading_coeff = data["polynomial"]["leading_coeff"]
        for i in range(noofQuestions):
            exp_2_ltx, exp_2 = self.linearExpression(data,1,['x'],leading_coeff,True)
            exp_1_ltx, exp_1 = self.linearExpression(data,1,['x'],leading_coeff,True)
            #print(exp_1)
            #print(exp_2)

            ans = exp_1.expr*exp_2.expr
            #print(ans)
            ques = expand(ans)
            ques, ans = latexQuestionAnsPackager(latex(ques),latex(ans))
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans

    def getQuadraticEquationInequalityQuestion(self,data, noofQuestions):
        tex_ques = ""
        tex_ans = ""
        relation = data["operation"]

        leading_coeff = data["polynomial"]["leading_coeff"]
        for i in range(noofQuestions):
            exp_2_ltx,exp_2 = self.linearExpression(data,1,['x'],leading_coeff,True)
            exp_1_ltx,exp_1 = self.linearExpression(data,1,['x'],leading_coeff,True)
            rela = random.choice(relation)
            #print(exp_1)
            #print(exp_2)
            if rela=='=':
                ques = Eq((exp_1 * exp_2).expr,0)
                #print(ques)
                ans = solve(ques)
                if len(ans)==1:
                    ques, ans = latexQuestionAnsPackager(latex(ques), 'x =' + str(ans[0]))
                else:
                    ques, ans = latexQuestionAnsPackager(latex(ques),'x ='+ str(ans[0]) + '\ or \ x ='+ str(ans[1]))
            else:
                ques = str((exp_1 * exp_2).expr) + rela + '0'
                ques_ltx = latex((exp_1 * exp_2).expr) + rela + '0'
                #print(ques)
                #print(solve_univariate_inequality(parse_expr(ques,evaluate=False), x))
                ans = str(solve_univariate_inequality(parse_expr(ques,evaluate=False), x))\
                    .replace('&', '\ and \ ').replace('|', '\ or \ ').replace('False','No Solution')
                ques, ans = latexQuestionAnsPackager((ques_ltx),ans)
            tex_ques = tex_ques + ques
            tex_ans = tex_ans + ans
        return tex_ques, tex_ans


    #def getAlgebraExpressionDescriptionQuestion(self,data, noofQuestions):
    #        tex_ques = ""
    #        tex_ans = "" AlgebraQuestions()
    #        leading_coeff = data["polynomial"]["leading_coeff"]etLinearEquationQuestion()
    #        for i in range(noofQuestions):