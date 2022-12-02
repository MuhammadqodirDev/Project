from django.shortcuts import render
from .models import Guruxlash, Post, Portfolio

# from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext



def HomePage(request):
    trans = translate(language='ru')

    return render(request, 'index-3.html', {'trans':trans})

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)

    return text


def AboutView(request):
    trans = translate(language='ru')

    return render(request, 'about.html', {'trans':trans})

def GuruxView(request):
    return {'gurux':Guruxlash.objects.all()}

def BlogView(request):
    post = Post.objects.all()
    context = {
        'post':post,

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





