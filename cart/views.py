from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(req):
    return render(req, "cart_summary.html", {})

def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        
        cart_quantity = cart.__len__()
        
        #response_data = {'Product Name': product.name} 
        response_data = {'qty': cart_quantity}  
        return JsonResponse(response_data)

    
def cart_delete(req):
    pass
    
def cart_update(req):
    pass