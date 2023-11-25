from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Folder, Task

def index(request, id):
    folders = Folder.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    current_folder = get_object_or_404(Folder, id=id)
    tasks = Task.objects.filter(folder_id=current_folder.id)
    return render(request, 'index.html', {
        'folders': folders,
        'tasks': tasks,
        'current_folder_id': current_folder.id,
        })