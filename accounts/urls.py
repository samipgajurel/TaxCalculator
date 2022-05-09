from django.urls import path
# import views from local directory.
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
 # When user request home page http://localhost:8000/my_hello_world, it will invoke the home function defined in views.py.
    path('', views.dashboard_page, name='dashboard'),
    # path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('profile/', views.dashboard_page, name='profile'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
    # path('logout/', LogoutView.as_view(next_page='/home'), name="logout"),
]
