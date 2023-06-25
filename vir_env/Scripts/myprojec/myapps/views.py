from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Product
from django.views.generic import DetailView


def home(request):
    products=Product.objects.all()
    context = {'products': products}
    return render(request,'myapps/home.html',context)



def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Hi! Account successfully created. Please login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'myapps/register.html',{'form':form})

class PostDetailView(DetailView):
    model=Product
    template_name="myapps/product_details.html"
