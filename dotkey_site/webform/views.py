from django.shortcuts import render, redirect
from .forms import ContactForm

def home_view(request):
    return render(request, "home.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("success")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

def success_view(request):
    return render(request, "success.html")
