from django.shortcuts import render
from django.views.generic import DetailView, View,TemplateView
from parcels.forms import OrderCreateForm

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

class ParcelsView(TemplateView):
    template_name = "pages/parcels.html"

    def dispatch(self, request, *args, **kwargs):
        parcels_form = OrderCreateForm()
        if request.method == 'POST':
            parcels_form = OrderCreateForm(request.POST)
            if parcels_form.is_valid():
                parcels_form.save()
                return render(request,self.template_name,{'parcels_form':parcels_form})
        else:
            parcels_form = OrderCreateForm()
        return render(request, self.template_name,{'parcels_form':parcels_form})

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
