"""bloger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatte rns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import index_view,blog_list_view, add_authour_view,edit_authour_view,delete_authour_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='index_page'),
    path('blog_list/',blog_list_view,name='blog_list_page'),
    path('add_authour/',add_authour_view,name='add_authour_page'),
    path('edit_authour/<int:authour_id>/', edit_authour_view,name='edit_authour_page'),
    path('delete_authour/<int:authour_id>/',delete_authour_view, name="delete_authour_page")
   

]
