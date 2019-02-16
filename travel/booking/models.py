from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.reverse import reverse as api_reverse

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\s]*$', 'Only alphanumeric characters are allowed.')
numeric = RegexValidator(r'^[0-9]*$', 'Only numeric digits are allowed.')
min_stars = MinValueValidator(1, 'Number of stars cannot be less than 1')
max_stars = MaxValueValidator(5, 'Number of stars cannot exceed 5')


class Hotel(models.Model):
    name = models.CharField('name', max_length=128, validators=[alphanumeric])
    address = models.CharField('address', max_length=128, validators=[alphanumeric])
    stars = models.IntegerField('Number of stars', validators=[numeric, min_stars, max_stars], default=0)

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('api_v1:hotel-rud', kwargs={'pk': self.pk}, request=request)


class Flight(models.Model):
    origin = models.CharField('Origin', max_length=128, validators=[alphanumeric])
    destination = models.CharField('Destination', max_length=128, validators=[alphanumeric])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date) + " date"

    def get_api_url(self, request=None):
        return api_reverse('api_v1:flight-rud', kwargs={'pk': self.pk}, request=request)
