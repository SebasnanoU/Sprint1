import csv
from django.shortcuts import render
from .models import update_archivo, products

def index(request):
    archivos = update_archivo.objects.all()
    if request.method == 'POST' and 'archivo' in request.FILES:
        archivo_csv = request.FILES['archivo']
        decoded_file = archivo_csv.read().decode('latin-1')  # Utilizar 'latin-1' en lugar de 'utf-8'
        reader = csv.reader(decoded_file.splitlines(), delimiter=';')
        # next(reader)  # Saltar la primera línea si contiene encabezados

        for fila in reader:
            codigo_producto = int(fila[0])
            nombre_producto = fila[1]
            nitproveedor = int(fila[2])
            precio_compra = float(fila[3])
            ivacompra = float(fila[4])
            precio_venta = float(fila[5])

            producto = products.objects.create(
                código_producto=codigo_producto,
                nombre_producto=nombre_producto,
                nitproveedor=nitproveedor,
                precio_compra=precio_compra,
                ivacompra=ivacompra,
                precio_venta=precio_venta
            )

    return render(request, 'file_manager/index.html', {'archivos': archivos})


def ver_productos(request):
    productos = products.objects.all()
    return render(request, 'file_manager/ver_productos.html', {'productos': productos})