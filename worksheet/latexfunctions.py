from pdflatex import PDFLaTeX
from stocks import settings
import shutil, os
from tex import latex2pdf

def latex_to_pdf(filename):
    #print(filename)
    pdfl = PDFLaTeX.from_texfile( settings.STATIC_ROOT+'/'+filename+".tex")
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
    #print("hi")
    filename_pdf = filename+'.pdf'
    shutil.move(filename_pdf,settings.STATIC_ROOT+'/pdf/'+filename_pdf)
    #print("hello")
    return filename_pdf

#latex_to_pdf('sample.tex')