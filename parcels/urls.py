
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('parcels/',parcels, name='parcels'),
    # path('add/<id>/',add_parcels, name ='add'),
    path('delete/<id>/',delete_parcels,name='delete'),
]