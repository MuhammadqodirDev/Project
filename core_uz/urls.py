from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='homeuz'),
    path('about/', views.AboutView, name='aboutuz'),
    path('blog/', views.BlogView, name='bloguz'),
    path('blog/<slug:slug>/', views.SingleBlog, name='single_bloguz'),
    path('contact/', views.ContactView, name='contactuz'),
    path('portfolio/', views.PortfolioView, name='portfoliouz'),
    path('portfolio/<slug:slug>/', views.SinglePortfolio, name='single_portfoliouz'),
    path('service/', views.ServiceView, name='serviceuz'),
    path('shop/', views.ShopView, name='shopuz'),


]