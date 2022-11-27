from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='homeru'),
    path('about/', views.AboutView, name='aboutru'),
    path('blog/', views.BlogView, name='blogru'),
    path('blog/<slug:slug>/', views.SingleBlog, name='single_blogru'),
    path('contact/', views.ContactView, name='contactru'),
    path('portfolio/', views.PortfolioView, name='portfolioru'),
    path('portfolio/<slug:slug>/', views.SinglePortfolio, name='single_portfolioru'),
    path('service/', views.ServiceView, name='serviceru'),
    path('shop/', views.ShopView, name='shopru'),


]