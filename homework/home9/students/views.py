from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    message = "Welcome to Students Page!"
    return render(request, 'students/student_list.html', {'students': students, 'message': message})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})
