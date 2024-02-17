from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title","image_preview" ,"offer")
    list_filter = ( "title","offer")
    search_fields = ("title","image_preview","offer")

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:70px;object-fit:contain;">'
            )
        return ""

    image_preview.short_description = 'Image Preview'