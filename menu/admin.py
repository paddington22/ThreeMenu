from django.contrib import admin
from .models import Menu, Item


# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'menu')
    list_filter = ('menu', )
    fieldsets = (
        (None, {
            'fields': ('title', ('menu', 'parent'))
        }),
    )