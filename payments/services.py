import stripe

from django.conf import settings

from .models import Order


def get_order_amount(order: Order) -> int:
    currencies_converter = {
        'usd': 0.93,
        'eur': 1.07,
    }
    items = order.items.all()
    order_amount = sum([
        float(item.price) * currencies_converter[item.currency]
        if item.currency != order.currency
        else float(item.price) for item in items
    ])
    stripe_format_amount = int(order_amount * 100)
    return stripe_format_amount


def create_stripe_checkout_session(order: Order) -> dict:
    if not settings.STRIPE_PUBLISHABLE_KEY or not settings.STRIPE_SECRET_KEY:
        return {'error': 'Stripe API keys are not received!'}
    domain_url = settings.DOMAIN_URL
    stripe.api_key = settings.STRIPE_SECRET_KEY
    order_amount = get_order_amount(order)
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success/',
            cancel_url=domain_url + 'cancel/',
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'price_data': {
                        'currency': order.currency,
                        'product_data': {'name': f'Order № {order.id}'},
                        'unit_amount': order_amount,
                    },
                    'quantity': 1,
                },
            ],
        )
        return {'publicKey': settings.STRIPE_PUBLISHABLE_KEY, 'sessionId': checkout_session['id']}
    except Exception as e:
        return {'error': str(e)}
