from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render,redirect

def signin_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/proj/")
    else:
        form  = UserCreationForm()
    return render(request, 'accounts/signin.html', {"form":form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/proj/')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {"form":form})

@login_required()
def logout_view(request):
    logout(request)
    return redirect('/proj/')
