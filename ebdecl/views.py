from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime


menu = {'Главная':3,'Компании': 'company','Декларации': 'decl','Отчеты':1,'Авторизация':2}

ef index(request):
   decls = Decl.objects.all()
   form = AddDecl()
   datenow = datetime.date.today()
   print(datenow)
   return render(request, 'ebdecl/index.html', {'datenow':datenow,'form': form, 'menu':menu, 'decls': decls, 'title': 'Главная страница'})

def firms(request):
    return HttpResponse("<h1>Клиенты</h1>")

# Create your views here.
def decladd(request):
    decls = Decl.objects.all()

    if request.method == 'POST':
        form = AddDecl(request.POST)
        if form.is_valid():
            try:
                Decl.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка записи')
    else:
        form = AddDecl()
    return render(request, 'ebdecl/decladd.html', {'form': form, 'menu':menu, 'decls': decls, 'title': 'Декларации'})

