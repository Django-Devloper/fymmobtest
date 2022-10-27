from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def Login(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            if request.method == 'GET':
                fm = AuthenticationForm()
                return render(request, 'login.html', {'form': fm})

            if request.method == 'POST':
                fm = AuthenticationForm(request=request, data=request.POST)
                if fm.is_valid():
                    uname = fm.cleaned_data['username']
                    passwd = fm.cleaned_data['password']
                    user = authenticate(username=uname, password=passwd)
                    if user is not None:
                        login(request, user)

                    return HttpResponseRedirect('/')

                else:
                    fm = AuthenticationForm()
                    return render(request, 'login.html', {'form': fm})



def Logout_User(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
