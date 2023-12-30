"""
URL configuration for ecomn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    """


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#from django.conf.urls.static import static
#from Socio import settings

urlpatterns = [
    path('home/', views.home, name='home'),
    path('submit_post/', views.submit_post, name='submit_post'),
    path('get_usernames/', views.get_usernames),
    path('search',views.search,name='search'),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('register', views.register),
    path('home', views.aftrlogin),
    path('message/', views.messages_page),
    path('friends/', views.friends),
    path('profile/', views.profile_form),

    
    # Add more URL patterns here as needed
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
