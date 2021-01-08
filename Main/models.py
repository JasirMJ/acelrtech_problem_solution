from django.db import models

# Create your models here.
class ItemTable(models.Model):
    ItemCode = models.CharField(unique=True,max_length=20)
    ItemName= models.CharField(max_length=20,null=True)
    CategoryL1 = models.CharField(max_length=20,null=True)
    CategoryL2 = models.CharField(max_length=20,null=True)
    UPC = models.CharField(max_length=20,null=True)
    ParentCode = models.CharField(max_length=20,null=True)
    MRPrice = models.FloatField()
    Size = models.CharField(max_length=20,null=True)
    Enabled = models.BooleanField()
