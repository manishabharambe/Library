from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Manager

# Create your models here.
# class CustomQuerySet(QuerySet):
#     def delete(self):
#         self.update(is_available=False)
class ActiveManager(models.Manager):
    def is_available(self):
        return self.model.objects.filter(is_available = 0)
    def get_queryset(self):
        return super(ActiveManager,self).get_queryset().filter(is_available = 0)
class Book(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()
    is_available = models.BooleanField(default=1)
    objects =models.Manager()
    activeobjects = ActiveManager()
    

    class Meta:
        db_table = "book_db"

    def __str__(self):
        return self.name

    # def delete(self):
    #     self.is_available = False
    #     self.save()
# class Book1(Book):
#     activeobjects = ActiveManager()
