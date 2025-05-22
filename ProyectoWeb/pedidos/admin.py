from django.contrib import admin

from .models import Pedido, LineaPedido

# Register your models here.
class LineaPedidoAdmin(admin.ModelAdmin):
    list_display=("user", "producto", "pedido", "cantidad")

admin.site.register(LineaPedido, LineaPedidoAdmin)
admin.site.register(Pedido)
