from django.db import models
from django.contrib.auth.models import User


# =========================================================
# PRODUCTOS
# =========================================================

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# =========================================================
# COLORES
# =========================================================

class Color(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


# =========================================================
# TALLAS
# =========================================================

class Talla(models.Model):
    numero = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.numero


# =========================================================
# INVENTARIO
# Producto + Color + Talla + Stock
# =========================================================

class Inventario(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )

    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT
    )

    talla = models.ForeignKey(
        Talla,
        on_delete=models.PROTECT
    )

    cantidad = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['producto', 'color', 'talla'],
                name='unique_producto_color_talla'
            )
        ]

    def __str__(self):
        return f"{self.producto} - {self.color} - {self.talla}"


# =========================================================
# CARRITO
# =========================================================

class Carrito(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Carrito de {self.usuario.username}"


# =========================================================
# DETALLE DEL CARRITO
# =========================================================

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE
    )

    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.PROTECT
    )

    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['carrito', 'inventario'],
                name='unique_carrito_inventario'
            )
        ]

    def __str__(self):
        return f"{self.inventario.producto} x {self.cantidad}"


# =========================================================
# PEDIDOS
# =========================================================

class Pedido(models.Model):

    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Procesando', 'Procesando'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    fecha = models.DateTimeField(auto_now_add=True)

    estado = models.CharField(
        max_length=50,
        choices=ESTADOS,
        default='Pendiente'
    )

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"


# =========================================================
# DETALLE DEL PEDIDO
# =========================================================

class DetallePedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE
    )

    inventario = models.ForeignKey(
        Inventario,
        on_delete=models.PROTECT
    )

    cantidad = models.PositiveIntegerField()

    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.inventario.producto} x {self.cantidad}"