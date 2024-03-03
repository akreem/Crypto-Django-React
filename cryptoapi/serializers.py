from rest_framework import serializers
from .models import Cryptocurrency, Trade

class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = '__all__'
class CryptocurrencyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['name', 'symbol', 'timestamp']

class TradeSerialiser(serializers.ModelSerializer):
    coin = CryptocurrencySerializer()
    class Meta:
        model = Trade
        fields = ['id', 'user', 'direction','timestamp','price','coin','status']