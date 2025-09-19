from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm

def teacher_list(request):
    teachers = Teacher.objects.all()
    message = "Welcome to Teachers Page!"
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers, 'message': message})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers:teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/add_teacher.html', {'form': form})
