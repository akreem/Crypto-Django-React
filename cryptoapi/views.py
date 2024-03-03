from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone 
from rest_framework import generics
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cryptocurrency, Trade
from .serializers import CryptocurrencySerializer,TradeSerialiser
# Create your views here.

def main(request):
    return HttpResponse("Crypto")

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_coins': '/all/',
        'Search by symbol': '/all/?symbol=symbol_name',
        'Add': '/create',
        'Update': '/symbol/update/',
        'Delete': '/symbol/delete/'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_coins(request):
    coin = CryptocurrencySerializer(data=request.data)
 
    # validating for already existing data
    if Cryptocurrency.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if coin.is_valid():
        coin.save()
        return Response(coin.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
@api_view(['GET'])
def view_coins(request):
    # checking for the parameters from the URL
    if request.query_params:
        coins = Cryptocurrency.objects.filter(**request.query_params.dict())
    else:
        coins = Cryptocurrency.objects.all()
 
    # if there is something in items else raise error
    if coins:
        serializer = CryptocurrencySerializer(coins, many=True)
        return Response({"coins":serializer.data})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_coins(request, pk):
    coin = Cryptocurrency.objects.get(pk=pk)
    data = CryptocurrencySerializer(instance=coin, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_coins(request, pk):
    coin = get_object_or_404(Cryptocurrency, pk=pk)
    coin.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def create_trade(request):
    trade = TradeSerialiser(data=request.data)
    if trade.is_valid():
        trade.save()
        return Response(trade.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_trades(request):
    if request.query_params:
        trades = Trade.objects.filter(**request.query_params.dict())
    else:
        trades = Trade.objects.all()
    if trades:
        serializer = TradeSerialiser(trades, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)     

@api_view(['POST'])
def update_trades(request, pk):
    trade = Trade.objects.get(pk=pk)
    data = TradeSerialiser(instance=trade, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_trade(request, pk):
    trade = get_object_or_404(Trade, pk=pk)
    trade.delete()
    return Response(status=status.HTTP_202_ACCEPTED)