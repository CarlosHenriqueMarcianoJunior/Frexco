from django.shortcuts import render
import random

# Create your views here.
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxz')

    length = int(request.GET.get("length"))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, '/cadastros',{"password":thepassword})