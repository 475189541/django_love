from django.shortcuts import render

# Create your views here.


def save_me(request):
    return render(request, 'save_me/index.html')


def marry_my(request):
    return render(request, 'marry_my/index.html')

