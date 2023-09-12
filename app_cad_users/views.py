from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'app_cad_users/home.html')

def users(request):
    new_user = User()
    new_user.nome = request.POST.get('nome')
    new_user.idade = request.POST.get('idade')
    new_user.save()
    context={'users': User.objects.all() }
    return render(request, 'app_cad_users/users.html', context)