from .views import *
from django.urls import path


urlpatterns = [
    path(r'^register/$', RegisterView.as_view()),
    path(r'^login/$', LoginView.as_view()),
]
