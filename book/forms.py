#name, author,price,pages,category
from django import forms
from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class BookForm(forms.Form):
#     name=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Book Name'}),label='')
#     author=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Author Name'}),label='')
#     price=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Book Price'}),label='')
#     pages=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Number of Pages'}),label='')
#     category=forms.CharField(widget=forms.TextInput(attrs={'class':'text_inp','placeholder': 'Category'}),label='')
#
#     def clean(self):
#         cleaned_data=super().clean()
#         pages=cleaned_data.get("pages")
#         if int(pages)<10:
#             msg="Pages must be greater than 10"
#             self.add_error("pages",msg)



#django model form
class BookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__" #for all fields
        widgets={
            'book_name':forms.TextInput(attrs={'class':'text_inp','placeholder': 'Book Name'}),
            'author': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Author'}),
            'price': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Price'}),
            'pages': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Pages'}),
            'category': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Category'})
        }
        labels={
            'book_name':'',
            'author':'',
            'price':'',
            'pages':'',
            'category':''
        }
        def clean(self):
            cleaned_data=super().clean()

            book_name=cleaned_data.get("book_name")
            book=Book.objects.filter(book_name=book_name)
            if book:
                msg="Already Exists"
                self.add_error("book_name",msg)



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1","password2", "email"];



class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())