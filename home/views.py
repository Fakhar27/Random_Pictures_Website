from django.shortcuts import render, HttpResponse
from home.models import Contact
from home.models import contacts
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'variable': 5
    }
    # messages.success(request, "THIS IS A TEST MESSAGE")
    return render(request, "index.html", context)
    # return HttpResponse("this is homepage")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        contact = contacts(name=name, email=email, text=text)
        contact.save()
        messages.success(request, "MESSAGE HAS BEEN SENT")
    return render(request, "contact.html")
