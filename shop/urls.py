from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
  path('', views.allProdCat, name='allProdCat'),
  path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),# this name is used in models.py
  path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'), #this name is also used in models.py

]
