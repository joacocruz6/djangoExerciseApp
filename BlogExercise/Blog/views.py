from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
# Create your views here.
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,"article_create.html",context)
def article_list_view(request):
    articles = Article.objects.all()
    context = {
        "objects_list": articles
    }
    return render(request,"articles_created.html",context)
def article_detail_view(request,id):
    obj = Article.objects.get(id=id)
    context = {
        'obj': obj
    }
    return render(request,"article_detail.html",context)
