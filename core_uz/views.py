from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Guruxlash, Post, Portfolio

# Create your views here.

def HomePage(request):

    return render(request, 'uz/index-3.html')


def AboutView(request):
    return render(request, 'uz/about.html')

def GuruxView(request):
    return {'gurux':Guruxlash.objects.all()}

def BlogView(request):
    post = Post.objects.all()
    context = {
        'post':post
    }
    return render(request, 'uz/blog.html', context)

def SingleBlog(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post1':post
    }
    return render(request, 'uz/single-blog.html', context)


# def SingleBlog(request):
#
#     return render(request, 'single-blog.html')

def ContactView(request):


    return render(request, 'uz/contact.html',)

def PortfolioView(request):
    portf = Portfolio.objects.all()
    return render(request, 'uz/portfolio.html', {'post':portf})

def SinglePortfolio(request, slug):
    post = Portfolio.objects.get(slug=slug)
    context = {
        'post':post
    }
    return render(request,'uz/single-portfolio.html', context )

def ServiceView(request):
    return render(request, 'uz/services.html')


def ShopView(request):
    return render(request, 'uz/shop.html')





