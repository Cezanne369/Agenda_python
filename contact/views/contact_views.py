from django.shortcuts import get_object_or_404, render

from contact.models import Contact


def index(request):# type:ignore
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[10:20]

    context = {# type:ignore
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,# type:ignore
        'contact/index.html',
        context# type:ignore
    )


def contact(request, contact_id):# type:ignore
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = { # type:ignore
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,# type:ignore
        'contact/contact.html',
        context # type:ignore
    )