import qrcode


def crear_qr(ingresar_datos:str):
    img = qrcode.make(ingresar_datos)
    f = open("generador_qr.png", "wb")
    img.save(f)
    f.close()


if __name__ == '__main__':
    crear_qr('datos_factura')
    print('facturación')