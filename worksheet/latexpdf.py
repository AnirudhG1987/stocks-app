from django_tex.core import compile_template_to_pdf
from django.conf import settings

settings.configure()
template_name = '\sample.tex'
context = {'foo': 'Bar'}
PDF = compile_template_to_pdf(template_name, context)


