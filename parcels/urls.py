
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('parcels/',parcels, name='parcels'),
    path('add/',add_parcels, name ='add'),
    path('delete/<int:id>/',delete_parcels,name='delete'),
    path('edit/<int:id>/',edit_parcels,name='edit'),
]