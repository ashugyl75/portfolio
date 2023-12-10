# pages/urls.py

from django.urls import path
from front_page import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("portfolio", views.portfolio, name='portfolio'),
    path("portfolio-details", views.portfolio_details, name='portfolio_details'),
    path("resume", views.resume, name='resume'),
    path("services", views.services, name='services'),
]