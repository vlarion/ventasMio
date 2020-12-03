from django.db import models

class Precio(models.Model):
    idPrecio = models.AutoField(primary_key=True)
    precioCosto=models.IntegerField()
    ganancia=models.IntegerField()
    precioVenta=models.IntegerField()
    class Meta:
        db_table = 'precio' 

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=200)
    class Meta:
        db_table = 'region' 

class Provincia(models.Model):
    idProvincia = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=200)
    idRegion=models.ForeignKey(Region, on_delete=models.CASCADE)
    class Meta:
        db_table = 'provincia' 

class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreComuna = models.CharField(max_length=200)
    idProvincia=models.ForeignKey(Provincia, on_delete=models.CASCADE) 
    class Meta:
        db_table = 'comuna' 


class Proveedor(models.Model):
    idProv=models.AutoField(primary_key=True)
    nombreProv=models.CharField(max_length=50)
    rut=models.CharField(max_length=15)
    razonSocial=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    email=models.CharField(max_length=50)    
    class Meta:
        db_table = 'proveedor'

class Cargo(models.Model):
    idCargo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    class Meta:
        db_table = 'cargo'


class Marca(models.Model):
    idMarca=models.AutoField(primary_key=True)
    nombreMarca=models.CharField(max_length=50)
    idProv=models.ForeignKey(Proveedor, on_delete=models.CASCADE) 
    class Meta:
        db_table = 'marca'

class Modelo(models.Model):
    idModelo=models.AutoField(primary_key=True)
    nombreModelo=models.CharField(max_length=50)
    idMarca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    idProv=models.ForeignKey(Proveedor, on_delete=models.CASCADE) 
    class Meta:
        db_table = 'modelo'

class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True)
    nombreProd=models.CharField(max_length=50)
    estado=models.CharField(max_length=10)
    garantia=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    fichaTecnica=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=200)
    imgProducto=models.CharField(max_length=50)
    idPrecio=models.ForeignKey(Precio, on_delete=models.CASCADE)
    idMarca=models.ForeignKey(Marca, on_delete=models.CASCADE)
    idModelo=models.ForeignKey(Modelo, on_delete=models.CASCADE)
    idProv=models.ForeignKey(Proveedor, on_delete=models.CASCADE)   
    class Meta:
        db_table = 'producto'

class Persona(models.Model):
    idPersona=models.AutoField(primary_key=True)
    run=models.IntegerField()
    dv=models.CharField(max_length=1)
    nombre=models.CharField(max_length=40)
    apePat=models.CharField(max_length=40)
    apeMat=models.CharField(max_length=40)
    fono=models.IntegerField()
    email=models.EmailField(blank=True)
    direccion=models.CharField(max_length=40)
    imgPersona=models.CharField(max_length=50)
    ifCargo=models.ForeignKey(Cargo, on_delete=models.CASCADE)
    class Meta:
        db_table = 'persona'


class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True)
    nombreCat=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    class meta:
        db_table = 'categoria'

class Departamento(models.Model):
    idDepa=models.AutoField(primary_key=True)
    nombreDepa=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    class Meta:
        db_table = 'departamento'
        
class Sueldo(models.Model):
    idSueldo=models.AutoField(primary_key=True)
    sueldoBase=models.IntegerField()
    comision=models.IntegerField()
    bono=models.IntegerField()
    class Meta:
        db_table = 'vendedor'

class Factura(models.Model):
    idFactura=models.AutoField(primary_key=True)
    fecha=models.DateTimeField('sysdate')
    neto=models.IntegerField()
    iva=models.IntegerField()
    total=models.IntegerField()
    idProv=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'factura'
        
class Boleta(models.Model):
    idBoleta=models.AutoField(primary_key=True)
    fecha=models.DateTimeField('sysdate')
    monto=models.IntegerField()    
    class Meta:
        db_table = 'boleta'

class DetalleFac(models.Model):
    idDetFac=models.AutoField(primary_key=True)    
    idProducto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    idFactura=models.ForeignKey(Factura, on_delete=models.CASCADE)
    class Meta:
        db_table = 'detalle_fac'

class DetalleBol(models.Model):
    idDetBol=models.AutoField(primary_key=True)
    idBoleta=models.ForeignKey(Boleta, on_delete=models.CASCADE)
    idProducto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadProd=models.IntegerField()
    class Meta:
        db_table = 'detalle_bol'



class Gastos(models.Model):
    idGasto=models.AutoField(primary_key=True)
    monto=models.IntegerField()
    detalle=models.CharField(max_length=200)
    fecha=models.DateTimeField('sysdate')
    idProv=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'gastos'
        
class Deterioro(models.Model):
    idDeterioro=models.AutoField(primary_key=True)
    idProducto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=200)
    fecha=models.DateTimeField('sysdate')
    class Meta:
        db_table = 'deterioro'
        
class Boleta_null(models.Model):
    idBolNull=models.AutoField(primary_key=True)
    fecha=models.DateTimeField('sysdate')
    descripcion=models.CharField(max_length=200)
    idBoleta=models.ForeignKey(Boleta, on_delete=models.CASCADE)
    class Meta:
        db_table = 'boleta_null'
        
class Factura_null(models.Model):
    idFacNull=models.AutoField(primary_key=True)
    fecha=models.DateTimeField('sysdate')
    descripcion=models.CharField(max_length=200)
    idFactura=models.ForeignKey(Factura, on_delete=models.CASCADE)
    class Meta:
        db_table = 'factura_null'
        
class Telefono(models.Model):
    idFono=models.AutoField(primary_key=True)
    numeroFono=models.IntegerField()
    compañia=models.CharField(max_length=20)
    idPersona=models.IntegerField()
    idFactura=models.ForeignKey(Factura, on_delete=models.CASCADE)
    class Meta:
        db_table = 'telefono'
        

