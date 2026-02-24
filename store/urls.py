from django.urls import path
from .views import HomeView, ContactView, RegisterView
from django.views.generic import TemplateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('order/', TemplateView.as_view(template_name="order.html"), name='order'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('order-success/', TemplateView.as_view(template_name="order_success.html"), name='order_success'),
    path('register/', RegisterView.as_view(), name='register'),
]