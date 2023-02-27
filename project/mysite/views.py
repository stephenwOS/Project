from django.shortcuts import render
from mysite.models import Product,Customer
from . import forms
# Create your views here.
def home(request):
    return render(request,'mysite/index.html')

def shopping_detail(request):
    customer = Customer.objects.all #Select * from customers
    my_dict = {'customers':customer}
    return render(request,"mysite/shopping_detail.html",context=my_dict)

def form_name_view(request):
    form = forms.CustomerForm()

    if request.method == 'POST':
        form = forms.CustomerForm(request.POST)
        if form.is_valid:
            form.save(commit=True) #Saving the data to database
            return shopping_detail(request)
        else:
            print("Invalid Form")
    return render(request,'mysite/form.html',{'form':form})
