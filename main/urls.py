from django.urls import path
from main.views import show_main
from main.views import show_main, create_product, show_xml 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
]