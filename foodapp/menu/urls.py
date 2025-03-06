from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
   
    path('',views.index,name='index'),
    path('list_product',views.list_products,name ='list_products'),
     path('product_details',views.detail_product,name ='product_detail'),
    
    
    
    
    ]