from django.urls import path
from .views import home, contacts

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),

]