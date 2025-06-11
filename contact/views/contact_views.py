from django.shortcuts import render
from contact.models import Contact


# Create your views here.
def index(request): # type: ignore
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }   
    return render(
        request, # type: ignore
        'contact/index.html',
        context,
    )