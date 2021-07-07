"""bookProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import createBook,list_all_book,book_details,delete_book,update_book
from .views import registration,login_user,signout,user_home,\
BookList,BookCreate,BookDetail,BookUpdate,BookDelete,\
ListBook,CreateBook,DetailBook,UpdateBook,DeleteBook


urlpatterns = [
    path("create",createBook,name="createbook"),
    path("list",list_all_book,name="list"),
    path("detail/<int:id>",book_details,name="detail"),
    path("delete/<int:id>",delete_book,name="deletebook"),
    path("edit/<int:id>", update_book, name="bookupdate"),
    path("registration",registration,name="register"),
    path("login",login_user,name="userlogin"),
    path("logout",signout,name="signout"),
    path("home",user_home,name="userhome"),
    path("booklist",BookList.as_view(),name="booklist"),
    path("bookcreate",BookCreate.as_view(),name="bookcreate"),
    path("books/<int:pk>",BookDetail.as_view(),name="bookview"),
    path("update/<int:pk>", BookUpdate.as_view(), name="bookedit"),
    path("deletebook/<int:pk>",BookDelete.as_view(),name="delete"),
    path("tbooklist", ListBook.as_view(), name="tbooklist"),
    path("tbookcreate",CreateBook.as_view(),name="tbookcreate"),
    path("tbooks/<int:pk>",DetailBook.as_view(),name="tbookview"),
    path("tupdate/<int:pk>", UpdateBook.as_view(), name="tbookedit"),
    path("tdeletebook/<int:pk>",DeleteBook.as_view(),name="tdelete"),
]
