from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto
from .models import Cliente

# Define la acción personalizada para actualizar el stock
def actualizar_stock_a_20(modeladmin, request, queryset):
    queryset.update(stock=20)
actualizar_stock_a_20.short_description = "Actualizar stock a 20 unidades"

# Clase de administración para el modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    # Otros campos y configuraciones de admin

    # Agrega la acción personalizada a las acciones disponibles
    actions = [actualizar_stock_a_20]

# Registra los modelos junto con sus clases de administración personalizadas
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)