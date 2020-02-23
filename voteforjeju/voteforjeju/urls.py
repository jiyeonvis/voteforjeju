"""voteforjeju URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from jeju2020 import views

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from markdownx import urls as markdownx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('jejugab/', views.gab, name='gab'),
    path('jejueul/', views.eul, name='eul'),
    path('seoguipo/', views.byeong, name='byeong'),
    path('jejugab/detail/<int:pk>', views.detail_gab, name='detail_gab'),
    path('jejueul/detail/<int:pk>', views.detail_eul, name='detail_eul'),
    path('seoguipo/detail/<int:pk>', views.detail_gab, name='detail_byeong'),
    url(r'^markdownx/', include(markdownx)),
    path('birye/', views.birye, name='birye'),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)