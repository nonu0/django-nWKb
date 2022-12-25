from django.urls import path
from .views import HomeView,DepartmentView,DoctorsView,AboutView,ContactView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('department',DepartmentView.as_view(),name='department'),
    path('doctors',DoctorsView.as_view(),name='doctors'),
    path('about',AboutView.as_view(),name='about'),
    path('contact',ContactView.as_view(),name='contact'),
]