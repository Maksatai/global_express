from django.shortcuts import redirect, render
from .models import Parcels
from .forms import OrderCreateForm

# filter(order__username=request.user)
def parcels(request):
    parcels_form = OrderCreateForm()
    form_object=Parcels.objects.all()
    return render(request, 'pages/parcels.html',{"forms":form_object,"parcels_form":parcels_form})

def add_parcels(request):
    parcels_form = OrderCreateForm()
    if request.method == 'POST':
        parcels_form = OrderCreateForm(request.POST)
        if parcels_form.is_valid():
            parcel = parcels_form.save(commit=False)
            parcel.order = request.user
            parcel.save() 
        else:
            print(parcels_form.errors)
        return redirect(parcels)

    # form = OrderCreateForm()
    return render(request, 'pages/parcels.html', {'parcels_form':parcels_form})

        
def delete_parcels(request,id):
    parcel=Parcels.objects.get(id=id)
    parcel.delete()
    return redirect(parcels)