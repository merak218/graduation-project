from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from account.models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'index.html', context)

def stream(request):
    return render(request, 'live_streaming.html')