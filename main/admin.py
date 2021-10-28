from django.contrib import admin
from .models import Products, MainPicture


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'categories', 'new_products')
    list_editable = ('new_products', 'categories',)
    prepopulated_fields = {"slug": ('title',)}
    save_as = True











@admin.register(MainPicture)
class MainPictureAdmin(admin.ModelAdmin):
    list_display = ('title',)

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False



# Register your models here.
