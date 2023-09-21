import json
import os
import shutil

from stocks import settings

from worksheet.algo.latexfunctions import latex_to_pdf
from worksheet.algo.questionsCreator import *
from sympy.abc import x


def createWorksheetbyTopic(chapter_name, topic_name):
    f = open(settings.STATIC_ROOT+'/json/grade5.json', )
    data = json.load(f)
    noofQuestions = data["Parameters"]["noofquestions"]
    noofWorksheets = data["Parameters"]["noofworksheets"]
    chapter_json = data["Chapters"][chapter_name]
    description = chapter_json[topic_name]["Description"]
    for difficulty in chapter_json[topic_name]:
        if difficulty == "Description":
            continue
        number_type = chapter_json[topic_name][difficulty]["num_type"]
        operations = chapter_json[topic_name][difficulty]["operation"]
        noofsteps = chapter_json[topic_name][difficulty]["noofsteps"]
        for i in range(noofWorksheets):
            data_param_difficulty = data["Parameters"][difficulty]
            data_param_difficulty["noofsteps"] = noofsteps
            data_param_difficulty["operation"] = operations
            data_param_difficulty["num_type"]=number_type
            data_param_difficulty["noofQuestions"] = noofQuestions

            if chapter_name == "Algebra":
                a = AlgebraQuestion()
                tex_ques, tex_ans = a.getQuestion[topic_name](data_param_difficulty,noofQuestions)

            elif chapter_name == "Shapes":
                shapes = ShapesQuestion()
                data_param_difficulty["Shape"]=topic_name
                #removed key from getquestion .. as th function points to correct shape
                tex_ques, tex_ans = shapes.getQuestion(data_param_difficulty, noofQuestions)


            elif chapter_name == "Coordinate Geometry":
                coog = CoordinateGeometry()
                tex_ques, tex_ans = coog.getQuestion[topic_name](data_param_difficulty, noofQuestions)

            elif chapter_name == "Numbers":
                num = NumbersQuestion()
                tex_ques, tex_ans = num.getQuestion[topic_name](data_param_difficulty, noofQuestions)

            elif chapter_name == "Percentages":
                perc = PercentageQuestion()
                tex_ques, tex_ans = perc.getQuestion[topic_name](data_param_difficulty, noofQuestions)

            elif chapter_name == "Exponents":
                exp = ExponentsQuestion()
                tex_ques, tex_ans = exp.getQuestion[topic_name](data_param_difficulty, noofQuestions)

            elif chapter_name == "Surds":
                surd = SurdQuestion()
                tex_ques, tex_ans = surd.questionCreator(data_param_difficulty, noofQuestions)

            elif chapter_name == "Sequence and Series":
                # this tells whether linear or quadratic or geometric
                data_param_difficulty["type"] = number_type
                s = SequenceSeriesQuestion()
                tex_ques, tex_ans = s.getQuestion[topic_name](data_param_difficulty,noofQuestions)
            elif topic_name == "Integration of Polynomials":
                calc_ques = CalculusQuestion()
                tex_ques, tex_ans = calc_ques.integrate_expr(data_param_difficulty, noofQuestions)
            elif topic_name == "Differentiation of Polynomials":
                calc_ques = CalculusQuestion()
                tex_ques, tex_ans = calc_ques.differentiate_expr(data_param_difficulty, noofQuestions)

            else:
                opq = OperationsQuestion()
                tex_ques, tex_ans = opq.multistepquestion(data_param_difficulty, noofQuestions)

            with open(settings.STATIC_ROOT+'/wstemplate.tex', 'r') as file:
                filedata = file.read()
                # Replace the target string
                filedata = filedata.replace('GRADE', "Grade 5")
                filedata = filedata.replace('CHAPTER', chapter_name)
                filedata = filedata.replace('TOPIC', topic_name)
                filedata = filedata.replace('DIFFICULTY', difficulty)
                filedata = filedata.replace('QUESTION', tex_ques)
                filedata = filedata.replace('ANSWER', tex_ans)
                filedata = filedata.replace('DESCRIPTION', description)

            # Write the file out again
            filename =  "Grade 5 "+chapter_name + " " + topic_name + " " + difficulty + " " + str(i + 1)

            with open(settings.STATIC_ROOT+'/'+ filename+ ".tex", 'w') as file:
                file.write(filedata)
            latex_to_pdf(filename)
            shutil.move(filename+".pdf",settings.STATIC_ROOT+'/pdf/'+filename+".pdf")
            os.remove(settings.STATIC_ROOT+'/'+filename+".tex")

def createWorksheet(chapter_name):
    f = open(settings.STATIC_ROOT+'/json/grade5.json', )
    data = json.load(f)
    noofQuestions = data["Parameters"]["noofquestions"]
    noofWorksheets = data["Parameters"]["noofworksheets"]
    chapter_json = data["Chapters"][chapter_name]
    #description = data["Chapters"][chapter_name]
    for topic_name in chapter_json:
        for difficulty in chapter_json[topic_name]:
            number_type = chapter_json[topic_name][difficulty]["num_type"]
            operations = chapter_json[topic_name][difficulty]["operation"]
            noofsteps = chapter_json[topic_name][difficulty]["noofsteps"]
            for i in range(noofWorksheets):
                opq = OperationsQuestion()
                tex_ques,tex_ans = opq.multistepquestion(number_type, operations,
                                                     data["Parameters"][difficulty],noofQuestions,noofsteps)
                with open('../../static/wstemplate.tex', 'r') as file:
                    filedata = file.read()

                # Replace the target string
                filedata = filedata.replace('GRADE', "Math")
                filedata = filedata.replace('CHAPTER', chapter_name)
                filedata = filedata.replace('TOPIC', topic_name)
                filedata = filedata.replace('DIFFICULTY', difficulty)
                filedata = filedata.replace('QUESTION', tex_ques )
                filedata = filedata.replace('ANSWER', tex_ans)
                #filedata = filedata.replace('DESCRIPTION', tex_ans)

                # Write the file out again
                filename = chapter_name+" "+topic_name+" "+difficulty+" "+str(i+1)+".tex"
                with open('dump/'+filename, 'w') as file:
                    file.write(filedata)
                latex_to_pdf(filename)
                os.remove('dump/' + filename)



#createWorksheetbyTopic("Numbers","Addition of Numbers")
#createWorksheetbyTopic("Numbers","Subtraction of Numbers")
#createWorksheetbyTopic("Numbers","Multiplication of Numbers")
#createWorksheetbyTopic("Numbers","Division of Numbers")
#createWorksheetbyTopic("Numbers","Mixed Operation of Numbers")
#createWorksheet("Numbers")
#createWorksheetbyTopic("Numbers","LCM HCF")

#createWorksheetbyTopic("Fractions","Addition of Fractions")
#createWorksheetbyTopic("Fractions","Subtraction of Fractions")
#createWorksheetbyTopic("Fractions","Multiplication of Fractions")
#createWorksheetbyTopic("Fractions","Division of Fractions")
#createWorksheetbyTopic("Fractions","Mixed Operation of Fractions")
#createWorksheetbyTopic("Decimals","Addition of Decimals")
#createWorksheetbyTopic("Decimals","Subtraction of Decimals")
#createWorksheetbyTopic("Decimals","Multiplication of Decimals")
#createWorksheetbyTopic("Decimals","Division of Decimals")
#createWorksheetbyTopic("Decimals","Mixed Operation of Decimals")
#createWorksheetbyTopic("Coordinate Geometry","Distance between two Points")
#createWorksheetbyTopic("Coordinate Geometry","Slope between two Points")
#createWorksheetbyTopic("Coordinate Geometry","Point of intersection between two lines")
#createWorksheetbyTopic("Coordinate Geometry","Equation of Perpendicular Bisector between two Points")
#createWorksheetbyTopic("Coordinate Geometry","Distance of Point from Line")
#createWorksheetbyTopic("Coordinate Geometry","Midpoint of two points")
#createWorksheetbyTopic("Coordinate Geometry","Equation of Line joining two Points")
#createWorksheetbyTopic("Algebra","Division")
#createWorksheetbyTopic("Algebra","Expansion")
#createWorksheetbyTopic("Algebra","Substitution of values")
#createWorksheetbyTopic("Numbers","Addition of Numbers")
#createWorksheetbyTopic("Complex Numbers","Addition of Complex Numbers")
#createWorksheetbyTopic("Complex Numbers","Addition of Complex Numbers")
#createWorksheetbyTopic("Complex Numbers","Subtraction of Complex Numbers")
#createWorksheetbyTopic("Complex Numbers","Multiplication of Complex Numbers")
#createWorksheetbyTopic("Complex Numbers","Division of Complex Numbers")

#createWorksheetbyTopic("Surds","Addition of Surds")
#createWorksheetbyTopic("Surds","Subtraction of Surds")
#createWorksheetbyTopic("Surds","Multiplication of Surds")
#createWorksheetbyTopic("Surds","Division of Surds")
#createWorksheetbyTopic("Numbers","Prime Factorization")
#createWorksheetbyTopic("Percentages","Compound Interest")
#createWorksheetbyTopic("Percentages","Simple Interest")
#createWorksheetbyTopic("Percentages","Profit Loss")
#createWorksheetbyTopic("Percentages","Percentage Increase Decrease")
#createWorksheetbyTopic("Percentages","Find Missing Value")
#createWorksheetbyTopic("Algebra","System of Linear Equations")
#createWorksheetbyTopic("Algebra","Addition of Variables")
#createWorksheetbyTopic("Algebra","Subtraction of Variables")
#createWorksheetbyTopic("Algebra","Making Subject")
#createWorksheetbyTopic("Algebra","Linear Equations")
#createWorksheetbyTopic("Algebra","Linear Inequality")
#createWorksheetbyTopic("Algebra","Quadratic Factorization")
#createWorksheetbyTopic("Algebra","Quadratic Equation")
#createWorksheetbyTopic("Algebra","Quadratic Inequality")
#createWorksheetbyTopic("Algebra","Expansion")
#createWorksheetbyTopic("Algebra","Division")
#createWorksheetbyTopic("Integration","Integration of Polynomials")
#createWorksheetbyTopic("Differentiation","Differentiation of Polynomials")
#createWorksheetbyTopic("Differentiation","Differentiation of Polynomials")
#createWorksheetbyTopic("Sequence and Series","Find Missing Terms in Geometric Series")
#createWorksheetbyTopic("Sequence and Series","Find Nth Term")
#createWorksheetbyTopic("Sequence and Series","Find Nth Term in Geometric Series")
#createWorksheetbyTopic("Sequence and Series","Find Nth Term Quadratic")
#createWorksheetbyTopic("Exponents","Indices Formulas")
#createWorksheetbyTopic("Shapes","Circle")
#createWorksheetbyTopic("Shapes","Square")
#createWorksheetbyTopic("Shapes","Rectangle")
#createWorksheetbyTopic("Shapes","Triangle")
#createWorksheetbyTopic("Shapes","Trapezium")
#createWorksheetbyTopic("Shapes","Cube")
#createWorksheetbyTopic("Shapes","Cuboid")
#createWorksheetbyTopic("Shapes","Cylinder")
#createWorksheetbyTopic("Shapes","Sphere")