from django.shortcuts import render
from .forms import TeacherForm
from .models import Teacher

def home(request):
    teachers = Teacher.objects.all()  # show list of teachers if any
    return render(request, 'home.html', {'teachers': teachers})

def add_teacher(request):
    message = ""
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Teacher saved successfully!"
        else:
            message = "Error: Please check the form."
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form, 'message': message})
