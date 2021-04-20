from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='index'),
    path('book/create/', views.CreateBook.as_view(), name='book_create'),
    path('book/delete/', views.DeleteBook.as_view(), name='book_delete'),
    path('book/update/', views.UpdateBook.as_view(), name='book_update'),
]
