from django.contrib import admin

from products.model import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)

