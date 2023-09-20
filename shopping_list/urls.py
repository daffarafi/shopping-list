from django.contrib import admin
from django.urls import path, include
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
