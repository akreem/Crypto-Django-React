from django.db import models

TRADE_DIRECTIONS = {
    ("LONG", "Future Long"),
    ("SHORT", "Future Short"),
    ("BUY", "Buy"),
    ("SELL", "Sell")
}
TRADE_STATUS = {
    ("In progress", "In progress"),
    ("Completed", "Completed"),
    ("Canceled", "Canceled")
}

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Trade(models.Model):
    user = models.CharField(max_length=50)
    direction = models.CharField(max_length=5, choices=TRADE_DIRECTIONS, default="Buy")
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=14, decimal_places=4)
    coin = models.ForeignKey(Cryptocurrency,on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=TRADE_STATUS, default="In progress")



