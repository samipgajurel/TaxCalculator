from django.urls import path
from django.contrib.auth.decorators import login_required
# import views from local directory.
from . import views

urlpatterns = [
    # When user request home page http://localhost:8000/my_hello_world, it will invoke the home function defined in views.py.
    path('', views.index_page, name='home'),
    path('add/', login_required(views.add_news),name='add'),
    path('view/',views.see_news,name='view'),
    path("update/",views.update_news,name='update'),
    path("delete/",views.delete_news,name='delete'),
]
