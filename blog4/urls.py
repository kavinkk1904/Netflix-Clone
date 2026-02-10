"""
URL configuration for blog4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp4 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root_redirect, name='root'),
    path('home/', views.Home, name='home'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('forgetpass/',views.Forget,name='forget'),
    path('deleteaccount/',views.Delete,name='delete'),
    path('moviedetails/<int:id>/',views.Moviedetails,name='moviedetail'),
    path('movielist/',views.Movielist,name='movieslist'),
    path('add-fav/<int:movie_id>/', views.AddtoFavourite, name='addtofavourite'),
    path('toggle-fav/<int:movie_id>/', views.ToggleFavourite, name='togglefavourite'),
    path('favouritelist/', views.FavouriteList, name='favouritelist'),
    path('subscribe/',views.Subscription,name='subscribe'),
    path('payment/',views.Payment,name='payment'),
    path('logout/', views.Logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)