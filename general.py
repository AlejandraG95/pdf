from fpdf import FPDF
from referencias import *
from encabezado import MiPDF

'''
P : #Formato Vertical
L : #Formato Horizontal

A4 : 210x297mm
'''

#* COMENZAMOS CON EL FORMATO DE LA PÁGINA
pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')   #? La orientación la podemos cambiar: si colocamos P la hoja estaria verticalmente, si colocamos L la hoja se coloca horizontal.



class FacturaPDF():
    

    def __init__(self, lista_datos, lista_datos_2, lista_datos_3, lista_datos_vendedor, lista_datos_comprador, lista_detalle_productos, lista_datos_subtotal, lista_datos_total_bruto,lista_global, lista_datos_dicc ) -> None:

        #* ATRIBUTOS
        self.pdf = MiPDF()
        self.pdf.alias_nb_pages() #? PARA DETECTAR EL NÚMERO TOTAL DE PAGINAS EN EL PIE DE PÁGINA.
        self.pdf.add_page()
        self.pdf.ln(45)
        

        #* LINEAS Y TITULO DE FACTURACIÓN
        self.pdf.line(10,46,200,46)       #? x1,y1,x2,y2
        self.pdf.set_font('Arial', 'B', 20)
        self.pdf.text(x=61, y=54, txt='FACTURA ELECTRÓNICA')
        self.pdf.line(10,56,200,56) 
        
        #* TABLAS.
        
        self.build_datos_generales(lista_datos, lista_datos_dicc)
        self.pdf.ln(0)
        self.build_datos_generales_2(lista_datos_2)
        self.pdf.ln(0)
        self.build_datos_generales_3(lista_datos_3)

        #* LÍNEAS ENTRE LAS CELDAS GRISES
        self.crear_linea(55,77,115,77,0.5, 'white')
        
        #* DATOS DEL VENDEDOR
        self.datos_vendedor()    
        self.pdf.ln(0)   
        self.build_tabla_vendedor(lista_datos_vendedor)

        #* DATOS DEL COMPRADOR
        self.datos_comprador()
        self.build_tabla_comprador(lista_datos_comprador)

        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.ln(10)

        #*DETALLES DEL PRODUCTO
        self.encabezado_detalles_producto(lista_detalle_productos)

        self.productos_comprados()

        #* DATOS SUBTOTALES
        self.datos_subtotal()
        self.elementos_subtotal(lista_datos_subtotal)

        #* TOTAL BRUTO
        self.total_bruto()
        self.elementos_total_bruto(lista_datos_total_bruto)

        #* TOTAL IMPUESTOS
        self.total_bruto()

        #* TOTAL NETO FACTURA
        self.total_neto()

         #* TOTAL GLOBAL
        self.total_global(lista_global)

        #* TOTAL FACTURA
        self.total_factura()

       #* SAVE PDF
        self.pdf.output('gral_1133.pdf') 





    def build_datos_generales(self, lista_datos:list, lista_datos_dicc:dict):
        
        for valor in lista_datos:
    
            self.pdf.set_font('Arial','B',10)        #? FUENTE, TIPO Y TAMAÑO DE LA LETRA
            self.pdf.cell(w = 45, h = 6, txt = str(valor[0]), border = 0,
                    align = 'L', fill = 0)

            

            self.pdf.set_font('Arial','B',10)       
            self.pdf.cell(w = 50, h = 6, txt = valor[2], border = 0,
                    align = 'L', fill = 0)      #? SI CAMBIO EL BORDER Y EL FILL A 1, EN EL PRIMERO OBTENGO EL RECUADRO Y EN EL SEGUNDO EL RELLENO DE LA CELDA.

            
        for valor in lista_datos_dicc:
             
             self.pdf.set_font('Arial','',9) 
             bcol_set(self.pdf, 'light_gray')       
             self.pdf.cell(w = 60, h = 6, txt = valor[1], border = 0,
                    align = 'L', fill = 1)
             
             bcol_set(self.pdf, 'light_gray')         #? COLOR DEL RELLENO
             self.pdf.set_font('Arial','',9)     
             self.pdf.multi_cell(w = 0, h = 6, txt = valor[3], border = 0,
                    align = 'L', fill = 1)      #? ESTE ÚLTIMO EN MULTICELL PARA QUE HAGA SALTO DE LÍNEA
    

    def build_datos_generales_2(self, lista_datos_2:list):
        
        for valor in lista_datos_2:
            
            self.pdf.set_font('Arial','B',10)        
            self.pdf.cell(w = 45, h = 6, txt = str(valor[0]), border = 0,
                    align = 'L', fill = 0)

            self.pdf.set_font('Arial','',9) 
            bcol_set(self.pdf, 'light_gray')      
            self.pdf.multi_cell(w = 60, h = 6, txt = valor[1], border = 0,
                    align = 'L', fill = 1)      

    def build_datos_generales_3(self, lista_datos_3:list):
        
        for valor in lista_datos_3:
            
            self.pdf.set_font('Arial','B',10)        
            
            self.pdf.cell(w = 45, h = 6, txt = str(valor[0]), border = 0,
                    align = 'L', fill = 0)


            self.pdf.set_font('Arial','',9) 
            bcol_set(self.pdf, 'light_gray')      
            self.pdf.multi_cell(w = 0, h = 6, txt = valor[1], border = 0,
                    align = 'L', fill = 1)        

    def crear_linea(self,x1,y1,x2,y2, w_line=0.5, color ='white'):    
        
            dcol_set(self.pdf, color)
            self.pdf.set_line_width(w_line)
            
            self.pdf.line(55,69,115,69)        #* FILA 1
            self.pdf.line(165.1,69,199.7,69)   #* FILA 1
            self.pdf.line(55,75,115,75)        #* FILA 2
            self.pdf.line(165.1,75,199.7,75)   #* FILA 2
            self.pdf.line(55,81,115,81)        #* FILA 3
            self.pdf.line(165.1,81,199.7,81)   #* FILA 3
            self.pdf.line(55,86.8,115,86.8)    #* FILA 4
       
        
         #* DATOS DEL VENDEDOR

    def datos_vendedor(self,color ='blue_light' ):
        
        # DATOS DEL VENDEDOR
        self.pdf.ln(8)
        self.pdf.set_font('Arial','B',10)
        bcol_set(self.pdf, color)       
        self.pdf.multi_cell(w = 50, h = 7, txt= ' DATOS DEL VENDEDOR ', border = 0,
            align = 'L', fill = 1) 
        
        #* LISTA_2

    def build_tabla_vendedor(self,  lista_datos_vendedor:list ):
        
        dcol_set(self.pdf, 'black')
        self.pdf.set_line_width(0.3) 
        self.pdf.ln(0)

        for valor in lista_datos_vendedor:

    
                self.pdf.set_font('Arial','B',10)      
                
                self.pdf.cell(w = 50, h = 7, txt = str(valor[0]), border = 1,
                        align = 'L', fill = 0)
                

                self.pdf.set_font('Arial','',9) 
                bcol_set(self.pdf, 'light_gray')       
                self.pdf.cell(w = 55, h = 7, txt = valor[1], border = 1,
                        align = 'L', fill = 1)
                
                self.pdf.set_font('Arial','B',10)       
                self.pdf.cell(w = 35, h = 7, txt = valor[2], border = 1,
                        align = 'L', fill = 0)      
                
                bcol_set(self.pdf, 'light_gray')        
                self.pdf.set_font('Arial','',9)     
                self.pdf.multi_cell(w = 0, h = 7, txt = valor[3], border = 1,
                align = 'L', fill = 1)  


        #* DATOS DEL COMPRADOR
        
    def datos_comprador(self,color ='blue_light' ):
        
       # DATOS DEL COMPRADOR
        
        self.pdf.ln(8)
        self.pdf.set_font('Arial','B',10)
        bcol_set(self.pdf, color)       
        self.pdf.multi_cell(w = 50, h = 7, txt= ' DATOS DEL COMPRADOR ', border = 0,
            align = 'L', fill = 1) 
        
        #* LISTA_3

    def build_tabla_comprador(self,  lista_datos_comprador:list ):
        
        dcol_set(self.pdf, 'black')
        self.pdf.set_line_width(0.3) 
        self.pdf.ln(0)

        for valor in lista_datos_comprador:

    
                self.pdf.set_font('Arial','B',10)      
                
                self.pdf.cell(w = 50, h = 7, txt = str(valor[0]), border = 1,
                        align = 'L', fill = 0)
                

                self.pdf.set_font('Arial','',9) 
                bcol_set(self.pdf, 'light_gray')       
                self.pdf.cell(w = 55, h = 7, txt = valor[1], border = 1,
                        align = 'L', fill = 1)
                
                self.pdf.set_font('Arial','B',10)       
                self.pdf.cell(w = 35, h = 7, txt = valor[2], border = 1,
                        align = 'L', fill = 0)      
                
                bcol_set(self.pdf, 'light_gray')        
                self.pdf.set_font('Arial','',9)     
                self.pdf.multi_cell(w = 0, h = 7, txt = valor[3], border = 1,
                align = 'L', fill = 1)

    #* DETALLES DEL PRODUCTO

    def encabezado_detalles_producto(self, lista_detalle_productos:list):
        
        self.pdf.ln(30)


        for valor in lista_detalle_productos:

                self.pdf.set_font('Arial','B',10)
                bcol_set(self.pdf, 'blue_light')

                self.pdf.cell(w = 9, h = 10, txt = valor[0], border = 1,
                        align = 'C', fill = 1)
                       
                self.pdf.cell(w = 15, h = 10, txt = valor[1], border = 1,
                        align = 'C', fill = 1)
                      
                self.pdf.cell(w = 30, h = 10, txt = valor[2], border = 1,
                        align = 'C', fill = 1)      
                   
                self.pdf.cell(w = 16, h = 10, txt = valor[3], border = 1,
                        align = 'C', fill = 1)

                self.pdf.cell(w = 17, h = 10, txt = valor[4], border = 1,
                        align = 'C', fill = 1)
                       
                self.pdf.cell(w = 20, h = 10, txt = valor[5], border = 1,
                        align = 'C', fill = 1)
                      
                self.pdf.cell(w = 20, h = 10, txt = valor[6], border = 1,
                        align = 'C', fill = 1)      
                   
                self.pdf.cell(w = 17, h = 10, txt = valor[7], border = 1,
                align = 'C', fill = 1)

                self.pdf.cell(w = 13, h = 10, txt = valor[8], border = 1,
                align = 'C', fill = 1)

                self.pdf.multi_cell(w = 35, h = 10, txt = valor[9], border = 1,
                align = 'C', fill = 1)

    def productos_comprados(self, No='1' , Código='5', Descripción='Cámaras', Cantidad='8', val_unit='200000', Descuentos='0' , Recargos='0', iva='0', porcentaje='0', val_uni_venta='0'):
         
        
                dcol_set(self.pdf, 'black')
                self.pdf.set_line_width(0.3) 
                self.pdf.ln(0)
                self.pdf.set_font('Arial','',9)
                
                self.pdf.cell(w = 9, h = 10, txt = No, border = 1,
                        align = 'L', fill = 0)
                       
                self.pdf.cell(w = 15, h = 10, txt = Código, border = 1,
                        align = 'L', fill = 0)
                      
                self.pdf.cell(w = 30, h = 10, txt = Descripción, border = 1,
                        align = 'L', fill = 0)      
                   
                self.pdf.cell(w = 16, h = 10, txt = Cantidad, border = 1,
                        align = 'L', fill = 0)

                self.pdf.cell(w = 17, h = 10, txt = val_unit, border = 1,
                        align = 'L', fill = 0)
                       
                self.pdf.cell(w = 20, h = 10, txt = Descuentos, border = 1,
                        align = 'L', fill = 0)
                      
                self.pdf.cell(w = 20, h = 10, txt = Recargos, border = 1,
                        align = 'L', fill = 0)      
                   
                self.pdf.cell(w = 17, h = 10, txt = iva, border = 1,
                align = 'L', fill = 0)

                self.pdf.cell(w = 13, h = 10, txt = porcentaje, border = 1,
                align = 'L', fill = 0)

                self.pdf.multi_cell(w = 35, h = 10, txt = val_uni_venta, border = 1,
                align = 'L', fill = 0)

                self.pdf.add_page()
                self.pdf.ln(10) 


    #* DATOS TOTALES

     # ENCABEZADO SUBTOTAL
    def datos_subtotal(self, val_uni_venta='$200.000'):
         
         self.pdf.ln(30)

         #* TABLA
         self.pdf.set_font('Arial','B',10)
         bcol_set(self.pdf, 'blue_light')

         self.pdf.cell(w = 60, h = 7, txt = 'Subtotal', border = 1, align = 'C', fill = 1)
         self.pdf.multi_cell(w = 20, h = 7, txt = val_uni_venta, border = 1, align = 'C', fill = 1)

        # COMPONENTES SUBTOTAL
    def elementos_subtotal(self, lista_datos_subtotal:list):
         dcol_set(self.pdf, 'black')
         self.pdf.set_line_width(0.3) 
         self.pdf.ln(0)
         self.pdf.set_font('Arial','',9)

         for valor in lista_datos_subtotal:

                self.pdf.cell(w = 60, h = 7, txt = str(valor[0]), border = 1,
                        align = 'L', fill = 0)
                
                        
                self.pdf.multi_cell(w = 20, h = 7, txt = valor[1], border = 1,
                        align = 'L', fill = 0)
                
       
        #*TOTAL BRUTO

    def total_bruto(self, total_bruto='$0' ):
         
         #* TABLA
         self.pdf.set_font('Arial','B',10)
         bcol_set(self.pdf, 'blue_light')

         self.pdf.cell(w = 60, h = 7, txt = 'Total Bruto Factura', border = 1, align = 'C', fill = 1)
         self.pdf.multi_cell(w = 20, h = 7, txt = total_bruto, border = 1, align = 'C', fill = 1)

    def elementos_total_bruto(self, lista_datos_total_bruto:list):
         dcol_set(self.pdf, 'black')
         self.pdf.set_line_width(0.3) 
         self.pdf.ln(0)
         self.pdf.set_font('Arial','',9)

         for valor in lista_datos_total_bruto:

    
                self.pdf.cell(w = 60, h = 7, txt = str(valor[0]), border = 1,
                        align = 'L', fill = 0)
    
          
                self.pdf.multi_cell(w = 20, h = 7, txt = valor[1], border = 1,
                        align = 'L', fill = 0)
                
        #* TOTAL IMPUESTOS

    def total_bruto(self, total_impuestos='$38.000' ):

        #* TABLA
        self.pdf.set_font('Arial','B',10)
        bcol_set(self.pdf, 'blue_light')

        self.pdf.cell(w = 60, h = 7, txt = 'Total Impuestos =', border = 1, align = 'L', fill = 1)
        self.pdf.multi_cell(w = 20, h = 7, txt = total_impuestos, border = 1, align = 'C', fill = 1)


        #* TOTAL NETO FACTURA

    def total_neto(self, total_neto_factura='$238.000'):

         #* TABLA
        self.pdf.set_font('Arial','B',10)
        bcol_set(self.pdf, 'blue_light')

        self.pdf.cell(w = 60, h = 7, txt = 'Total Neto Factura =', border = 1, align = 'L', fill = 1)
        self.pdf.multi_cell(w = 20, h = 7, txt = total_neto_factura, border = 1, align = 'C', fill = 1)

        #* TOTAL GLOBAL

    def total_global(self, lista_global: list):

        dcol_set(self.pdf, 'black')
        self.pdf.set_line_width(0.3) 
        self.pdf.ln(0)
        self.pdf.set_font('Arial','',9)

        for valor in lista_global:

    
                self.pdf.cell(w = 60, h = 7, txt = str(valor[0]), border = 1,
                        align = 'L', fill = 0)
                
                        
                self.pdf.multi_cell(w = 20, h = 7, txt = valor[1], border = 1,
                align = 'L', fill = 0)
        
        
        #* TOTAL FACTURA
        
    def total_factura(self, total_factura='$238.000'):
        
        #* TABLA

        self.pdf.set_font('Arial','B',10)
        bcol_set(self.pdf, 'blue_light')

        self.pdf.cell(w = 60, h = 7, txt = 'Total Factura =', border = 1, align = 'L', fill = 1)
        self.pdf.multi_cell(w = 20, h = 7, txt = total_factura, border = 1, align = 'C', fill = 1)
