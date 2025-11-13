from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio_autozone, name='inicio_autozone'),
    
    # URLs para Proveedores
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedor/editar/<int:proveedor_id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/editar/guardar/<int:proveedor_id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),
    
    # URLs para Sucursales
    path('agregar_sucursal/', views.agregar_sucursal, name='agregar_sucursal'),
    path('ver_sucursal/', views.ver_sucursal, name='ver_sucursal'),
    path('actualizar_sucursal/<int:id>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('realizar_actualizacion_sucursal/<int:id>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('borrar_sucursal/<int:id>/', views.borrar_sucursal, name='borrar_sucursal'),
    
    # URLs para Almacenes
    path('agregar_almacen/', views.agregar_almacen, name='agregar_almacen'),
    path('ver_almacen/', views.ver_almacen, name='ver_almacen'),
    path('actualizar_almacen/<int:id>/', views.actualizar_almacen, name='actualizar_almacen'),
    path('realizar_actualizacion_almacen/<int:id>/', views.realizar_actualizacion_almacen, name='realizar_actualizacion_almacen'),
    path('borrar_almacen/<int:id>/', views.borrar_almacen, name='borrar_almacen'),
    
    # URLs para Empleados
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/ver/', views.ver_empleados, name='ver_empleados'),
    path('empleado/editar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/editar/guardar/<int:empleado_id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),
    
    # URLs para Clientes
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_clientes, name='ver_clientes'),
    path('cliente/editar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/editar/guardar/<int:cliente_id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
    
    # URLs para Productos
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/ver/', views.ver_productos, name='ver_productos'),
    path('producto/editar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/editar/guardar/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
    
    # URLs para Ventas
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/ver/', views.ver_ventas, name='ver_ventas'),
    path('venta/editar/<int:venta_id>/', views.actualizar_venta, name='actualizar_venta'),
    path('venta/editar/guardar/<int:venta_id>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('venta/borrar/<int:venta_id>/', views.borrar_venta, name='borrar_venta'),
    path('venta/reportes/', views.reportes_ventas, name='reportes_ventas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)