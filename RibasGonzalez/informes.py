import os, var, shutil
from PIL import Image
from PyQt6 import QtSql, QtWidgets
from reportlab.pdfgen import canvas
from datetime import datetime
from svglib.svglib import svg2rlg
import conexion

class Informes:
    def reportclientes(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre =  fecha + '_listadoclientes.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO CLIENTES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            var.report.drawString(250,250, 'Mi primer informe')
            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('listadoclientes.pdf'):
                    os.startfile('%s\\%s' % (rootPath, file))

        except Exception as error:
            print('Error LISTADO CLIENTES :', error)

    def topInforme(titulo):
        try:
            ruta_logo = '.\\img\\logo.ico'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Transportes Teis')
                var.report.drawString(240, 695, titulo)
                var.report.line(50, 690, 525, 690)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: cartesteisr@mail.com')

            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')

        except Exception as error:
            print('Error en cabecera informe:', error)

    def footInforme(titulo):
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)