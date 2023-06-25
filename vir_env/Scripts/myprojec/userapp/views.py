from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from myapps.models import Product
from .models import CartItem, Order
from .forms import ShippingForm





@login_required
def add_to_cart(request, product_id):
    quantity=1
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
    product = get_object_or_404(Product, id=product_id)
    
    cart_item = CartItem(user=request.user, product=product, price=product.price, quantity=quantity)
    cart_item.calculate_subtotal()
    
    cart_item.save()
    
    return redirect('home')


@login_required
def cart_details(request):
    
    cart_items = CartItem.objects.filter(user=request.user)
    total = 0 
    for item in cart_items:
        total += item.subtotal
    


    return render(request, 'cart_details.html', {'cart_items': cart_items,'total': total})

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def update_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.subtotal = cart_item.price * quantity
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')




@login_required
def checkout(request):
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            
            cart_items = CartItem.objects.filter(user=request.user)
   
           
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip_code = form.cleaned_data['zip_code']
            phone = form.cleaned_data['phone']

            
            for item in cart_items:
                order = Order.objects.create(
                user=request.user,
                name=name,
                email=email,
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
                phone=phone,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
                subtotal=item.product.price * item.quantity
            )
               

           
            cart_items.delete()

            
            return redirect('order_history')
    else:
        form = ShippingForm()
    return render(request, 'checkout.html', {'form': form})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})
