from django.urls import path
from books.views import  home ,Booklistview , Bookdetail  , addBook , search_books


urlpatterns = [
    path('', home.as_view() , name = 'home'),
    path('Books/<str:category>/', Booklistview.as_view() , name = 'books list'),
    path('Books/<str:category>/<str:name>/', Bookdetail.as_view() , name = 'book detail'),
    path('/add_book/', addBook , name = 'add book'),
    path('search/', search_books, name='search_books'),


]
