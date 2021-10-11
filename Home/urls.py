from django.urls import path
from django.views.generic.base import TemplateView # new

app_name = "Home"

urlpatterns = [
    path('', TemplateView.as_view(template_name='Home/Home.html'), name='index'),
]