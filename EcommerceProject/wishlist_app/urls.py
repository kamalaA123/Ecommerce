from django.urls import path
from .import views
app_name='wishlist_app'
urlpatterns = [
    path('', views.wish_detail, name='wish_detail'),
    path('add/<int:product_id>/', views.add_wish, name='add_wish'),
    path('delete/<int:product_id>/', views.delete, name='delete'),
]