from django.db import models


# Create your models here.

class NC_skyField(models.Model):
    Field_information_size="40*20m"
    Field_information_shower_room="False"
    Field_imformation_parking="True"
    Field_information_shoes_rental="True"
    Field_information_beverage_support="True"
    
    match_Date=models.DateField()
    match_Time=models.TimeField()
    match_player=models.IntegerField(default=0)
    match_level1=models.IntegerField(default=0)
    match_level2=models.IntegerField(default=0)
    match_level3=models.IntegerField(default=0)
    
   
    def __str__(self):
        return str(self.match_Time)
    
 
class FC_football_Center(models.Model):
    Field_information_size="42*21m"
    Field_information_shower_room=True
    Field_imformation_parking=True
    Field_information_shoes_rental=True
    Field_information_beverage_support=False
    
    match_Date=models.DateField()
    match_Time=models.TimeField()
    match_player=models.IntegerField(default=0)
   
    def __str__(self):
        return str(self.match_Time)
    
class Jangseong_Field(models.Model):
    Field_information_size="42*23m"
    Field_information_shower_room=True
    Field_imformation_parking=True
    Field_information_shoes_rental=True
    Field_information_beverage_support=False
    
    match_Date=models.DateField()
    match_Time=models.TimeField()
    match_player=models.IntegerField(default=0)
   
    def __str__(self):
        return str(self.match_Time)
    