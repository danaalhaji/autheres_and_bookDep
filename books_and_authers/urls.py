from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('proccessAddBook', views.addBook),
    path('book/<int:id>', views.detailsB),
    path('addAutherBook/<int:id>', views.addAutherToBook),
    path('author',views.viewAuthor),
    path('author/proccessAddAuthor', views.addAuthor),
    path('author/<int:id>', views.detailsAuthor),
    path('author/addBookAuther/<int:id>', views.addBooksToAuthor),
]