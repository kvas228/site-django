from django.shortcuts import render,redirect
from .models import zakazi
from .forms import zakaziForm
from .models import articles
from django.views.generic import DetailView, ListView
from distutils.log import error
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import ImageForm

def index(request):
    return render(request,'main/index.html', {'nombre':'Имена','otziv':zakazi})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})
def index1(request):
    return render(request,'main/about.html')

def index2(request):
    error = ''
    if request.method == 'POST':
        form = zakaziForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Дерьмо санное не работает'
    form = zakaziForm
    contex = {
        'form': form
    }
    otziv = zakazi.objects.order_by('-id')[:4]
    return render(request,'main/comments.html',{'nombre':'Имена','otziv':otziv,})

def index3(request):
    error = ''
    if request.method == 'POST ':
        form = zakaziForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'error'
    form = zakaziForm
    contex = {
        'form': form
    }
    otziv = zakazi.objects.order_by('-id')[:4]
    return render(request, 'main/new.html')
def m1(request):
    return render(request,'main/m1.html')
def m2(request):
    return render(request,'main/m2.html')
def m3(request):
    return render(request,'main/m3.html')