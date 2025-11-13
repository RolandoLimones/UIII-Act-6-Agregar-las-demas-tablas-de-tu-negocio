from django.contrib import admin
from .models import Proveedor, Sucursal, Almacen, Empleado, Cliente, Producto, Venta

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_registro',)

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'id_proveedor', 'fecha_apertura')
    search_fields = ('nombre', 'ciudad')
    list_filter = ('ciudad', 'fecha_apertura', 'id_proveedor')

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_sucursal', 'capacidad_disp', 'capacidad_max')
    search_fields = ('nombre', 'id_sucursal__nombre')
    list_filter = ('id_sucursal',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_empleado', 'sucursal', 'fecha_contratacion', 'fecha_nacimiento')
    search_fields = ('nombre_empleado', 'sucursal__nombre')
    list_filter = ('sucursal', 'fecha_contratacion', 'fecha_nacimiento')
    date_hierarchy = 'fecha_contratacion'

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'telefono', 'email', 'fecha_nacimiento')
    search_fields = ('nombre_cliente', 'telefono', 'email')
    list_filter = ('fecha_nacimiento',)
    date_hierarchy = 'fecha_nacimiento'

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'proveedor', 'precio', 'cantidad', 'almacen')
    search_fields = ('nombre_producto', 'proveedor__nombre')
    list_filter = ('proveedor', 'almacen')
    list_editable = ('precio', 'cantidad')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_venta', 'cliente', 'producto', 'cantidad', 'total', 'sucursal', 'empleado')
    search_fields = ('cliente__nombre_cliente', 'producto__nombre_producto', 'sucursal__nombre')
    list_filter = ('fecha_venta', 'sucursal', 'empleado')
    date_hierarchy = 'fecha_venta'
    list_per_page = 20