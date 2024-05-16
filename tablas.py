from fpdf import FPDF
from referencias import *


class CreacionTablas():

    def build_datos_generales(self, lista_datos:list):
        
        for valor in lista_datos:
    
            self.pdf.set_font('Arial','B',10)        #? FUENTE, TIPO Y TAMAÑO DE LA LETRA
            self.pdf.cell(w = 45, h = 6, txt = str(valor[0]), border = 0,
                    align = 'L', fill = 0)

            self.pdf.set_font('Arial','',9) 
            bcol_set(self.pdf, 'light_gray')       
            self.pdf.cell(w = 60, h = 6, txt = valor[1], border = 0,
                    align = 'L', fill = 1)

            self.pdf.set_font('Arial','B',10)       
            self.pdf.cell(w = 50, h = 6, txt = valor[2], border = 0,
                    align = 'L', fill = 0)      #? SI CAMBIO EL BORDER Y EL FILL A 1, EN EL PRIMERO OBTENGO EL RECUADRO Y EN EL SEGUNDO EL RELLENO DE LA CELDA.

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

pdf=FPDF()           
pdf.ln(45)
pdf.build_datos_generales()
pdf.ln(0)
pdf.build_datos_generales_2()
pdf.ln(0)
pdf.build_datos_generales_3()