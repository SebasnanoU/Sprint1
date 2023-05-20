from django.contrib import admin
from .models import products,  update_archivo


class UpdateArchivoAdmin(admin.ModelAdmin):
    list_display = ["archivo"]
    list_filter = ["archivo"]

admin.site.register(products)
admin.site.register(update_archivo, UpdateArchivoAdmin)