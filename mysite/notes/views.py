from datetime import datetime

from django.shortcuts import render, redirect
from .models import Note


# Create your views here.


def login(request):
    return render(request, 'login.html')


def home(request):

    if 'message' in request.POST and request.POST['message']:
        print("form is submitted.")
        p1 = request.POST['message']

        Notes_note = Note(note_text=p1, update=datetime.now(), last_up_date=datetime.now())
        Notes_note.save()



    return render(request, 'index.html')


def index(request):
    return redirect(request, '/')


def view_status(request):
    all_notes= Note.objects.all()
    return render(request, 'status.html', {'notes':all_notes})


def update(request):
    return render(request, 'update.html')



