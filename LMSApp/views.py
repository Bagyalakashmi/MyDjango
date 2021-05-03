from django.shortcuts import render, redirect

from LMSApp.forms import RegisterForm, BookForm
from LMSApp.models import Register, Book


# Create your views here.
def RegisterView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/display/")
    return render(request, "templates/register.html", {"register": form})


def Retrieve_view(request):
    form = Register.objects.all()
    return render(request, "templates/display.html", {"display": form})


def Delete_view(request, pk):
    form = Register.objects.all().get(pk=pk)
    form.delete()
    return redirect("/display/")


def Update_view(request, pk):
    student = Register.objects.all().get(pk=pk)
    if request.method == 'POST':
        print("i am rinning1...")
        form = RegisterForm(request.POST, instance=student)
        if form.is_valid():
            print("i am rinning2...")
            print(form.error_class)
            form.save()
            return redirect("/display/")
    return render(request, "templates/update.html", {"update": student})


def AddBook_View(request):
    book = BookForm()
    if request.method == 'POST':
        book = BookForm(request.POST)
        if book.is_valid():
            book.save()
            return redirect("/addBook/")
    return render(request, "templates/addBook.html", {"bookData": book})


def showBook_view(request):
    all_book = Book.objects.all()
    return render(request, "templates/showBook.html", {"show": all_book})


def bookDelete_view(request, pk):
    delete_book = Book.objects.all().get(pk=pk)
    delete_book.delete()
    return redirect("/showBook/")


def BookUpdate_view(request, pk):
    update_book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        update = BookForm(request.POST, instance=update_book)
        if update.is_valid():
            update_book.save()
            return redirect("/showBook/")
    return render(request, "templates/bookUpdate.html", {"update": update_book})


def Home(request):
    return render(request, "templates/home.html")


# def showMember_view(request):
#     add_member = MembershipForm()
#     if request.method == 'POST':
#         add_member = Membership(request.POST)
#         if add_member.is_valid():
#             add_member.save()
#             return redirect("/addMember/")
#     return render(request, "templates/addMember.html", {"member": add_member})
