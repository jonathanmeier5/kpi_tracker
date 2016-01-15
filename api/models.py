from django.db import models


class Location(models.Model):
    
    name = models.CharField(max_length=60,null=True)
    address = models.CharField(max_length=60,null=True)
    zip_code = models.CharField(max_length=20,null=True)
    notes = models.TextField(null=True)
    
    owner = models.ForeignKey('auth.User', related_name='locations', null=True)
    


class GeneralRecord(models.Model):
    
    location = models.ForeignKey(Location,verbose_name="Location",null=True)
    time = models.DateTimeField(null=True)
    hours_worked = models.DecimalField(max_digits=10,decimal_places=3,null=True)
