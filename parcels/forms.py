from django import forms
from .models import COUNTRY_CHOICES, Parcels


class OrderCreateForm(forms.ModelForm):
    treck = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Ваш трек номер'}))
    parcels_name = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Например Zara, HM'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'0.00 $'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Например Техника'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'Количество товара'}))
    country = forms.ChoiceField(choices=COUNTRY_CHOICES,widget=forms.TextInput(attrs={'class':'sign__input country__input','placeholder':'Выберите страну'}))
    web_site = forms.URLField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'www.primer.com'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input modal__textarea','placeholder':'Можете оставить комментарий'}))

    class Meta:
        model = Parcels
        fields = ['treck','parcels_name','price','category','amount','country','web_site','comment']