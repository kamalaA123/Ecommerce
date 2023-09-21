from django.contrib import admin

# Register your models here.
from .models import category,product

class category_admin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,category_admin)

class product_admin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['stock','price','available']
    list_per_page = 10
admin.site.register(product,product_admin)