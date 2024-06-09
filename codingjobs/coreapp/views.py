from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth import logout

# from django.contrib.auth.views import LogoutView

# def logout(request):
#     if request.method == 'POST':
#         return LogoutView.as_view(next_page='login')
#     else:
#         return render(request, 'user_auth/coreapp/logout.html')

def frontpage(request):
    return render(request, 'coreapp/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
           user = form.save()
           login(request, user)
           
           return redirect('frontpage')

    else:
        form = UserCreationForm()

    return render(request, 'coreapp/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('frontpage')
