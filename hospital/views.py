from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

class DepartmentView(TemplateView):
    template_name = 'department.html'

class DoctorsView(TemplateView):
    template_name = 'doctors.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
