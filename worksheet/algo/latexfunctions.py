import pdflatex

import os
from stocks import settings

def latex_to_pdf(filename):
    pdfl = pdflatex.PDFLaTeX.from_texfile(settings.STATIC_ROOT + '/' + filename + ".tex")
    pdfl.create_pdf(keep_pdf_file=True,keep_log_file=False)
    #pass
#latex_to_pdf("Algebra Linear Inequality Easy 1.tex")