from datetime import datetime
from general import FacturaPDF




#todos PRIMERA PARTE: CONTENIDO DE DATOS GENERALES

#* DATOS A USAR EN EL SECTOR DE DATOS GENERALES

#* LISTA_1: DATOS GENERALES

lista_datos = (
    ( 'Fecha de factura:', '', 'Forma de pago:', ''),
    ( 'Número de factura:', '', 'Medio de pago:', ''),
    ( 'Fecha de vencimiento:', '', 'Orden de pedido:', '')
    )

arg = []
lista_datos_dicc ={
   'Fecha_factura' : 'MM/DD/AAAA',         #MM/DD/AAAA
   'Forma_pago' : 'Contado ',
   'Número_factura' : 'SETP990000003', 
   'Medio_pago' : 'Efectivo',
   'Fecha_vencimiento' : 'MM/DD/AAAA', 
   'Orden_pedido' : 'xxxxxx',
}

lista_datos_2 = (
   ('Fecha orden de pedido: ', 'MM/DD/AAAA'),

)
lista_datos_3 = (
( 'Código único de factura:', 'bbb32b343k5b465k7l67nnlLKBKLBKLBLKBLBgjgklhhhihil'),

)

#* LISTA_2: DATOS VENDEDOR

lista_datos_vendedor = (
    ( 'Nombre comercial:', 'AMBIENTES SEGUROS SAS', 'País:', 'Colombia '),
    ( 'NIT:', '901697756', 'Departamento:', 'Valle del Cauca'),
    ( 'Razón social:', 'AMBIENTES SEGUROS SAS', 'Municipio/Ciudad:', 'Cali'),
    ( 'Tipo de contribuyente:', 'Persona jurídica', 'Dirección:', 'Calle 5 # 3-33'),
    ( 'Régimen fiscal:', 'O-47', 'Móvil:', '3001562169'),
    ( 'Responsabilidad tributaria:', '01 - IVA', 'Correo:', 'admin@ambientes-seguros.com'),
    )

#* LISTA_3: DATOS COMPRADOR

lista_datos_comprador = (
    ( 'Nombre / Razón social:', 'Andres Pérez', 'País:', 'Colombia '),
    ( 'Tipo de Documento:', 'Cédula de ciudadania', 'Departamento:', 'Valle del Cauca'),
    ( 'Número de Documento:', '1112458987', 'Municipio/Ciudad:', 'Cali'),
    ( 'Tipo de contribuyente:', 'Persona natural', 'Dirección:', 'Calle 5 # 6-66'),
    ( 'Régimen fiscal:', 'R-99-PN', 'Móvil:', '3001566789'),
    ( 'Responsabilidad tributaria:', 'ZZ-No aplica', 'Correo:', 'andres_perez@gmail.com'),
    )*8

#* LISTA_4: ENCABEZADO DETALLE DE LOS PRODUCTOS

lista_detalle_productos=(
   ( 'No.', 'Código', 'Descripción', 'Cantidad', '$ Unit', 'Descuentos', 'Recargos', 'IVA', '%', '$ Unit de Venta'),

   )
 
 #* LISTA SUBTOTAL

lista_datos_subtotal = (
    ( 'Descuentos', '$ 0'), 
     ('Recargos', '$ 0'),

    )

#* LISTA TOTAL BRUTO

lista_datos_total_bruto = (
    ( 'IVA', '$ 38.000'), 
     ('Otros Impuestos', '$ 0'),

    )

#* TOTAL NETO FACTURA

lista_global = (
    ( 'Descuento Global', '$ 0'), 
     ('Recargo Global', '$ 0'),
)
    
if __name__  == '__main__':
   mi_factura_e = FacturaPDF(lista_datos, lista_datos_2, lista_datos_3, lista_datos_vendedor, lista_datos_comprador, lista_detalle_productos , lista_datos_subtotal, lista_datos_total_bruto, lista_global,lista_datos_dicc) 
   tiempo_actual = datetime.now()
   print(tiempo_actual)



