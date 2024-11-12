from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:page>/', views.other_page, name='other'),
    path('account/login', views.BBLoginView.as_view(), name='login'),
    path('account/profile/', views.profile, name='profile'),
    path('acconts/logout/', views.BBLogoutView.as_view(), name='logout')
]
