from django.urls import path
from django.contrib.auth.decorators import login_required
# import views from local directory.
from . import views
urlpatterns = [
    # When user request home page http://localhost:8000/calculator it will invoke the home function defined in views.py.
    path('', login_required(views.calculator_page), name='calculator'),
    path('incometax', login_required(views.incomeTax), name='incometax'),
]
