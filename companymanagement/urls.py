"""companymanagement URL Configuration

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
from django.urls import path, include, re_path

from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


api_documentation_view = include_docs_urls(
    title='Company Management API',
    public=False,
    authentication_classes=(SessionAuthentication,),
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('', api_documentation_view, name='documentation'),
    path('admin/', admin.site.urls),
    path('api/', include('TeamManagement.urls'))
]
