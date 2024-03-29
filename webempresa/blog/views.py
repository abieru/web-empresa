from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

def category(request, category_id):
    #Category.objects.get(id=category_id)
    #el get_object_or_404 es para que le pasemos dos parametros el primero es el modelo y el segundo la foregeinkey o el id 
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category': category})  