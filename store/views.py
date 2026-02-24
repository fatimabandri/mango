from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        return render(request, "contact.html", {"form": form})
    
class OrderView(LoginRequiredMixin, View):

    def get(self, request):
        form = OrderView()
        return render(request, "order.html", {"form": form})

    def post(self, request):
        form = OrderView(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_success')
        return render(request, "order.html", {"form": form})

class RegisterView(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, "register.html", {"form": form})
    

    def about(request):
     return render(request, 'about.html')