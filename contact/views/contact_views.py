from django.shortcuts import render

# Create your views here.
def index(request): # type: ignore
    return render(
        request, # type: ignore
        'contact/index.html',
    )