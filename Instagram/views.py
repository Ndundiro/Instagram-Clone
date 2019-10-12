from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'jghjg',
        'image':'image',
        'caption':'caption',
        'comment':'comment'
    }
]



def home(request):
    return render(request, 'index.html', {'posts':posts})


def about(request):
    return render (request, 'about.html')
