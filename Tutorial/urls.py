from django.urls import path
import Tutorial.views

app_name = "Tutorial"

urlpatterns = [
    path('', Tutorial.views.index , name='index'),
]