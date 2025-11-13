from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    fecha_registro = models.DateField()
    dias_entrega = models.CharField(max_length=150)
    hora_entrega = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)
    fecha_apertura = models.DateField()
    horario = models.CharField(max_length=100)
    id_proveedor = models.ForeignKey(
        Proveedor, 
        on_delete=models.CASCADE,
        related_name='sucursales',
        verbose_name='Proveedor'
    )
    
    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
    
    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"


class Almacen(models.Model):
    id_sucursal = models.ForeignKey(
        Sucursal, 
        on_delete=models.CASCADE,
        related_name='almacenes',
        verbose_name='Sucursal'
    )
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    capacidad_max = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad_disp = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    horario = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Almacén'
        verbose_name_plural = 'Almacenes'
    
    def __str__(self):
        return f"{self.nombre} - {self.id_sucursal.nombre}"


class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    fecha_contratacion = models.DateField()
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        related_name='empleados',
        verbose_name='Sucursal'
    )
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return self.nombre_empleado


class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    direccion = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nombre_cliente


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name='productos',
        verbose_name='Proveedor'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    almacen = models.ForeignKey(
        Almacen,
        on_delete=models.CASCADE,
        related_name='productos',
        verbose_name='Almacén'
    )
    foto = models.ImageField()
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre_producto


class Venta(models.Model):
    fecha_venta = models.DateField()
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='ventas',
        verbose_name='Producto'
    )
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='ventas',
        verbose_name='Cliente'
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE,
        related_name='ventas',
        verbose_name='Sucursal'
    )
    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='ventas',
        verbose_name='Empleado'
    )
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    
    def __str__(self):
        return f"Venta {self.id} - {self.fecha_venta}"