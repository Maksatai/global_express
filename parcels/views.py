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
            # parcel = parcels_form.save(commit=False)
            # parcel.order = request.user
            parcels_form.save() 
        else:
            print(parcels_form.errors)
        return redirect(parcels)

    # form = OrderCreateForm()
    return render(request, 'pages/parcels.html', {'parcels_form':parcels_form})

        
def delete_parcels(request,id):
    parcel=Parcels.objects.get(id=id)
    parcel.delete()
    return redirect(parcels)


def edit_parcels(request, id):
    parcel = Parcels.objects.get(id=id)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST,instance=parcel)
        print(form)
        if form.is_valid():
            parc = form.save(commit=False)
            parc.order = request.user
            parc.save()
            return redirect('parcels')

    form = OrderCreateForm(instance=parcel)
    return render(request, 'parcels', {'form': form})


    