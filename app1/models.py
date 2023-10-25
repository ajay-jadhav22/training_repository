from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    author = models.CharField(max_length=200)
    qunty = models.IntegerField()
    is_pub = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = 'Book'

