from django.contrib import admin
from .models import User, Category, Product, Cart, Order, OrderItem


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)

