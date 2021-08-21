from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .utils import welcome_email, email_check


def homepage(request):
    context={}
    return render (request=request, template_name="main/home.html", context=context)

def register_request(request):
    tmp = False
    form = False
    exists_mail = False
    if request.user.is_authenticated:
        return redirect('main:homepage')
    else:
        tmp = "main/register.html"
        if request.method == "POST":
            form = NewUserForm(request.POST)
            emailCheck = email_check(request.POST["email"])
            exists_mail = True if emailCheck else False
            if form.is_valid():
                user = form.save()
                login(request, user)
                # sending email but this is too much slow for local server
                welcome_email(user)
                messages.success(request, "Registration successful." )
                return redirect("main:homepage")
            messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
    return render (request=request, template_name=tmp, context={"register_form":form, "exists_mail":exists_mail})


def login_request(request):
    if request.user.is_authenticated:
        return redirect('main:homepage')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                print("form is valid")
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("main:homepage")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")