from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('potatoes/', views.potatoes_index, name='potatoes_index'),
    path('potatoes/<int:potato_id>/', views.potato_detail, name='potato_detail'),
    path('potatoes/create/', views.PotatoCreate.as_view(), name='potatoes_create'),
    path('potatoes/<int:pk>/update/', views.PotatoUpdate.as_view(), name='potatoes_update'),
    path('potatoes/<int:pk>/delete/', views.PotatoDelete.as_view(), name='potatoes_delete'),
    path('potatoes/<int:potato_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('potatoes/<int:potato_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),

    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
]