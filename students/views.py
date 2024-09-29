from django.shortcuts import render
from .models import AddStudents
# Create your views here.
def student_list(request):
    return render(request, "students.html")

def all_students(request):
    all_students = AddStudents.objects.all()
    return render(request, "all_students.html",{"students": all_students})