from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Sucursal, Almacen, Empleado, Cliente, Producto, Venta
from django.urls import reverse
from django.utils import timezone

def inicio_autozone(request):
    # Página de inicio; puedes añadir más contexto si quieres
    return render(request, 'inicio.html')

# ============================================================
# VISTAS PARA PROVEEDORES
# ============================================================
def agregar_proveedor(request):
    if request.method == 'POST':
        # No validamos según tu instrucción
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_registro = request.POST.get('fecha_registro')  # formato YYYY-MM-DD
        dias_entrega = request.POST.get('dias_entrega')
        hora_entrega = request.POST.get('hora_entrega')

        Proveedor.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_registro=fecha_registro,
            dias_entrega=dias_entrega,
            hora_entrega=hora_entrega
        )
        return redirect('ver_proveedores')

    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.fecha_registro = request.POST.get('fecha_registro')
        proveedor.dias_entrega = request.POST.get('dias_entrega')
        proveedor.hora_entrega = request.POST.get('hora_entrega')
        proveedor.save()
        return redirect('ver_proveedores')
    # si no es POST, redirige a la página de edición
    return redirect('actualizar_proveedor', proveedor_id=proveedor.id)

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ============================================================
# VISTAS PARA SUCURSALES
# ============================================================
def agregar_sucursal(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        fecha_apertura = request.POST.get('fecha_apertura')
        horario = request.POST.get('horario')
        id_proveedor = request.POST.get('id_proveedor')
        
        proveedor = Proveedor.objects.get(id=id_proveedor)
        Sucursal.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            ciudad=ciudad,
            fecha_apertura=fecha_apertura,
            horario=horario,
            id_proveedor=proveedor
        )
        return redirect('ver_sucursal')
    
    proveedores = Proveedor.objects.all()
    return render(request, 'sucursal/agregar_sucursal.html', {'proveedores': proveedores})

def ver_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursal.html', {'sucursales': sucursales})

def actualizar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    proveedores = Proveedor.objects.all()
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal, 'proveedores': proveedores})

def realizar_actualizacion_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    if request.method == "POST":
        sucursal.nombre = request.POST.get('nombre')
        sucursal.direccion = request.POST.get('direccion')
        sucursal.telefono = request.POST.get('telefono')
        sucursal.ciudad = request.POST.get('ciudad')
        sucursal.fecha_apertura = request.POST.get('fecha_apertura')
        sucursal.horario = request.POST.get('horario')
        proveedor_id = request.POST.get('id_proveedor')
        sucursal.id_proveedor = Proveedor.objects.get(id=proveedor_id)
        sucursal.save()
        return redirect('ver_sucursal')

def borrar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    if request.method == "POST":
        sucursal.delete()
        return redirect('ver_sucursal')
    return render(request, 'sucursal/borrar_sucursal.html', {'sucursal': sucursal})

# ============================================================
# VISTAS PARA ALMACENES
# ============================================================
def agregar_almacen(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        capacidad_max = request.POST.get('capacidad_max')
        capacidad_disp = request.POST.get('capacidad_disp')
        telefono = request.POST.get('telefono')
        horario = request.POST.get('horario')
        id_sucursal = request.POST.get('id_sucursal')

        sucursal = Sucursal.objects.get(id=id_sucursal)
        Almacen.objects.create(
            id_sucursal=sucursal,
            nombre=nombre,
            direccion=direccion,
            capacidad_max=capacidad_max,
            capacidad_disp=capacidad_disp,
            telefono=telefono,
            horario=horario
        )
        return redirect('ver_almacen')

    sucursales = Sucursal.objects.all()
    return render(request, 'almacen/agregar_almacen.html', {'sucursales': sucursales})

def ver_almacen(request):
    almacenes = Almacen.objects.all()
    return render(request, 'almacen/ver_almacen.html', {'almacenes': almacenes})

def actualizar_almacen(request, id):
    almacen = get_object_or_404(Almacen, id=id)
    sucursales = Sucursal.objects.all()
    return render(request, 'almacen/actualizar_almacen.html', {
        'almacen': almacen,
        'sucursales': sucursales
    })

def realizar_actualizacion_almacen(request, id):
    almacen = get_object_or_404(Almacen, id=id)
    if request.method == "POST":
        almacen.nombre = request.POST.get('nombre')
        almacen.direccion = request.POST.get('direccion')
        almacen.capacidad_max = request.POST.get('capacidad_max')
        almacen.capacidad_disp = request.POST.get('capacidad_disp')
        almacen.telefono = request.POST.get('telefono')
        almacen.horario = request.POST.get('horario')
        sucursal_id = request.POST.get('id_sucursal')
        almacen.id_sucursal = Sucursal.objects.get(id=sucursal_id)
        almacen.save()
        return redirect('ver_almacen')

def borrar_almacen(request, id):
    almacen = get_object_or_404(Almacen, id=id)
    if request.method == "POST":
        almacen.delete()
        return redirect('ver_almacen')
    return render(request, 'almacen/borrar_almacen.html', {'almacen': almacen})

# ============================================================
# VISTAS PARA EMPLEADOS
# ============================================================
def agregar_empleado(request):
    if request.method == "POST":
        nombre_empleado = request.POST.get('nombre_empleado')
        direccion = request.POST.get('direccion')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        sucursal_id = request.POST.get('sucursal')

        sucursal = Sucursal.objects.get(id=sucursal_id)
        Empleado.objects.create(
            nombre_empleado=nombre_empleado,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            fecha_contratacion=fecha_contratacion,
            sucursal=sucursal
        )
        return redirect('ver_empleados')

    sucursales = Sucursal.objects.all()
    return render(request, 'empleado/agregar_empleado.html', {'sucursales': sucursales})

def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    sucursales = Sucursal.objects.all()
    return render(request, 'empleado/actualizar_empleado.html', {
        'empleado': empleado,
        'sucursales': sucursales
    })

def realizar_actualizacion_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == "POST":
        empleado.nombre_empleado = request.POST.get('nombre_empleado')
        empleado.direccion = request.POST.get('direccion')
        empleado.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion')
        sucursal_id = request.POST.get('sucursal')
        empleado.sucursal = Sucursal.objects.get(id=sucursal_id)
        empleado.save()
        return redirect('ver_empleados')
    return redirect('actualizar_empleado', empleado_id=empleado.id)

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == "POST":
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# ============================================================
# VISTAS PARA CLIENTES
# ============================================================
def agregar_cliente(request):
    if request.method == "POST":
        nombre_cliente = request.POST.get('nombre_cliente')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')

        Cliente.objects.create(
            nombre_cliente=nombre_cliente,
            telefono=telefono,
            email=email,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento
        )
        return redirect('ver_clientes')

    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        cliente.nombre_cliente = request.POST.get('nombre_cliente')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direccion = request.POST.get('direccion')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        cliente.save()
        return redirect('ver_clientes')
    return redirect('actualizar_cliente', cliente_id=cliente.id)

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ============================================================
# VISTAS PARA PRODUCTOS
# ============================================================
def agregar_producto(request):
    if request.method == "POST":
        nombre_producto = request.POST.get('nombre_producto')
        cantidad = request.POST.get('cantidad')
        proveedor_id = request.POST.get('proveedor')
        precio = request.POST.get('precio')
        almacen_id = request.POST.get('almacen')
        foto = request.FILES.get('foto')  # Cambio importante: request.FILES

        proveedor = Proveedor.objects.get(id=proveedor_id)
        almacen = Almacen.objects.get(id=almacen_id)
        
        Producto.objects.create(
            nombre_producto=nombre_producto,
            cantidad=cantidad,
            proveedor=proveedor,
            precio=precio,
            almacen=almacen,
            foto=foto  # Se pasa el archivo directamente
        )
        return redirect('ver_productos')

    proveedores = Proveedor.objects.all()
    almacenes = Almacen.objects.all()
    return render(request, 'producto/agregar_producto.html', {
        'proveedores': proveedores,
        'almacenes': almacenes
    })

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == "POST":
        # Procesar el formulario aquí mismo
        producto.nombre_producto = request.POST.get('nombre_producto')
        producto.cantidad = request.POST.get('cantidad')
        proveedor_id = request.POST.get('proveedor')
        producto.proveedor = Proveedor.objects.get(id=proveedor_id)
        producto.precio = request.POST.get('precio')
        almacen_id = request.POST.get('almacen')
        producto.almacen = Almacen.objects.get(id=almacen_id)
        
        # Manejo de la imagen
        if 'foto' in request.FILES:
            producto.foto = request.FILES['foto']
        elif 'foto-clear' in request.POST:
            producto.foto.delete(save=False)
        
        producto.save()
        return redirect('ver_productos')
    
    # Si es GET, mostrar el formulario
    proveedores = Proveedor.objects.all()
    almacenes = Almacen.objects.all()
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'proveedores': proveedores,
        'almacenes': almacenes
    })

def realizar_actualizacion_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        producto.nombre_producto = request.POST.get('nombre_producto')
        producto.cantidad = request.POST.get('cantidad')
        proveedor_id = request.POST.get('proveedor')
        producto.proveedor = Proveedor.objects.get(id=proveedor_id)
        producto.precio = request.POST.get('precio')
        almacen_id = request.POST.get('almacen')
        producto.almacen = Almacen.objects.get(id=almacen_id)
        
        # Manejo de la imagen
        if 'foto' in request.FILES:
            producto.foto = request.FILES['foto']
        elif 'foto-clear' in request.POST:
            producto.foto.delete(save=False)  # Elimina la imagen actual
        
        producto.save()
        return redirect('ver_productos')
    return redirect('actualizar_producto', producto_id=producto.id)

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})

# ============================================================
# VISTAS PARA VENTAS
# ============================================================
def agregar_venta(request):
    if request.method == "POST":
        fecha_venta = request.POST.get('fecha_venta')
        producto_id = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        cliente_id = request.POST.get('cliente')
        total = request.POST.get('total')
        sucursal_id = request.POST.get('sucursal')
        empleado_id = request.POST.get('empleado')

        producto = Producto.objects.get(id=producto_id)
        cliente = Cliente.objects.get(id=cliente_id)
        sucursal = Sucursal.objects.get(id=sucursal_id)
        empleado = Empleado.objects.get(id=empleado_id)

        Venta.objects.create(
            fecha_venta=fecha_venta,
            producto=producto,
            cantidad=cantidad,
            cliente=cliente,
            total=total,
            sucursal=sucursal,
            empleado=empleado
        )
        return redirect('ver_ventas')

    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    sucursales = Sucursal.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'venta/agregar_venta.html', {
        'productos': productos,
        'clientes': clientes,
        'sucursales': sucursales,
        'empleados': empleados
    })

def ver_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/ver_ventas.html', {'ventas': ventas})

def actualizar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    sucursales = Sucursal.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'venta/actualizar_venta.html', {
        'venta': venta,
        'productos': productos,
        'clientes': clientes,
        'sucursales': sucursales,
        'empleados': empleados
    })

def realizar_actualizacion_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == "POST":
        venta.fecha_venta = request.POST.get('fecha_venta')
        producto_id = request.POST.get('producto')
        venta.producto = Producto.objects.get(id=producto_id)
        venta.cantidad = request.POST.get('cantidad')
        cliente_id = request.POST.get('cliente')
        venta.cliente = Cliente.objects.get(id=cliente_id)
        venta.total = request.POST.get('total')
        sucursal_id = request.POST.get('sucursal')
        venta.sucursal = Sucursal.objects.get(id=sucursal_id)
        empleado_id = request.POST.get('empleado')
        venta.empleado = Empleado.objects.get(id=empleado_id)
        venta.save()
        return redirect('ver_ventas')
    return redirect('actualizar_venta', venta_id=venta.id)

def borrar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == "POST":
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})

def reportes_ventas(request):
    # Vista básica para reportes - puedes expandirla según necesites
    ventas = Venta.objects.all()
    total_ventas = sum(venta.total for venta in ventas)
    return render(request, 'venta/reportes_ventas.html', {
        'ventas': ventas,
        'total_ventas': total_ventas
    })