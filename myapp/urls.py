# myapp/urls.py

from django.urls import path
from .views import getAllProduct, getProductById, saveProduct, deleteProductById, updateProduct

urlpatterns = [
    path('api/products/', getAllProduct, name='all_products'),
    path('api/products/<int:id>/', getProductById, name='product_by_id'),
    path('api/products/add/', saveProduct, name='save_product'),
    path('api/products/<int:id>/delete/', deleteProductById, name='delete_product'),
    path('api/products/<int:id>/update/', updateProduct, name='update_product'),
]
