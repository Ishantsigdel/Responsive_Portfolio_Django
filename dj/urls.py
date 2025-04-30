from django.urls import path
from . import views
# from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('footer/', views.footer, name='footer'),
]
