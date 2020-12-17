from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('potatoes/', views.potatoes_index, name='potatoes_index'),
    path('potatoes/<int:potato_id>/', views.potato_detail, name='potato_detail'),
]