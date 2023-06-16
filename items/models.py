from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length = 255)

    class Meta:

        verbose_name_plural = "Investments"
    def __str__(self):
        return self.name


#class for the different types of investments a user can dive into
class Investments(models.Model):
    investment_type = models.ForeignKey(Category, related_name='investments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='image', blank=True, null=True)
    is_Risky = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='ivestments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Greeks(models.Model):
    greeks = [
        ("Delta"),
        ("Gamma"),
        ("Vega"),
        ("Theta"),
        ("Rho")
    ]
    name = models.CharField(max_length=60)
    greeks = models.CharField(max_length=1, choices=greeks)

