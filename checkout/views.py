from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "You have no products in your cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HWMrLIu09P0FTqkNB4NCwHxMKIy8Q7VGOcjBxnzbhO9aZqogXNobex6pkYh4uAf9mCFS9zOGbRR6CIi3dadG1B600cwIAlFDT',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
