from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileUploadForm
from .models import UploadedFile

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_files')
    else:
        form = FileUploadForm()
    return render(request, 'notesUpload/index.html', {'form':form})


def my_files(request):
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'notesUpload/files.html', {'uploaded_files': uploaded_files})

def delete_file(request, file_id):
    file_to_delete = get_object_or_404(UploadedFile, pk=file_id)
    if request.method == 'POST':
        file_to_delete.file.delete()
        file_to_delete.delete()

    return redirect('my_files')