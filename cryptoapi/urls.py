from django.urls import path
from .views import main, CryptocurrencyList, CryptocurrencyUpdate, CryptocurrencyBySymbolView, TradeList

urlpatterns = [
    path('', main),
    path('coins/', CryptocurrencyList.as_view(), name='cryptocurrency-list'),
    path('coins/<str:symbol>/update/', CryptocurrencyUpdate.as_view(), name='cryptocurrency-update'),
    path('coins/<str:symbol>/', CryptocurrencyBySymbolView.as_view(), name='cryptocurrency-selectOne'),
    path('trades/', TradeList.as_view(), name='trade-list'),
]
