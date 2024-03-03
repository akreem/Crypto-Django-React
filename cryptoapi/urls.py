from django.urls import path
from . import views


urlpatterns = [
    path('coins/', views.ApiOverview, name='home'),
    path('coins/create/', views.add_coins, name='add-coins'),
    path('coins/all/', views.view_coins, name='view-coins'),
    path('coins/<str:symbol>/update/', views.update_coins, name='update-coins'),
    path('coins/<str:symbol>/delete/', views.delete_coins, name='delete-coins'),
    path('trades/create/', views.create_trade, name='create-trade'),
    path('trades/all/', views.view_trades, name='view-trades'),
    path('trades/<int:pk>/update/', views.update_trades, name='update-trades'),
    path('trades/<int:pk>/delete/', views.delete_trade, name='delete-trades'),
]
