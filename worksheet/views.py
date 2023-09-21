from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from stocks import settings
from worksheet.algo.worksheetCreator import createWorksheetbyTopic

def tex_editor(filename,question,answer):
    with open(settings.STATIC_ROOT+'/'+'wstemplate.tex', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('QUESTION', question )
    filedata = filedata.replace('ANSWER', answer)

    # Write the file out again
    with open(settings.STATIC_ROOT+'/'+filename, 'w') as file:
        #print("i wrote the file")
        file.write(filedata)

@csrf_exempt
def ajax_ws(request):
    if request.method == 'POST':
        chapter = request.POST['chapter']
        topic = request.POST['topic']
        print("i am creating worksheet",chapter,topic)

        filename1 = "Grade 5 "+chapter+" "+topic+" Easy 1.pdf"
        filename2 = "Grade 5 " + chapter + " " + topic + " Medium 1.pdf"
        filename3 = "Grade 5 " + chapter + " " + topic + " Hard 1.pdf"
        createWorksheetbyTopic(chapter,topic)

        #template_name = filename
        #context = {'filename': filename_pdf}
        #http_response = render_to_pdf(request, template_name, context, filename='wstemplate.pdf')
        #return http_response
        return JsonResponse({
            'filename': [filename1,filename2,filename3]
        })

@csrf_exempt
def index(request):
    if request.method == 'POST':
        return ajax_ws(request)
    else:
        return render(request,'worksheets/index.html')

