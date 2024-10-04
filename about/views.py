from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()  # Ensure `about` is always set
    collaborate_form = CollaborateForm()  # Initialize form for both GET and POST

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
    
    return render(
        request,
        "about/about.html",
        {
            "about": about,  # Ensure about is passed in all cases
            "collaborate_form": collaborate_form
        },
    )
