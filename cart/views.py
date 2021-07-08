from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.info(request, f'Added: {product.name} to your cart')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust quantity of items in shopping cart
    """

    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session["cart"] = cart
    return (redirect("view_cart"))


def remove_from_cart(request, item_id):
    """
    Adjust quantity of items in shopping cart
    """

    cart = request.session.get("cart", {})
    product = get_object_or_404(Product, pk=item_id)

    cart.pop(item_id)

    request.session["cart"] = cart
    return redirect("view_cart")
