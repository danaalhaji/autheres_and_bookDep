from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponse
from .models import *
# render the books page 
def root(request):
    context={
        'Books' : Book.objects.all(),
    }
    return render(request,"addBook.html",context)
#  adding books and redirect to the book page
def addBook(request):
    titleB = request.POST['TitleInput']
    descB = request.POST['DescInput']
    book=Book.objects.create(title=titleB,describtion=descB)
    book.save()
    return redirect("/")
# render the book derails and it's authors 
def detailsB(request, id):
    context={
        'Book' : Book.objects.get(id=int(id)),
        'Authors': Author.objects.all()
    }
    return render(request,"bookDetail.html",context)
# define the relation many to many and authors to book
def addAutherToBook(request,id):
    book = Book.objects.get(id=int(id))
    author = Author.objects.get(id=request.POST['AutherOptions'])
    book.Authers.add(author)
    return redirect("/book/" + str(id))
# render the authors table and the form
def viewAuthor(request):
    context={
        'Authors' : Author.objects.all()
    }
    return render(request, "addAuthor.html",context)
# allow adding authors to the author model
def addAuthor(request):
    author = Author.objects.create(first_name = request.POST['authorFirst'], last_name = request.POST['authorLast'])
    author.save()
    return redirect('/author')
# render the author details 
def detailsAuthor(request, id):
    context={
    'Author': Author.objects.get(id=int(id)),
    'Books' : Book.objects.all()
    }
    return render (request, 'authorDetails.html',context)
# allow adding books to author
def addBooksToAuthor(request, id):
    author= Author.objects.get(id=int(id))
    book = Book.objects.get(id = request.POST['booksOptions'])
    book.Authers.add(author)
    return redirect("/author/" + str(id))

# Create your views here.
