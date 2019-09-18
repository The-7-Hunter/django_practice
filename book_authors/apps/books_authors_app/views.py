from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def index_for_authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, 'books_authors_app/authors.html', context)

def book_info(request, book_id):
    context = {
        "books": Book.objects.get(id = book_id),
        "authors": Book.objects.get(id = book_id).authors.all(),
        "auth_not_related": Author.objects.all()
    }
    return render(request, 'books_authors_app/book_info.html', context)

def add_book(request):
    if len(request.POST['title']) < 1:
        return redirect("/") 
    newBook = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect("/")

def append_authors(request, book_id):
    isThere = Book.objects.get(id = book_id).authors.all()
    selected = Author.objects.get(id = request.POST['select_author'])
    if selected in isThere:
        return redirect("/")
    Book.objects.get(id = book_id).authors.add(selected)
    return redirect(f"/book_info/{book_id}")

def author_info(request, author_id):
    context = {
        "author": Author.objects.get(id = author_id),
        "book": Author.objects.get(id = author_id).books.all(),
        "books_not_related": Book.objects.all()
    }
    return render(request, 'books_authors_app/author_info.html', context)

def add_author(request):
    if len(request.POST['first_name']) < 1 or len(request.POST['last_name']) < 1:
        return redirect("/") 
    newAuth = Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect("/authors")

def append_books(request, author_id):
    isThere = Author.objects.get(id = author_id).books.all()
    selected = Book.objects.get(id = request.POST['select_book'])
    if selected in isThere:
        return redirect("/authors")
    Author.objects.get(id = author_id).books.add(selected)
    return redirect(f"/author_info/{author_id}")