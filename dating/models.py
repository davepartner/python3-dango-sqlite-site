from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    street = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.city} - {self.address} '

class Facilitator(models.Model):
    email = models.EmailField(unique=True)
    def __str__(self):
        return f'{self.email}'

class Dating(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    country = models.CharField(max_length=200)
    friend_slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    facilitator = models.ManyToManyField(Facilitator, blank=True)

    def __str__(self):
        return f'{self.name}'