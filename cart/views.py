from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view that renders the shopping cart contents """

    return render(request, 'view_cart/cart.html')