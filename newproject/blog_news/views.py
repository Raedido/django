from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import NewsModel
from blog_news.models import NewsModel 

# Create your views here
def index(request):
    index = {'page': 'Index Page Loading for the first time'}
    

def about(request):
    return HttpResponse("About page")

def news(request):
    url = "https://newsapi.org/v2/everything?q=tesla&from=2024-03-01&sortBy=publishedAt&apiKey=f74fc01cfe164581b6c7e5d29e3d73e5"


    data = requests.get(url)
    allnews= data.json()
    articles= allnews.get("articles", [])

    blog = NewsModel()

    print(NewsModel.objects)

    for latest in articles: 
        blog = NewsModel(description=latest['description'], title=latest['title'], url=latest['url'], content=latest['content'])
        
        blog.save()
    
    context = {'articles': articles}
    return render(request, 'blog/news.html')
