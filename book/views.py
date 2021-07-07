from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from .decorators import login_required,user_admin
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
# Create your views here.


@login_required
@user_admin
def createBook(request):
    context={}
    form=BookForm()
    context["form"]=form
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            # name=form.cleaned_data.get("name")
            # author=form.cleaned_data.get("author")
            # price=form.cleaned_data.get("price")
            # pages=form.cleaned_data.get("pages")
            # category=form.cleaned_data.get("category")
            # book=Book(book_name=name,author=author,price=price,pages=pages,category=category)
            # print("Saved")
            # book.save()
            form.save()

            return redirect("list")

        else:
            form = BookForm(request.POST)
            context["form"] = form
            return render(request, "book/create_book.html", context)
    return render(request,"book/create_book.html",context)

@login_required
def list_all_book(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"book/listallBook.html",context)

@login_required
def book_details(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/book_view.html",context)

@login_required
@user_admin
def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("list")

@login_required
@user_admin
def update_book(request,id):
    book=Book.objects.get(id=id)
    # book_det={
    #     "name":book.book_name,
    #     "author":book.author,
    #     "price":book.price,
    #     "pages":book.pages,
    #     "category":book.category
    # }
    form=BookForm(instance=book);
    context={}
    context["form"]=form
    if request.method == "POST":
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            # name = form.cleaned_data.get("name")
            # author = form.cleaned_data.get("author")
            # price = form.cleaned_data.get("price")
            # pages = form.cleaned_data.get("pages")
            # category = form.cleaned_data.get("category")
            # book.book_name=name
            # book.author=author
            # book.price=price
            # book.pages=pages
            # book.category=category
            # book.save()
            form.save()
            return redirect("list")

    return render(request,"book/edit_book.html",context)


def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"] = form
    return render(request,"book/registration.html",context)


def login_user(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                # return render(request,"book/index.html")
                return redirect("userhome")

    return render(request,"book/login.html",context)

def signout(request):
    logout(request)
    return redirect("userlogin")

@login_required
def user_home(request):
    return render(request,"book/index.html")


#class based views
class BookList(ListView):
    model = Book
    template_name = "book/listallBook.html"
    context_object_name = "books"


class BookCreate(CreateView):
    model=Book
    template_name = "book/create_book.html"
    form_class=BookForm
    success_url = reverse_lazy("booklist")

class BookDetail(DetailView):
    model = Book
    template_name = "book/book_view.html"
    context_object_name = "book"

class BookUpdate(UpdateView):
    model=Book
    form_class=BookForm
    template_name = "book/edit_book.html"
    success_url = reverse_lazy("booklist")

class BookDelete(DeleteView):
    model=Book
    template_name = "book/deletebook.html"
    success_url = reverse_lazy("booklist")
    context_object_name = "book"

class ObjectMixin(object):
    model=None
    def get_object(self,id):
        return self.model.objects.get(id=id)


class ListBook(TemplateView):
    model=Book
    template_name = "book/listallBook.html"
    context={}
    def get(self, request, *args, **kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)

class CreateBook(TemplateView):
    model=Book
    template_name = "book/create_book.html"
    context={}
    form_class=BookForm
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class
        return render(request,self.template_name,self.context)
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tbooklist")
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)

class DetailBook(TemplateView,ObjectMixin):
    model=Book
    template_name = "book/book_view.html"
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        book=self.get_object(id)
        self.context["book"]=book
        return render(request,self.template_name,self.context)

class UpdateBook(TemplateView,ObjectMixin):
    model=Book
    template_name = "book/edit_book.html"
    form_class=BookForm
    context={}
    lookup=0
    # def get_object(self,id):
    #     return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        self.lookup=kwargs.get("pk")
        book=self.get_object(self.lookup)
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,**kwargs):
        self.lookup = kwargs.get("pk")
        book = self.get_object(self.lookup)
        form=self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("tbooklist")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)


class DeleteBook(TemplateView,ObjectMixin):
    model=Book
    # def get_object(self,id=id):
    #     return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        book=self.get_object(id)
        book.delete()
        return redirect("tbooklist")

