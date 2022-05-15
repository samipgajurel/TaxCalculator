from .models import Profile
from django.contrib.auth.models import User

def get_total_users():
    return Profile.objects.count()
def get_total_admins():
    return User.objects.filter(is_superuser=True).count()
