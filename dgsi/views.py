from django.shortcuts import render
from .models import StudentInfo

# Create your views here.
def home(request):
    students = StudentInfo.objects.all()

    return render(request, 'home.html',{
        'students' : students
    })