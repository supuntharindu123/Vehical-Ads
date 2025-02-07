from django.db import models
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField(max_length=500)
    date=models.DateField(default=date.today)

    class Meta:
        db_table="myapp_contact"

class Ads(models.Model):
    username = models.CharField(max_length=200)
    contact = models.CharField(
        max_length=12,
        validators=[RegexValidator(r'^\d{10,12}$', 'Enter a valid phone number.')]
    )
    vehicle_type=models.CharField(max_length=100)
    vehicle_condition=models.CharField(max_length=100)
    vehicle_make=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    manufacture_year=models.CharField(max_length=100)
    price=models.IntegerField()
    transmission=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=100)
    engine_capacity=models.CharField(max_length=100)
    mileage=models.CharField(max_length=100)
    info=models.CharField(max_length=200)
    image01=models.ImageField(upload_to="vehicles")
    image02=models.ImageField(upload_to="vehicles",blank=True,null=True)
    image03=models.ImageField(upload_to="vehicles",blank=True,null=True)
    image04=models.ImageField(upload_to="vehicles",blank=True,null=True)
    image05=models.ImageField(upload_to="vehicles",blank=True,null=True)
    image06=models.ImageField(upload_to="vehicles",blank=True,null=True)
    date = models.DateField(default=date.today)

    def delete(self):
        self.image01.delete()
        self.image02.delete()
        self.image03.delete()
        self.image04.delete()
        self.image05.delete()
        self.image06.delete()
        super().delete()


class Test(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="test")

    def delete(self):
        self.img.delete()
        super().delete()

class Faq(models.Model):
    question=models.CharField(max_length=200)
    answer=models.TextField(max_length=5000)

    class Meta:
        db_table="myapp_faq"

   

   