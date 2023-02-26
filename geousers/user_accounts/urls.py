from django.contrib.auth import views as auth_views
from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('account/', views.account, name='account'),
    path('edit-account/', views.edit_account, name='edit_account'),
    path('map/', views.map, name='map'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]