import uuid
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from store.models import Game


class Transaction(models.Model):
    pid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    state = models.CharField(
        max_length = 7, 
        choices =  (
            ('PENDING', 'Pending'),
            ('SUCCESS', 'Success'),
            ('CANCEL', 'Cancel'),
            ('ERROR', 'Error')
        ),
        default = 'PENDING'
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)