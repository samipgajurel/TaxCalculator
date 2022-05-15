from django.shortcuts import render,redirect
from news.models import News
import datetime
from django.core.paginator import Paginator
from news.service import get_latest_news,get_popular_news
from news.forms import NewsImageForm

# Create your views here.
def index_page (request):
    # Get the index template file absolute path.
    # index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    latest_news= get_latest_news()
    paginatorL = Paginator(latest_news, 3)
    page_number_L = request.GET.get('pageL',1)
    page_obj_L = paginatorL.get_page(page_number_L)

    popular_news=get_popular_news()
    paginatorP=Paginator(popular_news,3)
    page_number_P = request.GET.get('pageP',1)
    page_obj_P = paginatorP.get_page(page_number_P)
    return render(request, 'HomePage.html',{'page_obj_L': page_obj_L,
                                            'page_obj_P':page_obj_P})

def add_news (request):
    currentUser= request.user
    if not currentUser.is_superuser:
        return render(request,'AccessDenied.html')
    if request.method == "GET":
        form= NewsImageForm()
        return render(request,'AddNEWSPage.html',{'form':form})
    else:
        headline=request.POST.get("headline")
        content=request.POST.get("content")
        now = datetime.datetime.now()
        image = request.FILES.get('picture')
        print(image)
        news=News(headline=headline,content=content,author=currentUser,
                  dateCreated=now,lastModified=now,picture=image)
        news.save()
        return render(request,'NEWSViewPage.html',{'news':news})

def see_news(request):
    id = request.GET.get('id')
    news = News.objects.get(id=id)
    news.views= news.views+1
    news.save()
    return render(request, 'NEWSViewPage.html', {'news': news})
def update_news(request):
    currentUser = request.user
    if not currentUser.is_superuser:
        return render(request, 'AccessDenied.html')
    id= request.GET.get('id')
    print (id)
    news = News.objects.get(id=id)
    if request.method =="GET":
        return render(request, 'UpdateNEWSPage.html', {'news': news})
    else:
        news.headline= request.POST.get('headline')
        news.content = request.POST.get("content")
        news.lastModified = datetime.datetime.now()
        image = request.FILES.get('picture')
        if image:
            news.picture= image
        news.save()
        return render(request, 'NEWSViewPage.html', {'news': news})


def delete_news(request):
    currentUser = request.user
    if not currentUser.is_superuser:
        return render(request, 'AccessDenied.html')
    id = request.GET.get('id')
    news=News.objects.get(id=id)
    news.delete()
    return redirect("/home")



