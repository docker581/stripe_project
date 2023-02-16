from django.urls import path

from . import views

urlpatterns = [
    path('order/<int:order_id>/', views.order_detail),
    path('buy/<int:order_id>/', views.buy_order),
    path('success/', views.SuccessView.as_view()),
    path('cancelled/', views.CancelView.as_view()),
]
