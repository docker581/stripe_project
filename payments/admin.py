from django.contrib import admin

from .models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'currency']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'currency', 'get_items']

    def get_items(self, obj):
        return '\n'.join([item.name for item in obj.items.all()])


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
