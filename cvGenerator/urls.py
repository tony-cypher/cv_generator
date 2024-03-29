"""cvGenerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from pdfGen import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.accept_data, name='accept'),
    path('resume/<int:id>/', views.view_resume, name='view_resume'),
    path('<int:id>/', views.resume, name='resume'),
    path('list/', views.list, name='list')
]
