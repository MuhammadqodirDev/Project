from django.shortcuts import render
from .models import Guruxlash, Post, Portfolio

# Create your views here.

def HomePage(request):

    return render(request, 'index-3.html')


def AboutView(request):
    return render(request, 'about.html')

def GuruxView(request):
    return {'gurux':Guruxlash.objects.all()}

def BlogView(request):
    post = Post.objects.all()
    context = {
        'post':post
    }
    return render(request, 'blog.html', context)

def SingleBlog(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post1':post
    }
    return render(request, 'single-blog.html', context)


# def SingleBlog(request):
#
#     return render(request, 'single-blog.html')

def ContactView(request):


    return render(request, 'contact.html',)

def PortfolioView(request):
    portf = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'post':portf})

def SinglePortfolio(request, slug):
    post = Portfolio.objects.get(slug=slug)
    context = {
        'post':post
    }
    return render(request,'single-portfolio.html', context )

def ServiceView(request):
    return render(request, 'services.html')


def ShopView(request):
    return render(request, 'shop.html')





