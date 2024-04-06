from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username and password:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,("you were successfully logged in"))
            return render(request,'tss/index.html',{'user':user})
        else:
            messages.success(request,("Password or Username is incorrect"))
            return redirect('account:login_user')

    return render(request, 'account/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("you were successfully logged out"))
    return redirect('home')


def signup(request):
    print(request.method)
    if request.method == 'POST':
        print("signup successfully")
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("User created successfully")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("you have successfully created a new account"))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html',{'form': form})

