from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            uploaded_file = request.FILES.get("id_card")

            if uploaded_file:
                file_type = uploaded_file.name.split('.')[-1].lower()
                if file_type not in IMAGE_FILE_TYPES:
                    messages.error(request, "Only .png, .jpg, and .jpeg files are supported.")
                    return redirect("register_student")

                student.id_card = uploaded_file
                student.save()
                messages.success(request, "Registration successful!")
                return redirect("register_student")
            else:
                messages.error(request, "Please upload an ID card image.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentForm()
    
    return render(request, "register.html", {"form": form})
