from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.views.generic.edit import UpdateView
from .models import Parcels
from .forms import OrderCreateForm


def parcels(request):
    parcels_form = OrderCreateForm()
    form_object=Parcels.objects.filter(order=request.user)
    paginator = Paginator(form_object, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/parcels.html',{"parcels_form":parcels_form,"page_obj":page_obj})

def add_parcels(request):
    parcels_form = OrderCreateForm()
    if request.method == 'POST':
        parcels_form = OrderCreateForm(request.POST)
        if parcels_form.is_valid():
            parcel = parcels_form.save(commit=False)
            parcel.order = request.user
            parcels_form.save() 
        else:
            print(parcels_form.errors)
        return redirect(parcels)

    # form = OrderCreateForm()
    return render(request, 'pages/parcels.html', {'parcels_form':parcels_form})

        
def delete_parcels(request,id):
    parcel=Parcels.objects.get(id=id)
    if (parcel.status=='during' or parcel.status=='processed_1'):
        parcel.delete()
    return redirect(parcels)


# def edit_parcels(request, id):
#     parcel = Parcels.objects.get(id=id)
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST,instance=parcel)
#         if form.is_valid():
#             parc = form.save(commit=False)
#             parc.order = request.user
#             parc.save()
#             return redirect('parcels')

#     form = OrderCreateForm(instance=parcel)
#     return render(request, 'parcels', {'form': form})

class AuthorUpdateView(UpdateView):
    model = Parcels
    fields = ['treck','parcels_name','recipient','price','category','amount','weight','country','web_site','comment']
    success_url ="/"

