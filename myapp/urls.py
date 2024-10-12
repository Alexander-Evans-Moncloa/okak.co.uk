from django.urls import path
from django.views.generic import TemplateView
from .views import my_form_view
from . import views

urlpatterns = [
    path('form/', my_form_view, name='form'),
    path('submit-form/', views.submit_form, name='submit_form'),

    # Map each HTML template to a URL path
    path('checkout/', TemplateView.as_view(template_name='checkout.html'), name='checkout'),
    path('products/', TemplateView.as_view(template_name='products.html'), name='products'),
    path('cart/', TemplateView.as_view(template_name='cart.html'), name='cart'),
    path('fpga/', TemplateView.as_view(template_name='fpga.html'), name='fpga'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('ros2/', TemplateView.as_view(template_name='ros2.html'), name='ros2'),
    path('wone/', TemplateView.as_view(template_name='wone.html'), name='wone'),
    path('grone/', TemplateView.as_view(template_name='grone.html'), name='grone'),
    path('mouse/', TemplateView.as_view(template_name='mouse.html'), name='mouse'),
    path('projects/', TemplateView.as_view(template_name='projects.html'), name='projects'),
    path('pirate/', TemplateView.as_view(template_name='pirate.html'), name='pirate'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('costing/', TemplateView.as_view(template_name='costing.html'), name='costing'),
    path('rev_eng/', TemplateView.as_view(template_name='rev_eng.html'), name='rev_eng'),
    path('anaconda/', TemplateView.as_view(template_name='anaconda.html'), name='anaconda'),
    path('fullstack/', TemplateView.as_view(template_name='fullstack.html'), name='fullstack'),
    path('vanilla_europa/', TemplateView.as_view(template_name='vanilla_europa.html'), name='vanilla_europa'),
    path('mars_explorer/', TemplateView.as_view(template_name='mars_explorer.html'), name='mars_explorer'),
    path('thank-you/', TemplateView.as_view(template_name='thank-you.html'), name='thank-you'),
]
