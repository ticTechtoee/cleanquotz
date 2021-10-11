from django.shortcuts import render


def index(request):
    return render(request, 'Tutorial/Tutorial.html')
