from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
from django.utils import timezone 

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)


    ADMINISTRADOR = 'Administrador'
    GERENTE = 'Gerente'
    EMPLEADO = 'Empleado'

    ESTADO_CHOICES = [
        (ADMINISTRADOR,'Administrador'),
        (GERENTE , 'Gerente'),
        (EMPLEADO, 'Empleado')
    ]
    tipo = models.CharField(max_length=100, choices=ESTADO_CHOICES)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)

    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, blank=True)
    
    # ESTDOS DOS DATOS SON MEDIOS CONFUsos
    
    created = models.DateField(auto_now_add=True)
    FechaRegistro = models.DateField(auto_now_add=True,blank=True,null=True)
    
    datecompleted = models.DateTimeField(blank=True, null=True)
    #
    important = models.BooleanField(default=False)
    
    # INICIADA -PROCESO 

    INICIADA = 'Iniciada'
    PROCESO = 'Proceso'
    TERMINADA = 'Terminada'

    ESTADO_CHOICES = [
        (INICIADA, 'Iniciada'),
        (PROCESO, 'Proceso'),
        (TERMINADA,'Terminada'),
    ]
    estadotarea = models.CharField(max_length=100, blank=True, null=True, choices=ESTADO_CHOICES,)

    # INVESTIGAR LA LLAVE FORANEA DE ESTA TABLA.
    #empleado_asignado = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    NotasTarea = models.CharField(max_length=100,blank=True, null=True)
    Comentarios = models.CharField(max_length=100, blank=True, null=True)

    # Este codigo no sirve pa nada
    def __str__(self):
        return self.title + '-by ' + self.user.username





class Proveedor(models.Model):

    nombre = models.CharField(blank=True,null=True,max_length=100)
    correo = models.EmailField(blank=True,null=True)
    telefono = models.CharField(blank=True,null=True,max_length=10)

    ACTIVO = 'Activo'
    DESACTIVADO = 'Desactivado'

    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (DESACTIVADO, 'Desactivado'),
    ]

    estadodelprovedor = models.TextField(blank=True,null=True,choices=ESTADO_CHOICES,)
    #productos = models.CharField(blank=True,null=True,max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    # se ponen blank true  y null true para que no haya problema a la hora de no llenar esos campos.
    precioComun = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #precioMayoreo = models.IntegerField(blank=True, null=True)
    precioMayoreo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    canStock = models.IntegerField(blank=True, null=True)
    # ESTA FECHA SE INGRESARA EN AUTOMATICO 
    fechaingreso = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    tamaño = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    tiempodeProduccion = models.TimeField(blank=True, null=True)

    visto = models.BooleanField(default=False)
    ACTIVO = 'Activo'
    DESACTIVADO = 'Desactivado'

    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (DESACTIVADO, 'Desactivado'),
    ]
    
    estado = models.CharField(max_length=50, blank=True, null=True,choices=ESTADO_CHOICES,)
    #Este campo lo puedo eliminar   
    # SE AGREGO EL ID DE PROVEEDOR
    idProveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,blank=True,null=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    

    def __str__(self):
        return self.nombre

    # fecha_nacimiento = models.DateTimeField(null=True)


    # DE AQUI NO HAY NADA PENDIENTE
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    paterno = models.CharField(max_length=50)
    materno = models.CharField(max_length=50)

    MAYORISTA = 'Mayorista'
    COMUN = 'Menudista'

    ESTADO_CHOICES = [
        (MAYORISTA, 'Mayorista'),
        (COMUN, 'Menudista'),
    ]

    tipocliente = models.CharField(max_length=100, blank=True, null=True, choices=ESTADO_CHOICES)
    direccion = models.CharField(max_length=100,blank=True,null=True)
    fecharegistro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        
    fechanacimiento = models.DateField( blank=True, null=True)

    correo = models.EmailField( blank=True, null=True)
    celular = models.CharField(max_length=100, blank=True, null=True)
    
    referencias = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    
    

    def __str__(self):
        return self.nombre

#Primero se crea el modelo de la tabla -> despues el formulario - despues la vista -> despues las paginas ( nombre,nombre_detail,create_nombre).

# TABLAS NUEVAS 

class Servicio(models.Model):
    nombre = models.CharField(blank=True,null=True,max_length=100)
    descripcion = models.CharField(blank=True,null=True,max_length=100)
    # verificar si es integer o decimal
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
        
    tiempoestimado = models.IntegerField(blank=True,null=True)
    categoria = models.CharField(blank=True,null=True,max_length=100)
    notas = models.CharField(blank=True,null=True,max_length=100)

    ACTIVO = 'Activo'
    DESACTIVADO = 'Desactivado'

    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (DESACTIVADO, 'Desactivado'),
    ]

    estadoServicio = models.CharField(blank=True,null=True,max_length=100,choices=ESTADO_CHOICES,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    COMPRA = 'Compra'
    VENTA = 'Venta'

    ESTADO_CHOICES = [
        (COMPRA, 'Compra'),
        (VENTA, 'Venta'),
    ]
    
    tipoOrden = models.CharField(blank=True, max_length=100,null=True,choices=ESTADO_CHOICES,)
    # INVESTIGAR LOS DATOS QUE VAN EN LA FECHA
    fechaorden = models.DateField(auto_now_add=True,null=True,blank=True)
    idCliente = models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
    idProveedor = models.ForeignKey(Proveedor,null=True,blank=True,on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)
    idServicio = models.ForeignKey(Servicio,null=True,blank=True,on_delete=models.CASCADE)
    # FALTAN
    cantidadProductos = models.IntegerField(null=True,blank=True)
    precioUnitarioProducto = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    subtotalProductos = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

    cantidadServicios = models.IntegerField(null=True,blank=True)
    precioUnitarioServicios = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    subtotalServicio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

    totalOrden =  models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

    descripcion = models.TextField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    # LLAVES FORANEAS

    
    idEmpleado = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipoOrden

class Venta(models.Model):

    
    ACEPTADA = 'Aceptada'
    RECHAZADA = 'Rechazada'

    ESTADO_CHOICES = [
        (ACEPTADA, 'Aceptada'),
        (RECHAZADA, 'Rechazada'),
    ]
    
    visto = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    #idOrden = models.ForeignKey(Orden,null=True,blank=True,on_delete=models.CASCADE)
    
    FechaVenta = models.DateField(auto_now_add=True, null=True, blank=True)
    totalVenta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,blank=True, null=True)
    cantidad = models.IntegerField(null=True, blank=True)
    
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE,blank=True, null=True)
    cantidadservicio = models.IntegerField(null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    idCliente = models.ForeignKey(Cliente,null=True,blank=True,on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    
    estado = models.CharField(max_length=100,null=True,blank=True,choices=ESTADO_CHOICES,)

    def save(self, *args, **kwargs):
        if self.estado == 'Aceptada':
            producto_total = 0
            servicio_total = 0

            if self.cantidad > 0:
                producto_total = self.cantidad * self.producto.precioComun 
                if self.cantidad > self.producto.canStock:
                    raise ValueError("La cantidad elegida es mayor que la cantidad en stock del producto.")
                self.producto.canStock = self.producto.canStock - self.cantidad
                self.producto.save()

            if self.cantidadservicio > 0:
                servicio_total = self.cantidadservicio * self.servicio.precio

            self.totalVenta = producto_total + servicio_total

        super(Venta, self).save(*args, **kwargs)


    
    

class Compra(models.Model):
    fechaCompra = models.DateField(auto_now_add=True,null=True, blank=True)
    
    totalCompra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # ORDEN SE VA A ELIMINAR 

    #idOrden = models.ForeignKey(Orden,on_delete=models.CASCADE,null=True,blank=True)
    idProducto = models.ForeignKey(Producto, null=True, blank=True,on_delete=models.CASCADE)
    idProveedor = models.ForeignKey(Proveedor, null=True, blank=True,on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Usuario, null=True, blank=True,on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True, blank=True)
    


    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    
    def save(self, *args, **kwargs):

        #precioMayoreo
        self.totalCompra = self.cantidad * self.idProducto.precioMayoreo
        a = self.totalCompra
        
        self.idProducto.canStock = self.idProducto.canStock + self.cantidad

        self.idProducto.save()

        super(Compra, self).save(*args, **kwargs)


#Primero se crea el modelo de la tabla -> despues el formulario - despues la vista -> despues las paginas ( nombre,nombre_detail,create_nombre).
class Ticket(models.Model):
    fechaCreacion = models.DateTimeField(blank=True,null=True)
    asunto = models.CharField(max_length=100,blank=True,null=True)
    descripcion = models.CharField(blank=True,max_length=100,null=True)
    # Llaves foraneas
    idCliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,blank=True,null=True)
    idEmpleado = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True,null=True)
    # PREGUNTAR A ISSAC sobre este campo. 
    estadoTicket = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)



class IncidenteLaboral(models.Model):

    INTERNO = 'Interno'
    EXTERNO = 'Externo'

    ESTADO_CHOICES = [
        (INTERNO,'Interno'),
        (EXTERNO,'Externo'),
        ]
    horaIncidente = models.DateTimeField(blank=True,null=True)

    
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    
    reportadopor = models.CharField(max_length=100,blank=True,null=True)
    tipoIncidente = models.CharField(max_length=100,blank=True,null=True,choices=ESTADO_CHOICES)
    accionesCorrectivas = models.CharField(max_length=100,blank=True,null=True)
    comentarios = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)



class Opionion(models.Model):
    QUEJA = 'Queja'
    OPINION = 'Opinión'
    SUGERENCIA = 'Sugerencia'

    ESTADO_CHOICES = [
        (QUEJA, 'Queja'),
        (OPINION, 'Opinión'),
        (SUGERENCIA, 'Sugerencia'),
    ]

    Correo  = models.EmailField(blank=True,null=True)
    FechaRegistro = models.DateField(auto_now_add=True,blank=True,null=True)
    tipo = models.CharField(blank=True,null=True,max_length=100,choices=ESTADO_CHOICES)
    descripcion = models.TextField(blank=True,null=True)
    calificacion = models.IntegerField(blank=True,null=True,validators=[MinValueValidator(1), MaxValueValidator(10)])
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)


class Herramienta(models.Model):
    nombreHerramienta = models.CharField(blank=True,null=True,max_length=100)

    COMPUTADORA = 'Computadora'
    ROUTER = 'Router'
    IMPRESORA = 'Impresora'

    ESTADO_CHOICES = [
        (COMPUTADORA, 'Computadora'),
        (ROUTER, 'Router'),
        (IMPRESORA, 'Impresora'),
    ]

    tipo  =  models.CharField(blank=True,null=True,max_length=100,choices=ESTADO_CHOICES)
    marca = models.CharField(blank=True,null=True,max_length=100)
    fechaAdquisicion = models.DateField(blank=True,null=True)
    idProveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True,blank=True)

    ACTIVO = 'Activo'
    DESACTIVADO = 'Desactivado'

    ESTADO_CHOICES = [
        (ACTIVO, 'Activo'),
        (DESACTIVADO, 'Desactivado'),
    ]
    estadoHerramienta = models.CharField(blank=True,null=True,max_length=100,choices=ESTADO_CHOICES,)
    valor = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True,validators=[MinValueValidator(0)])
    notas = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)


    def __str__(self):
        return self.nombreHerramienta





# LLENAR PRIMERO LA TABLA HERRAMIENTA, y LA TABLA USUARIOS
class Mantenimiento(models.Model):
    idHerramienta = models.ForeignKey(Herramienta,on_delete=models.CASCADE,null=True,blank=True)
    # AÑO- MES - DIA
    fechaMantenimineto = models.DateField(blank=True,null=True)
    
    PREVENTIVO = 'Preventivo'
    CORRECTIVO = 'Correctivo'
    PREDICTIVO = 'Predictivo'

    ESTADO_CHOICES = [
        (PREVENTIVO, 'Preventivo'),
        (CORRECTIVO, 'Correctivo'),
        (PREDICTIVO, 'Predictivo'),
    ]
    tipoMantenimiento = models.CharField(max_length=100,null=True,blank=True,choices=ESTADO_CHOICES)
    # DEscripcionMantenimiento = Detalles
    detalles = models.CharField(max_length=100,null=True,blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='responsable_mantenimientos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='creador_mantenimientos')

    def __str__(self):
        return self.responsable