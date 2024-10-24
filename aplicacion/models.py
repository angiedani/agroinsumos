from django.db import models

# Create your models here.
class categorias(models.Model):
  idCategoria = models.UUIDField(primary_key=True, help_text="ID único para tipo de producto")
  nomCategoria = models.CharField(max_length=50)
  subcategoria = models.CharField(max_length=100)

class productos(models.Model):
  idProducto = models.UUIDField(primary_key=True, help_text="ID único para tipo de producto")
  nomProducto = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=150)
  precioProducto = models.IntegerField()
  stock = models.IntegerField()
  imagen = models.ImageField(null=True)
  categoria = models.ForeignKey('categorias', on_delete=models.SET_NULL, null=True)

class usuarios(models.Model):
  idUsuario = models.UUIDField(primary_key=True, help_text="ID único para tipo de usuario")
  nomUsuario = models.CharField(max_length=100)
  email = models.EmailField(max_length=150)
  password = models.CharField(null=True)
  fecha_nac = models.DateField(null=True)
  direccion = models.CharField (max_length=150)
  telefono = models.IntegerField()
  tipo_usuario = models.BooleanField(null=True)

class pagos(models.Model):
  id_pago = models.UUIDField(primary_key=True, help_text="ID único para tipo de pago")
  fecha_pago = models.DateField()
  monto = models.IntegerField ()
  estado_pago = models.CharField(max_length=50)
  idmetodo = models.ForeignKey('metodos_pago', on_delete=models.SET_NULL, null=True)
  idPedido = models.ForeignKey('pedidos', on_delete=models.SET_NULL, null=True)


class metodos_pago(models.Model):
  id_metodo = models.UUIDField(primary_key=True, help_text="ID único para tipo de metodo")
  tipo_metodo = models.CharField(max_length=50)


class pedidos(models.Model):
  idPedido = models.UUIDField(primary_key=True, help_text="ID único para tipo de pedido")
  fecha_pedido = models.DateField(null=True)
  #estado 
  idUsuario = models.ForeignKey('usuarios', on_delete=models.SET_NULL, null=True)
  total_productos = models.ForeignKey('carrito', on_delete=models.SET_NULL, null=True)

class pedido_detalles(models.Model):
  idDetalle = models.UUIDField(primary_key=True, help_text="ID único para tipo de detalle del pedido")
  total_productos = models.IntegerField()
  precio_total = models.IntegerField()
  # = models.ForeignKey('usuarios', on_delete=models.SET_NULL, null=True)

class carrito(models.Model):
  id_carrito = models.UUIDField(primary_key=True, help_text="ID único para tipo de detalle del carrito")
  total_productos = models.IntegerField()
  precio_total = models.ForeignKey('pedido_detalles', on_delete=models.SET_NULL, null=True)

  
  



