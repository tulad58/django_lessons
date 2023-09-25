from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator

# page_number = int(request.GET.get('page', 1))
# paginator = Paginator(csv_data, per_page=10)
# page = paginator.get_page(page_number)

def books_view(request):
    template = 'books/books_list.html'
    books_dates_obj = Book.objects.all()
    context = {'books': books_dates_obj}
    return render(request, template, context)


def books_date_view(request, date):
    template = 'books/books_pagination.html'
    books_dates_obj = Book.objects.order_by('pub_date').all()
    list_of_dates = []
    for i in range(len(books_dates_obj)):
        list_of_dates.append(books_dates_obj.values_list()[i][3])

    paginator = Paginator(list_of_dates, per_page=1)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    books_items = Book.objects.filter(pub_date=date).all()
    context = {'books': books_items,
               'page': page}
    return render(request, template, context)
