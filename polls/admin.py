from django.contrib import admin
from .models import polls,ProductCategory

# Register your models here.

admin.site.register(polls)
admin.site.register(ProductCategory)
admin.site.register(ProductList)
