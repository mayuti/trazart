from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('create/', views.create_post, name='create_post'),
   path('blog/', views.blog, name='blog'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('nav/', views.nav, name='nav'),
]
