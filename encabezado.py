from fpdf import FPDF

class MiPDF(FPDF):


#* ENCABEZADO

    def header(self, empresa='AMBIENTES SEGUROS SAS', nit = '901697756', ciudad='Cali - Valle del Cauca', movil='3001562169', correo='admin@ambientes-seguros.com'):
        
        #IMAGEN LOGO EMPRESA (.JPG, .PNG)
        self.image('ambienteslogo.png', x=10, y=10, w=35, h=30)

        #AMBIENTES SEGUROS ,   Arial bold 15
        self.set_font('Arial', 'B', 15)
        self.text(x=70, y=20, txt=empresa)     #? Posición del texto, solo acepta str en caso de ingresar un float o un int, se debe convertir a cadena ej:1, str(1)
        
        #NIT
        self.set_font('Arial', 'B', 10)
        self.text(x=94, y=25, txt=f'NIT:{nit}')

        #CIUDAD
        self.set_font('Arial', 'B', 10)
        self.text(x=88, y=30, txt=ciudad)

        #CONTÁCTO
        self.set_font('Arial', 'B', 10)
        self.text(x=90.6, y=35, txt=f'movil: {movil}')

        #CORREO
        self.set_font('Arial', 'B', 10)
        self.text(x=72, y=40, txt=f'Correo: {correo}')

        #IMAGEN QR
        self.image('generador_qr.png', x=166, y=7, w=35, h=35)
      
        # ESPACIO ENTRE EL ENCABEZADO Y EL CONTENIDO
        self.ln(8)
        


    #* PIE DE PÁGINA
    
    def footer(self):

       
         # Arial italic 11
        self.set_font('Arial', 'I', 11)

        self.set_y(-20) #? COMO SE VA A COLOCAR ABAJO COLOCAMOS VALORES NEGATIVOS PARA QUE EMPIECE DESDE LA PARTE INFERIOR DE LA HOJA.
        
        self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}', border = 0, 
                  align = 'C', fill = 0)  #FILL: RELLENO DE LA FIGURA


        #* LÍNEAS DE PIE DE PÁGINA
        self.line(10,279,200,279)
        self.line(10,285,200,285) 
        self.ln(8)
# Instantiation of inherited class
