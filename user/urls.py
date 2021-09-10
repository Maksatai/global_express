from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='base'),
    path('example/', ExampleView.as_view(), name='example'),
    path('about/', AboutUsView.as_view(), name='aboutus'),
    path('detail-news/', DetailNewsView.as_view(), name='detail-news'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('how-works/', HowWorksView.as_view(), name='how-works'),
    # path('/', View.as_view(), name='index'),
    path('news/', NewsView.as_view(), name='news'),
    path('personal-area/', PersonalAreaView.as_view(), name='personal-area'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('sign/', SignView.as_view(), name='sign'),

    ]