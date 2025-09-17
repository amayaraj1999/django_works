from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookForm
from .models import Books

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_books.html', {'form': form})

def book_list(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'books': books})