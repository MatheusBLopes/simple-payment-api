from django.urls import path
from .views import PaymentView


app_name = "payment"
urlpatterns = [
    path('payment/', PaymentView.as_view(), name='payment'),
]