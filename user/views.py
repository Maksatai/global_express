from django.shortcuts import render
from django.views.generic import DetailView, View

class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')


class ExampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'example.html')

class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/about-us.html')


class DetailNewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/detail-news.html')

class FAQView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/FAQ.html')

class HowWorksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/how-works.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/index.html')

class NewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/news.html')

class ParcelsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/parcels.html')

class PersonalAreaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/personal-area.html')

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/registration.html')
class ShopView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/shop.html')

class SignView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/sign.html')


