from django.conf import settings
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.reverse import reverse as api_reverse

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\s]*$', 'Only alphanumeric characters are allowed.')
numeric = RegexValidator(r'^[0-9]*$', 'Only numeric digits are allowed.')
min_stars = MinValueValidator(1, 'Number of stars cannot be less than 1')
max_stars = MaxValueValidator(5, 'Number of stars cannot exceed 5')


class Profile(models.Model):
    class Meta:
        verbose_name_plural = "profiles"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, validators=[alphanumeric])

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('api_v1:profile-rud', kwargs={'pk': self.pk}, request=request)


class Hotel(models.Model):
    profile = models.ForeignKey('booking.Profile', on_delete=models.PROTECT,
                                related_name='hotel_booking', validators=[alphanumeric])

    name = models.CharField('hotel address', max_length=128, validators=[alphanumeric])
    address = models.CharField('hotel address', max_length=128, validators=[alphanumeric])

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('api_v1:travel-rud', kwargs={'pk': self.pk}, request=request)


class Flight(models.Model):
    profile = models.ForeignKey('booking.Profile', on_delete=models.PROTECT,
                                related_name='flight_booking', validators=[alphanumeric])

    origin = models.CharField('Origin', max_length=128, validators=[alphanumeric])
    destination = models.IntegerField('Destination', validators=[numeric, min_stars, max_stars])
    date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField('Number of stars', validators=[numeric, min_stars, max_stars])

    def __str__(self):
        return str(self.date) + " date"

    def get_api_url(self, request=None):
        return api_reverse('api_v1:flight-rud', kwargs={'pk': self.pk}, request=request)
