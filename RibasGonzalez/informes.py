import os, var

from PyQt6 import QtSql, QtWidgets, QtGui
from PIL import Image
from reportlab.pdfgen import canvas
from datetime import datetime

import conexion
import eventos

class Informes:
    @staticmethod
    def reportclientes():
        """

        Genera un informe en formato PDF con el listado de clientes.

        Este método genera un informe en formato PDF que contiene un listado de todos los clientes registrados en la base de datos.
        El informe incluye información como el código del cliente, su DNI (encriptado), razón social, municipio, teléfono y fecha de baja (si existe).
        El informe se guarda en la carpeta 'informes' con un nombre que incluye la fecha y hora de creación.
        Después de generar el informe, se abre automáticamente para que el usuario lo visualice.

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoclientes.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO CLIENTES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = 'CODIGO', 'DNI', 'RAZON SOCIAL', 'MUNICIPIO', 'TELEFONO', 'FECHA BAJA'
            var.report.setFont('Helvetica-Bold', size=9)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(120, 675, str(items[1]))
            var.report.drawString(170, 675, str(items[2]))
            var.report.drawString(290, 675, str(items[3]))
            var.report.drawString(390, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)
            # obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dnicli, social, municli, movilcli, bajacli from clientes order by social')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 60
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 80, 'Pagina siguiente...')
                        var.report.showPage()  # crea una pagina nueva
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica', size=10)
                        var.report.drawString(60, 675, str(items[0]))
                        var.report.drawString(120, 675, str(items[1]))
                        var.report.drawString(170, 675, str(items[2]))
                        var.report.drawString(290, 675, str(items[3]))
                        var.report.drawString(390, 675, str(items[4]))
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50, 670, 525, 670)
                        i = 60
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i, j, str(query.value(0)))
                    var.report.drawString(i + 40, j, Informes.encriptarDNI(str(query.value(1))))
                    var.report.drawString(i + 115, j, str(query.value(2)))
                    var.report.drawString(i + 235, j, str(query.value(3)))
                    var.report.drawString(i + 335, j, str(query.value(4)))
                    var.report.drawString(i + 405, j, str(query.value(5)))
                    j = j - 20
            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))

        except Exception as error:
            print('Error LISTADO CLIENTES :', error)



    @staticmethod
    def reportdrivers():
        """

        Genera un informe en formato PDF con el listado de conductores.

        Este método genera un informe en formato PDF que contiene un listado de todos los conductores registrados en la base de datos.
        El informe incluye información como el código del conductor, apellidos, nombre, teléfono, licencias y fecha de baja (si existe).
        El informe se guarda en la carpeta 'informes' con un nombre que incluye la fecha y hora de creación.
        Después de generar el informe, se abre automáticamente para que el usuario lo visualice.

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoconductores.pdf'
            var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO CONDUCTORES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            items = 'CODIGO', 'APELLIDOS', 'NOMBRE', 'TELEFONO', 'LICENCIAS', 'FECHA BAJA'
            var.report.setFont('Helvetica-Bold', size=9)
            var.report.drawString(50, 675, str(items[0]))
            var.report.drawString(120, 675, str(items[1]))
            var.report.drawString(210, 675, str(items[2]))
            var.report.drawString(290, 675, str(items[3]))
            var.report.drawString(390, 675, str(items[4]))
            var.report.drawString(460, 675, str(items[5]))
            var.report.line(50, 670, 525, 670)
            # obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers order by apeldri')
            var.report.setFont('Helvetica', size=9)
            if query.exec():
                i = 60
                j = 655
                while query.next():
                    if j <= 80:
                        var.report.drawString(450, 80, 'Pagina siguiente...')
                        var.report.showPage()  # crea una pagina nueva
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        var.report.setFont('Helvetica', size=10)
                        var.report.drawString(55, 675, str(items[0]))
                        var.report.drawString(120, 675, str(items[1]))
                        var.report.drawString(210, 675, str(items[2]))
                        var.report.drawString(290, 675, str(items[3]))
                        var.report.drawString(390, 675, str(items[4]))
                        var.report.drawString(460, 675, str(items[5]))
                        var.report.line(50, 670, 525, 670)
                        i = 60
                        j = 655
                    var.report.setFont('Helvetica', size=9)
                    var.report.drawCentredString(i, j, str(query.value(0)))
                    var.report.drawString(i + 50, j, str(query.value(1)))
                    var.report.drawString(i + 155, j, str(query.value(2)))
                    var.report.drawString(i + 235, j, str(query.value(3)))
                    var.report.drawCentredString(i + 345, j, str(query.value(4)))
                    var.report.drawString(i + 405, j, str(query.value(5)))
                    j = j - 20
            var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))

        except Exception as error:
            print('Error LISTADO conductores :', error)



    def topInforme(titulo):
        """

        Agrega la cabecera al informe PDF.

        Este método agrega la cabecera al informe PDF, incluyendo el título del informe, el logotipo de la empresa y la información de contacto.
        La cabecera incluye el nombre de la empresa, el título del informe, la dirección, el teléfono y el correo electrónico de contacto.

        :param titulo: El título del informe.

        """
        try:
            ruta_logo = '.\\img\\logo.ico'
            logo = Image.open(ruta_logo)

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Car Teis')
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
        """

        Agrega el pie de página al informe PDF.

        Este método agrega el pie de página al informe PDF, incluyendo la fecha de generación del informe, el título del informe
        y el número de página.

        :param titulo: El título del informe.

        """
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



    def encriptarDNI(dni):
        """

        Encripta parcialmente el número de DNI ocultando los primeros caracteres.

        Este método encripta parcialmente el número de DNI ocultando los primeros caracteres, dejando visibles los últimos cuatro
        dígitos.

        :param dni: El número de DNI a encriptar.
        :return: El DNI encriptado.

        """
        dni = "******" + dni[6:]
        dni_lista = list(dni)
        dni_lista[8] = "*"
        dni_modificado = ''.join(dni_lista)
        return dni_modificado



    @staticmethod
    def checkboxinforme():
        """

        Muestra un cuadro de diálogo para que el usuario seleccione qué informes desea generar.

        Este método muestra un cuadro de diálogo con opciones para generar informes de conductores y/o clientes.
        El usuario puede marcar las casillas correspondientes y hacer clic en "Aceptar" para generar los informes seleccionados.
        Si el usuario no selecciona ningún informe y hace clic en "Aceptar", se mostrará un mensaje de error.

        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Realizar Informe")
            mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
            mbox.setText("Seleccione informe/es")

            conductorcheck = QtWidgets.QCheckBox("Informe de conductores")
            clientecheck = QtWidgets.QCheckBox("Informe de clientes")

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(conductorcheck)
            layout.addWidget(clientecheck)

            container = QtWidgets.QWidget()
            container.setLayout(layout)

            mbox.layout().addWidget(container, 1, 1, 1, mbox.layout().columnCount())

            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Aceptar')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('Cancelar')

            resultado = mbox.exec()

            if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
                if conductorcheck.isChecked():
                    eventos.Eventos.mensaje("Aviso", "Informe de conductores creado")
                    Informes.reportdrivers()
                if clientecheck.isChecked():
                    eventos.Eventos.mensaje("Aviso", "Informe de clientes creado")
                    Informes.reportclientes()
                if not (conductorcheck.isChecked() or clientecheck.isChecked()):
                    eventos.Eventos.error("Aviso", "No se ha seleccionado ningún informe")

        except Exception as error:
            print("Error en checkbox_informe", error)



    @staticmethod
    def topFactura(titulo):
        """

        Muestra la cabecera de un informe de factura.

        Este método muestra la cabecera de un informe de factura, que incluye el logo de la empresa, el número de factura,
        la fecha, la información del cliente y el título del informe.

        :param titulo: El título del informe de factura.

        """
        try:
            registro = conexion.Conexion.codCli(var.ui.txtcifcli.text())
            ruta_logo = '.\\img\\logo.ico'
            logo = Image.open(ruta_logo)
            fecha = datetime.today()
            fecha = fecha.strftime('%d/%m/%Y')

            # Asegúrate de que el objeto 'logo' sea de tipo 'PngImageFile'
            if isinstance(logo, Image.Image):
                var.report.line(50, 800, 525, 800)
                var.report.setFont('Helvetica-Bold', size=14)
                var.report.drawString(55, 785, 'Car Teis')
                var.report.drawString(240, 670, titulo)
                var.report.line(50, 665, 525, 665)

                # Dibuja la imagen en el informe
                var.report.drawImage(ruta_logo, 480, 725, width=40, height=40)

                var.report.setFont('Helvetica-Bold', size=8)
                var.report.drawString(290, 785,
                                      'NÚMERO FACTURA: ' + var.ui.lblcodfacturacion.text() + '        Fecha: ' + fecha)
                var.report.drawString(290, 770, 'CLIENTE')

                var.report.setFont('Helvetica', size=9)
                var.report.drawString(55, 770, 'CIF: A12345678')
                var.report.drawString(55, 755, 'Avda. Galicia - 101')
                var.report.drawString(55, 740, 'Vigo - 36216 - España')
                var.report.drawString(55, 725, 'Teléfono: 986 132 456')
                var.report.drawString(55, 710, 'e-mail: cartesteisr@mail.com')
                var.report.setFont('Helvetica', size=8)
                var.report.drawString(290, 755, 'CIF: ' + str(registro[1]))
                var.report.drawString(290, 740, 'Razón Social: ' + str(registro[2]))
                var.report.drawString(290, 725, 'Dirección: ' + str(registro[3]))
                var.report.drawString(290, 710, 'Provincia: ' + str(registro[5]))
                var.report.drawString(290, 695, 'Teléfono: ' + str(registro[4]))
            else:
                print(f'Error: No se pudo cargar la imagen en {ruta_logo}')

        except Exception as error:
            print('Error en cabecera informe:', error)



    @staticmethod
    def reportfactura():
        """

        Genera un informe de factura.

        Este método genera un informe de factura en formato PDF. El informe incluye la información detallada de una factura
        seleccionada en la interfaz gráfica.

        """
        try:
            codigofactura = var.ui.lblcodfacturacion.text()
            if codigofactura == '':
                eventos.Eventos.error('Aviso', 'Elige una factura')
            else:
                nombre = codigofactura + '_factura.pdf'
                var.report = canvas.Canvas('informes/' + nombre)
                titulo = 'FACTURA'
                Informes.topFactura(titulo)
                Informes.footInforme(titulo)

                var.report.save()
                rootPath = '.\\informes'
                for file in os.listdir(rootPath):
                    if file.endswith(nombre):
                        os.startfile('%s\\%s' % (rootPath, file))

        except Exception as error:
            print('Error LISTADO conductores :', error)
