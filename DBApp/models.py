from django.db import models

class Emp(models.Model):
    Employee_ID = models.AutoField(primary_key = True)
    Employee_Name = models.CharField(max_length = 100)
    Department_Name = models.IntegerField()
    image = models.ImageField(upload_to = 'images')
    #Location = models.CharField(max_length = 100)