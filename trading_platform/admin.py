from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from trading_platform.models import NetworkNode, Product


@admin.register(NetworkNode)
class NetworkNode(admin.ModelAdmin):
    readonly_fields = ('get_supplier',)
    list_filter = ('city',)

    def get_supplier(self, obj):
        products = obj.products.all()
        suppliers = [product.supplier for product in products if product.supplier]
        supplier_links = []
        for supplier in suppliers:
            supplier_url = reverse('admin:trading_platform_networknode_change', args=[supplier.id])
            supplier_links.append('<a href="{}">{}</a>'.format(supplier_url, supplier.name))
        return format_html(', '.join(supplier_links) if supplier_links else '-')
    get_supplier.short_description = 'Supplier'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_debt']

    def clear_debt(self, queryset):
        queryset.update(debt_to_supplier=0)

    clear_debt.short_description = 'Clear debt'
