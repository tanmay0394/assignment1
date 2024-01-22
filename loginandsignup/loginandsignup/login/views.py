# views.py
from django.shortcuts import render
from .models import User

def loginaction(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        # Use Django ORM to query the User model
        try:
            user = User.objects.get(email=email, password=password)
            return render(request, 'welcome.html')
        except User.DoesNotExist:
            return render(request, 'error.html')

    return render(request, 'login_page.html')
