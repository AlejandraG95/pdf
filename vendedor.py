from fpdf import FPDF
from referencias import *


class Vendedor():
        
        def datos_vendedor(self):

            self.ln(8)
            self.set_font('Arial','B',10)
            bcol_set( 'blue_light')       
            self.multi_cell(w = 50, h = 7, txt= ' DATOS DEL VENDEDOR ', border = 0,
                align = 'L', fill = 1) 
          
            