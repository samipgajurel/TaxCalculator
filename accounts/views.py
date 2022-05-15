from django.contrib.auth import login, authenticate
from .forms import SignUpForm,ProfileForm
from django.shortcuts import render, redirect
from .models import Profile
from .service import get_total_users,get_total_admins
from news.service import get_total_news,get_news_this_week

# Create your views here.
def dashboard_page (request):
    # Get the index template file absolute path.
    # index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    currentUser= request.user
    account= Profile.objects.get(user=currentUser)
    print(account.first_name)
    if account.first_name is not None and len(account.first_name)>0:
        if currentUser.is_superuser:
            total_users= get_total_users()
            total_admins= get_total_admins()
            return render(request, 'AdminDashboard.html', {"account": account,
                                                           'total_users':total_users,
                                                           'total_admins':total_admins,
                                                           'total_news':get_total_news(),
                                                           "total_news_this_week":get_news_this_week()})
        else:
            return render(request, 'UserDashboard.html', {"account": account})
    else:
        form= ProfileForm()
        next= "/accounts/dashboard"
        return render(request, 'EditProfile.html', {"form": form,"next":next})

def profile_page(request):
    next = "/accounts/dashboard"
    user = request.user
    profile= Profile.objects.get(user=user)
    print(user)
    if request.method == "GET":
        form= ProfileForm(instance=profile)
    else:
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            user.refresh_from_db()
            if user.profile is None:
                print('profileMissing')

                profile = Profile(user=user,
                                  first_name=form.cleaned_data.get('first_name'),
                                  last_name=form.cleaned_data.get('last_name'),
                                  email=form.cleaned_data.get('email'),
                                  phone=form.cleaned_data.get('phone'))
                profile.save()
                # user.profile= profile
                # user.save()
            else:
                print(user.profile.first_name,form.cleaned_data.get('first_name'))
                user.profile.first_name = form.cleaned_data.get('first_name')
                user.profile.last_name = form.cleaned_data.get('last_name')
                user.profile.email = form.cleaned_data.get('email')
                user.profile.phone = form.cleaned_data.get('phone')
                user.profile.save()
                user.save()
            return redirect(next)

    return render(request, 'EditProfile.html', {"form": form,"next":next,'model':user.profile})





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



