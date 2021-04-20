from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Book


class BookList(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'


class DeleteBook(DeleteView):
    def get(self, request):
        id = request.GET.get('id')
        book = get_object_or_404(Book, id=id)
        book.delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class CreateBook(CreateView):
    def get(self, request):
        name = request.GET.get('name')
        author = request.GET.get('author')
        year = request.GET.get('year')
        last_book = Book.objects.create(
            name=name,
            author=author,
            year=year
        )
        new_book_data = {
            'id': last_book.id,
            'name': name,
            'author': author,
            'year': year,
        }
        return JsonResponse({'book': new_book_data})


class UpdateBook(UpdateView):
    def get(self, request):
        id = request.GET.get('id')
        book = get_object_or_404(Book, id=id)
        book.name = request.GET.get('name')
        book.author = request.GET.get('author')
        book.year = request.GET.get('year')
        book.save()
        updated_book_data = {
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'year': book.year,
        }
        return JsonResponse({'book': updated_book_data})
