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
    class Meta:
        model = Trade
        fields = '__all__'