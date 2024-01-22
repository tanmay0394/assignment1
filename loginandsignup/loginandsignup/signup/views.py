from django.shortcuts import render
from .models import User  # Assuming you have a User model in your models.py

def signaction(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        sex = request.POST.get("sex", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        # Create a new User object and save it to the database
        user = User(first_name=first_name, last_name=last_name, sex=sex, email=email, password=password)
        user.save()

    return render(request, 'signup_page.html')
