from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'app/home.html'

class AboutView(TemplateView):
    template_name = 'app/about.html'   

class ContactView(TemplateView):
    template_name = 'app/contact.html' 

class LoginView(TemplateView):
    template_name = 'app/login.html'

class RegisterView(TemplateView):
    template_name = 'app/register.html'