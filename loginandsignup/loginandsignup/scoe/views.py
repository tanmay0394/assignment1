from django.shortcuts import render
from .models import Student

def seating_arrangement(request):
    students = Student.objects.all().order_by('seat_number')
    return render(request, 'seating_arrangement.html', {'students': students})
