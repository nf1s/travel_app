from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.models import ModelForm

from booking.models import Flight


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'stars']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'UPDATE'))
