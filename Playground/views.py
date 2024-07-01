from django.shortcuts import render,redirect
from .models import MainServices,OUR_TECHNICIANS,Clients_reviews,ALLServices
from .forms import ServiceRequestForm
# Create your views here.
def product_list(request):
    main_services = MainServices.objects.all()
    our_technicians = OUR_TECHNICIANS.objects.all()
    clients_reviews = Clients_reviews.objects.all()
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ServiceRequestForm()


    return render(request, 'index.html',{'main_services': main_services,'our_technicians':our_technicians,'clients_reviews':clients_reviews,'form':form})




def Services(request):
    all_services = ALLServices.objects.all()  
    our_technicians = OUR_TECHNICIANS.objects.all()
    clients_reviews = Clients_reviews.objects.all()
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ServiceRequestForm()

    return render(request,'service.html',{'all_services':all_services,'our_technicians':our_technicians,'clients_reviews':clients_reviews,'form':form})





def success(request):
    return render(request, 'success.html')