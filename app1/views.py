from django.shortcuts import render, HttpResponse, redirect
from .models import Book
# Create your views here.


def home(request):
    data = request.POST
    if request.method == 'POST':
        bid = data.get('b_id')
        name = data.get('b_name')
        author = data.get('b_author')
        price = data.get('b_price')
        quantity = data.get('b_quanty')
        is_published = data.get('b_published')
        is_active = data.get('b_active')
        if is_published == 'yes':
            is_published = True
        else:
            is_published = False
        if is_active == 'yes':
            is_active = True
        else:
            is_active = False
        Book.objects.create(name=name, author=author, price=price,
        qunty=quantity, is_pub=is_published, is_active=is_active)
        if not bid:
            # bk = Book.
            name = name



    return render(request, 'home.html')

def show_all_books(request):
    return render(request, 'show_data.html', context={'all_books': Book.objects.all()})

def all_inactive_books(request):
    return render(request, 'show_data.html', context={'all_books': Book.objects.filter(is_active=False), 'inactive':True})

def all_active_books(request):
    return render(request, 'show_data.html', context={'all_books': Book.objects.filter(is_active=True)})
def update_book(request, pk):
    return render(request, 'home.html', context={'single_book': Book.objects.get(id=pk)})

def soft_delete(request, pk):
    bk = Book.objects.get(id=pk)
    bk.is_active = False
    bk.save()
    return redirect('all_active_books')
def hard_delete(request, id):
    Book.objects.get(id=id).delete()
    return redirect('all_books')

def restore_book(request, pk):
    bk = Book.objects.get(id=pk)
    bk.is_active = True
    bk.save()
    return redirect('inactive_books')