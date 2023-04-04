from django.db import models

class user_details(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

class booking_details(models.Model):
    User_name=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=10)
    Time=models.TimeField()
    Date=models.DateField()
    Service = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class admin_details(models.Model):
    name=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class gallery(models.Model):

    image = models.FileField()



class quotes(models.Model):

    quote = models.CharField(max_length=50)

    def __str__(self):
        return self.quote

class offers(models.Model):

    hair = models.CharField(max_length=10)
    massage = models.CharField(max_length=10)
    makeup = models.CharField(max_length=10)






# Create your models here.
