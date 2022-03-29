from django.shortcuts import render

# Create your views here.
def index_page (request):
    # Get the index template file absolute path.
    # index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    return render(request, 'HomePage.html')


