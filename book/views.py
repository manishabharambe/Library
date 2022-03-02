from email.policy import HTTP
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def homepage(request):      ## request --  httprequest
    print(request.POST)
    # print(request.method)           ## o/p- GET
    # print(request.GET)      # to see data entered...will give empty dictionary
    # print(request.POST)     # will print dictionary of data entered  o/p-<QueryDict: {'csrfmiddlewaretoken': ['b11T4STPWblfIqsT0wGD50PtqBOcre1FltGSEGgsnH79vR8ZzxaP78pjkgiQOQwc'], 'b_name': ['nisha'], 'b_price': ['9877'], 'b_qty': ['32']}>
    # print(request.build_absolute_uri())     ## o/p-- http://127.0.0.1:8000/home/
    # return HttpResponse("<h2> Hi Hello </h2>""<h5> Manisha </h5>")

    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")
    is_available = request.POST.get("available")
        
    if request.method == "POST":
        if not request.POST.get("bid"):
            book_name = name #,False)
            book_price = price  #,False)
            book_qty = qty#,False)
            book_available = is_available
            # print(book_name,book_price,book_qty)
            Book.objects.create(name=book_name,price=book_price,qty=book_qty,is_available=book_available)
            return redirect("homepage")
        else:
            bid = request.POST.get("bid")
            try:
                book_obj = Book.objects.get(id=bid)
                book_obj.name = name
                book_obj.price = price
                book_obj.qty = qty
                book_obj.is_available = is_available
                book_obj.save()
                return redirect("show_all_books")
            except Book.DoesNotExist as msg:
                print(msg)
            

    elif request.method == "GET":
        return render(request,template_name="home.html") 
    # return HttpResponse("<h3>Hello</h3>")

def show_all_books(request):
    all_data = Book.objects.all()
    # print(all_data)
    data = {"Books":all_data}
    return render(request,template_name="show_all_books.html",context = data)

def soft_delete_pg(request):
    all_data = Book.activeobjects.is_available()
    # print(all_data)
    data = {"Books":all_data}
    return render(request,template_name="soft_delete_pg.html",context = data)

def edit_data(request,id):   ## as will fetch with id
    book = Book.objects.get(id=id)
    return render(request,template_name="home.html",context={"single_book": book})
import traceback
def delete_data(request, id):
    if request.method == "POST":        # form madhun delete hoil just through delete button as we have give post method. directly url thr will give else part i.e error occured            
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as error:  # this will just print msg..if we want detailed error then use traceback
            # print(error)
            traceback.print_exc()
            return HttpResponse("Book does not exist")
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse("Error Ocured")

def show_book_bootstrap(request):
    all_books = Book.objects.all()
    data = {"books": all_books}
    return render(request, "show_book_bootstrap.html", context=data)

def login(request):
    return render(request,template_name="login.html")
def delete_all_books(request):
    if request.method == "POST":        # form madhun delete hoil just through delete button as we have give post method. directly url thr will give else part i.e error occured            
        try:
            book = Book.objects.all()
        except Book.DoesNotExist as error:  # this will just print msg..if we want detailed error then use traceback
            # print(error)
            traceback.print_exc()
            return HttpResponse("Book does not exist")
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse("Error Ocured")

def soft_delete(request,id):
    if request.method =='POST':
        try:
        # data = Book.objects.get(id=id)
            book = Book.activeobjects.get(id=id)
        except:  # this will just print msg..if we want detailed error then use traceback
            # print(error)
            traceback.print_exc()
            return HttpResponse("Book does not exist")
        else:
            book.delete()
            return redirect("show_all_books.html")
    else:
        return HttpResponse("Error Ocured")


def soft_delete_all(request):
    if request.method == 'POST':
        all_data = Book.activeobjects.is_available()
        data={"books": all_data}
        # return render(request,template_name="soft_delete_pg.html")
    return render(request,template_name="soft_delete_pg.html",context=data)
"""
def book_list(request):
    return render(request,"book_list.html")
"""

