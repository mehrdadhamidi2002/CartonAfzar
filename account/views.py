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
            messages.success(request,("شما با موفقیت وارد شدید."))
            return render(request,'tss/index.html',{'user':user})
        else:
            messages.success(request,("Password or Username is incorrect"))
            return redirect('account:login_user')

    return render(request, 'account/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("شما با موفقیت خارج شدید"))
    return redirect('tss:home')


def signup(request):
    print(request.method)
    if request.method == 'POST':
        print("signup successfully")
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False
            user.save()
            print("User created successfully")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("شما موفق به ساخت اکانت خود شدید."))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html',{'form': form})





