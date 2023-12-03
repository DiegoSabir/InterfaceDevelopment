import os.path

from datetime import datetime
from PyQt6 import QtWidgets, QtCore, QtGui

import locale
import sys
import drivers
import var
import zipfile
import shutil
import conexion
import xlwt
import xlrd

# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Eventos():


    """
    * Muestra la ventana de calendario (var.calendar) cuando se activa.
    * Controla cualquier error que ocurra al intentar mostrar el calendario.
    """
    @staticmethod
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print('error en abrir calendar: ', error)



    """
    * Muestra la ventana de "Acerca de" (var.dlgacerca) cuando se invoca.
    * Controla cualquier excepción que pueda surgir al intentar abrir la ventana.
    """
    @staticmethod
    def acercade():
        try:
            var.dlgacerca.show()
        except Exception as error:
            print('error abrir ventana acerca: ', error)



    """
    * Oculta la ventana "Acerca de" (var.dlgacerca) si está abierta.
    * Maneja cualquier error que pueda surgir al intentar cerrar la ventana.
    """
    @staticmethod
    def cerraracercade():
        try:
            var.dlgacerca.hide()
        except Exception as error:
            print('error abrir ventana acerca: ', error)



    """
    * Presenta un mensaje de confirmación antes de salir de la aplicación.
    * Si se selecciona "Sí" en la ventana de diálogo, el programa se cierra (sys.exit()).
    """
    def mostrarsalir(self=None):
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle('Confirmar Salida')
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
        mbox.setText('¿Está seguro de que desea salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            mbox.hide()



    """
    * Agrega widgets permanentes a la barra de estado (var.ui.statusbar) con información como la fecha 
      y la versión del programa.
    * Maneja errores si ocurren al intentar cargar la información en la barra de estado.
    """
    def cargastatusbar(self):
        try:
            fecha = datetime.now().strftime("%A  -  " + "%d/%m/%Y")
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)
            self.labelstatusversion = QtWidgets.QLabel("Version: " + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)

        except Exception as error:
            print('Error cargar el statusbar: ', error)



    """
    * Ajusta automáticamente el tamaño de las columnas en la tabla de conductores (var.ui.tabDrivers) para que el 
      contenido se muestre correctamente.
    * Controla los errores relacionados con el redimensionamiento de la tabla.
    """
    def resizeTabdrivers(self):
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print('error resize en tab drivers', error)



    """
    * Realizan formatos específicos en los campos de texto (txtApel, txtNome, txtSalario, txtMovil) de la interfaz.
    * Verifican y formatean los valores ingresados para cumplir con ciertos criterios (mayúsculas, 
      formatos de salario y números de teléfono).
    * Presentan mensajes de advertencia si se ingresan datos incorrectos o inválidos.
    * Manejan las excepciones que puedan surgir durante el proceso de formato de los campos de texto.
    """
    @staticmethod
    def formatCajatexto(self=None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNome.setText(var.ui.txtNome.text().title())
            salario = var.ui.txtSalario.text()
            valores = "1234567890."
            for n in salario:
                if n in valores:
                    pass
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                    msg.setText('Valor de Salario Incorrecto (00000000.00)')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtSalario.setText("")
                    break
            var.ui.txtSalario.setText(str(locale.currency(round(float(var.ui.txtSalario.text()),2),grouping=True)))

        except Exception as error:
            print('error poner letra capital cajas text', error)



    def formatCajamovil(self=None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNome.setText(var.ui.txtNome.text().title())
            movil = var.ui.txtMovil.text()
            valorm = "1234567890"
            for n in movil:
                if n in valorm and len(movil) == 9:
                    pass

                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                    msg.setText('Introduzca un numero correcto')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtMovil.setText("")
                    break

        except Exception as error:
            print('error poner movil', error)



    """
    * Este método se encarga de generar una copia de seguridad de la base de datos.
    * Utiliza la fecha y hora actuales para crear un nombre único para el archivo de respaldo.
    * Presenta un diálogo para seleccionar la ubicación y el nombre del archivo de respaldo.
    * Especifica el contenido del archivo ZIP con la base de datos y lo mueve a la ubicación seleccionada.
    * Muestra mensajes informativos o de advertencia en caso de éxito o fracaso respectivamente.
    * Maneja errores en el proceso de creación de la copia de seguridad, mostrando mensajes con detalles del error.
    """
    def crearbackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = str(fecha) + '_backup.zip'
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia Seguridad', copia, '.zip')

            if var.dlgabrir.accept and filename:
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText("Copia de seguridad creada")
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("Error al crear la copia de seguridad", error)
            msg.exec()


    """
    * Este método se encarga de restaurar una copia de seguridad previamente creada.
    * Abre un diálogo para seleccionar el archivo de respaldo ZIP que se va a restaurar.
    * Extrae los contenidos del archivo ZIP seleccionado y lo restaura en la ubicación actual.
    * Muestra un mensaje informativo cuando la restauración es exitosa.
    * Controla y muestra mensajes de advertencia si hay algún error durante el proceso de restauración.
    """
    def restaurarbackup(self):
        try:
            filename = var.dlgabrir.getOpenFileName(None,'Restaurar Copia de Seguridad',
                                                    '','*.zip;;All Files(*)')
            file = filename[0]
            if file:
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText("Copia de seguridad restaurada")
                msg.exec()
                conexion.Conexion.mostrardrivers(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("Error al restaurar la copia de seguridad", error)
            msg.exec()



    """
    * Crea un archivo de hoja de cálculo en formato XLS que contiene información específica de los conductores.
    * Establece un nombre único para el archivo basado en la fecha y hora actuales.
    * Presenta un diálogo para elegir la ubicación y el nombre del archivo de exportación.
    * Crea y llena una hoja de cálculo con la información de los conductores.
    * Muestra un mensaje informativo al usuario si la exportación se completa exitosamente.
    * Maneja errores que puedan surgir durante el proceso de exportación, mostrando mensajes detallados sobre el error.
    """
    def exportardatosxls(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = (str(fecha) + '_Datos.xls')
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar Datos en XLS', file, '.xls')
            if file:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Conductores')
                sheet1.write(0, 0, 'ID')
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Apellidos')
                sheet1.write(0, 4, 'Nombre')
                sheet1.write(0, 5, 'Direccion')
                sheet1.write(0, 6, 'Provincia')
                sheet1.write(0, 7, 'Municipio')
                sheet1.write(0, 8, 'Movil')
                sheet1.write(0, 9, 'Salario')
                sheet1.write(0, 10, 'Carnet')

                registros = conexion.Conexion.selectDriverstodos()
                for fila, registro in enumerate(registros, 1):
                    for i, valor in enumerate(registro[:-1]):
                        sheet1.write(fila, i, str(valor))
                wb.save(directorio)

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Exportación de datos realizada')
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("Error al exportar datos a hoja de calculo", error)
            msg.exec()



    """
    * Permite importar datos desde un archivo de hoja de cálculo en formato XLS a la base de datos.
    * Abre un diálogo para seleccionar el archivo XLS que contiene los datos a importar.
    * Lee y procesa los datos del archivo seleccionado y los inserta en la base de datos.
    * Realiza validaciones específicas para asegurar la integridad de los datos importados.
    * Muestra mensajes informativos o de advertencia dependiendo de si la importación es exitosa o si 
      se encuentran datos incorrectos.
    * Controla los errores que puedan surgir durante el proceso de importación, informando al usuario sobre el problema.
    """
    def importardatosxls(self):
        try:
            estado = 0
            drivers.Drivers.limpiapanel(self)
            filename, _ = var.dlgabrir.getOpenFileName(None, 'Importar datos',
                                                    '', '*.xls;;All Files (*)')
            if filename:
                file = filename
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                for i in range(filas):
                    if i == 0:
                        pass

                    else:
                        new = []
                        for j in range(columnas):
                            if j == 1:
                                dato = xlrd.xldate_as_datetime(datos.cell_value(i, j), documento.datemode)
                                dato = dato.strftime('%d/%m/%Y')
                                new.append(str(dato))

                            else:
                                new.append(str(datos.cell_value(i, j)))

                        if drivers.Drivers.validarDNI(str(new[0])):
                            conexion.Conexion.guardardri(new)

                        elif estado == 0:
                            estado = 1
                            msg = QtWidgets.QMessageBox()
                            msg.setModal(True)
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                            msg.setText('Hay DNI incorrectos')
                            msg.exec()

                var.ui.lblValidardni.setText('')
                var.ui.txtDni.setText('')
                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importación de Datos Realizada')
                var.ui.lblValidardni.setText('')
                msg.exec()
            conexion.Conexion.selectDrivers(1)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error', error)
            msg.exec()
