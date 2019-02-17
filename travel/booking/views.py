import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from markdown import markdown

from booking.forms import FlightForm
from booking.models import Flight


class AssignmentView(TemplateView):
    template_name = 'booking/assignment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open(os.path.join(os.path.dirname(settings.BASE_DIR), 'README.md'), encoding='utf-8') as f:
            assignment_content = f.read()

        context.update({
            'assignment_content': mark_safe(markdown(assignment_content))
        })

        return context


class DashboardView(LoginRequiredMixin, ListView):
    model = Flight
    ordering = ('-date',)
    context_object_name = 'booking'
    template_name = 'booking/dashboard.html'

    def get_queryset(self):
        flights = super().get_queryset()
        flights = flights.all()

        return flights


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Flight
    form_class = FlightForm
    success_url = reverse_lazy('dashboard')
