from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import UploadedFile

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_upload')
    else:
        form = FileUploadForm()
    files = UploadedFile.objects.all()
    return render(request, 'upload_download/upload_download.html', {'form': form, 'files': files})

def delete_file(request, pk):
    if request.method == 'POST':
        file = UploadedFile.objects.get(pk=pk)
        file.file.delete()  # Delete the actual file
        file.delete()  # Delete the model instance
        return redirect('file_upload')