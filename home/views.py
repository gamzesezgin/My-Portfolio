from django.shortcuts import render, redirect

from . models import Mail

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def aboutme(request):
    return render(request, 'home/aboutme.html')

def contact(request):
    return render(request, 'home/contact.html')

def getCoursesByCategory(request, category):
    return render(request, 'home/home.html')

def submit_contact_form(request):

    if request.method == "POST":
        mail = request.POST.get("mail")
        message = request.POST.get("message")

        Mail.objects.create(mail=mail, message=message)

        return redirect("success_page")
    
    return render(request, "contact.html")