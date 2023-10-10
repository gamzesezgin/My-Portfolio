from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),    #name -> url nin ismi
    path('home/', views.home, name='home'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('contact/', views.contact, name='contact'),
    path('<category>', views.getCoursesByCategory),
    path('contact/', views.submit_contact_form, name = 'message')
]
