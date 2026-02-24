from django import forms
from .models import Order, Contact


# =========================
# Common Styling Classes
# =========================
common_classes = (
    "w-full border-2 border-gray-400 rounded-xl px-4 py-3 "
    "bg-white text-gray-700 "
    "focus:border-orange-500 focus:ring-2 focus:ring-orange-200 "
    "hover:border-orange-400 transition duration-200 outline-none"
)


# =========================
# Order Form
# =========================
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['customer_name', 'product', 'quantity', 'address', 'phone']

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': common_classes}),
            'product': forms.Select(attrs={'class': common_classes}),
            'quantity': forms.NumberInput(attrs={'class': common_classes}),
            'address': forms.Textarea(attrs={'class': common_classes}),
            'phone': forms.TextInput(attrs={'class': common_classes}),
        }
# =========================
# Contact Form
# =========================
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': common_classes,
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': common_classes,
                'placeholder': 'Enter your email address'
            }),
            'message': forms.Textarea(attrs={
                'class': common_classes,
                'placeholder': 'Write your message here...',
                'rows': 4
            }),
        }