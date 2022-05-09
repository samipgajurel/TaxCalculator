from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserModel

# Create your views here.
def dashboard_page (request):
    # Get the index template file absolute path.
    # index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    return render(request, 'UserDashboard2.html')

def login_page (request):
    if request.method == "GET":
        form = UserModel()
    else:
        form = UserModel(request.POST)
        if form.is_valid():
            # user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

    # return render(request,'login.html')
    return render(request, 'login.html', {'form': form})

def signup_page(request):
    if request.method == "GET":
        form= SignUpForm()
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('/accounts/login')
    return render(request, 'SignUpPage.html', {'form': form})



