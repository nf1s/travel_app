from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from booking.schema import schema
from booking.views import AssignmentView, DashboardView, ProjectUpdateView

urlpatterns = [
    url(r'^$', AssignmentView.as_view(), name='assignment'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^booking/(?P<pk>[0-9]+)-(?P<slug>[-\w]*)/$', ProjectUpdateView.as_view(), name='project-update'),
    url(r'^graphql/$', csrf_exempt(GraphQLView.as_view(
        graphiql=True,
        schema=schema
    ))),

]
