
from api.views import ProfileAPIView
from api.views import ProfileRudView
from api.views import HotelAPIView
from api.views import HotelRudView
from api.views import FlightAPIView
from api.views import FlightRudView

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Booking API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^profile/(?P<pk>\d+)/$', ProfileRudView.as_view(), name='profile-rud'),
    url(r'^hotel/(?P<pk>\d+)/$', HotelRudView.as_view(), name='hotel-rud'),
    url(r'^flight/(?P<pk>\d+)/$', FlightRudView.as_view(), name='flight-rud'),
    url(r'^profile/$', ProfileAPIView.as_view(), name='profile-create'),
    url(r'^hotel/$', HotelAPIView.as_view(), name='hotel-create'),
    url(r'^hotel/(?P<pk>\d+)/booking/$', FlightAPIView.as_view(), name='flight-create'),
]
