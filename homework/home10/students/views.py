from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def home(request):
    return render(request, 'home.html')

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_create.html', {'form': form})

def student_update(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_update.html', {'form': form})

def student_delete(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_delete.html', {'student': student})

def student_list(request):
    students = Student.objects.all().order_by('id')
    return render(request, 'student_list.html', {'students': students})

def student_search(request):
    query = request.GET.get('q')
    results = Student.objects.filter(name__icontains=query) if query else []
    return render(request, 'student_search.html', {'results': results, 'query': query})
