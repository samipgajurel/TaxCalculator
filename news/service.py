from .models import News
from datetime import datetime, timedelta
# from django.contrib.auth.models import User

def get_total_news():
    return News.objects.count()
# def get_total_admins():
#     return User.objects.filter(is_superuser=True).count()
def get_news_this_week():
    now = datetime.now()
    last_week= now -timedelta(days=7)
    return News.objects.filter(dateCreated__gte=last_week).count()

def get_latest_news(limit=15):
    latest= News.objects.all().order_by('-dateCreated')[:limit]
    return latest

def get_popular_news(limit=15):
    popular= News.objects.all().order_by('-views')[:limit]
    return popular

