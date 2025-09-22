from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import BookForm
from .models import Books

def home(request):
    return render(request, 'home.html')

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list_paginated')
    else:
        form = BookForm()
    return render(request, 'create.html', {'form': form})

def book_read(request):
    book_list = Books.objects.all()
    return render(request, 'retrieve.html', {'book_list': book_list})

def book_list_paginated(request):
    book_list = Books.objects.all().order_by('id')
    paginator = Paginator(book_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'retrieve.html', {'page_obj': page_obj})

def book_update(request, id):
    book = Books.objects.get(pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list_paginated')
    else:
        form = BookForm(instance=book)
    return render(request, 'update.html', {'form': form})

def book_delete(request, id):
    book = Books.objects.get(pk=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list_paginated')
    return render(request, 'delete.html', {'book': book})
