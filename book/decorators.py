from django.shortcuts import redirect


def login_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            return redirect("userlogin")
    return wrapper

def user_admin(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return func(request,*args,**kwargs)
        else:
            return redirect("userlogin")
    return wrapper