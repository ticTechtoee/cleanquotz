from django.urls import path
import contact.views

app_name = "contact"

urlpatterns = [
    path('', contact.views.index , name='index'),
]