from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import Order
from .services import create_stripe_checkout_session


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


def page_not_found(request, exception):
    return render(request, '404.html', {'path': request.path}, status=404)


def order_detail(request, order_id):
    if request.method == 'GET':
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'order.html', {'order_id': order.id, 'items': order.items.all()})


def buy_order(request, order_id):
    if request.method == 'GET':
        order = get_object_or_404(Order, id=order_id)
        response = create_stripe_checkout_session(order)
        return JsonResponse(response)
