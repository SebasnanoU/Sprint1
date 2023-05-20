from django.db import models

class products(models.Model):
    código_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    nitproveedor = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    ivacompra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)


class update_archivo(models.Model):
    archivo = models.FileField(upload_to='archivos/')
    