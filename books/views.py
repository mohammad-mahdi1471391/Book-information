from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.db.models import Q
import random

import users
from .models import Category , Book
from .srializers import CategorySerializer , BookSerializer
from .forms import addbook

# Create your views here.


class home(APIView):
    def get(self, request):

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        book = list(Book.objects.all())
        books_random = random.sample(book , min(20, len(book)))
        serializer2 = BookSerializer(books_random, many=True)
        context = {
            'categories': serializer.data,
            'books': serializer2.data,
        }

        return render(request, 'books/home.html', context)



class Booklistview(APIView):
    def get(self , request , category):
        book = Book.objects.filter(Categoris__name=category)
        serializer = BookSerializer(book, many=True )
        return render (request , 'books/books_list.html' , {'books':serializer.data})






class Bookdetail(APIView):
    def get(self , request ,category, name):
        try:
            book = Book.objects.get(Categoris__name = category ,name = name)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Book.MultipleObjectsReturned:
            return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
        serializer = BookSerializer(book)
        books =list(Book.objects.exclude(pk=book.pk))
        books_random = random.sample(books , 10)
        serializer2 = BookSerializer(books_random, many=True )
        context = {
            'book': serializer.data,
            'book2': serializer2.data
        }
        return render(request, 'books/book.html', context)





def addBook(request):
    if  not request.user.is_authenticated:
        return redirect('users-login')
    if request.method == 'POST':
        form = addbook(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            newbook = Book(
                name = data['name'],
                author = data['author'],
                Categoris = data['table'],
                text = data['overview'],
                img = data.get('image'),
                created = data.get('created')
            )
            newbook.save()
            messages.success(request, f'{newbook.name} Book Added Successfully')
            return redirect("home")

    else:
        form = addbook()

    return render(request, 'books/add_book.html' , {'form': form})



def search_books(request):
    query = request.GET.get('q', '').strip()

    books = Book.objects.none()

    if query:
        books = Book.objects.filter(
            Q(name__icontains=query) |
            Q(author__icontains=query) |
            Q(text__icontains=query) |
            Q(Categoris__name__icontains=query)

        )

    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)

    context = {
        'books': books,
        'query': query,
        'categories': serializer.data,
    }

    return render(request, 'books/search_results.html', context)

