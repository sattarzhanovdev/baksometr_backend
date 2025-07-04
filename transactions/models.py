# transactions/models.py

from django.db import models

class Category(models.Model):
    emoji = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.emoji} {self.title}"
      
      
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.amount}"
      
