from django.urls import path
import About.views

app_name = "About"

urlpatterns = [
    path('', About.views.index , name='index'),
]