from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('about/', views.AboutView, name='about'),
    path('blog/', views.BlogView, name='blog'),
    path('blog/<slug:slug>/', views.SingleBlog, name='single_blog'),
    path('contact/', views.ContactView, name='contact'),
    path('portfolio/', views.PortfolioView, name='portfolio'),
    path('service/', views.ServiceView, name='service'),
    path('shop/', views.ShopView, name='shop'),


]