from django.urls import path, include, reverse_lazy

from rest_framework_simplejwt.views import(
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from .views import *
from django.contrib import admin
admin.autodiscover()

app_name = 'TeamManagement'
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('get-company-details/<str:pk>/', GetCompanyById.as_view(), name = "get_company_details"),
    path('get-company/', GetCompanyByName.as_view(), name = "get_company_by_name"),
    path('get-company/<str:name>/', GetCompanyByName.as_view(), name="get_company_by_name"),
    path('company/', CompanyViewNoPK.as_view(), name="company_view_nopk"),
    path('company/<str:pk>/', CompanyView.as_view(), name="company_view"),


    path('team/', TeamViewNoPK.as_view(), name="team_view_nopk"),
    path('team/<str:pk>/', TeamView.as_view(), name="company_view"),
    path('create-team/<str:pk>/', CreateTeamByCompanyID.as_view(), name="create_team_by_company_id"),
    path('get-team/', GetTeamByCompanyID.as_view(), name="get_team_by_company_id"),


    path('auth/generate-token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify-token/', TokenVerifyView.as_view(),name='token_verify'),
]
