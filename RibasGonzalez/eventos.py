import locale
import os.path
import xlrd
import clientes
import conexion

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

import sys, zipfile, shutil

from auxiliar import *
from datetime import datetime

import xlwt
import drivers
import var

class Eventos():
    @staticmethod
    def salir(self):
        """

        Cierra la aplicación.

        :param self:
        :type self:

        """
        try:
            sys.exit(0)

        except Exception as error:
            print(error, "en modulo enventos.")



    @staticmethod
    def abrirCalendar(self):
        """

        Abre el widget del calendario.

        Muestra el widget del calendario en la interfaz.

        :param self:
        :type self:

        """
        try:
            var.calendar.show()

        except Exception as error:
            print(error, "en modulo eneventos")



    @staticmethod
    def cerrarAcercaDe(self):
        """

        Cierra la ventana Acerca De.

        Oculta la ventana Acerca De en la interfaz.

        :param self:
        :type self:

        """
        try:
            var.acercaDe.hide()

        except Exception as error:
            print(error , " en modulo eventos")



    def abrirAcercaDe(self):
        """

        Abre la ventana Acerca De.

        Muestra la ventana Acerca De en la interfaz.

        """
        try:
            var.acercaDe.show()

        except Exception as error:
            print(error , " en modulo eventos")



    @staticmethod
    def abrirSalir(self):
        """

        Abre la ventana de confirmación para salir.

        Muestra la ventana de confirmación para salir en la interfaz.

        :param self:
        :type self:

        """
        try:
            var.salir.show()

        except Exception as error:
            print(error , " en modulo eventos")



    @staticmethod
    def cerrarSalir(self):
        """

        Cierra la ventana de confirmación para salir.

        Oculta la ventana de confirmación para salir en la interfaz.

        :param self:
        :type self:

        """
        try:
            var.salir.hide()

        except Exception as error:
            print(error , " en modulo eventos")



    @staticmethod
    def acercade(self):
        """

        Placeholder para la función Acerca De.

        No se implementa actualmente.

        :param self:
        :type self:

        """
        try:
            pass

        except Exception as error:
            print(error, " en abrir acercade")



    @staticmethod
    def selEstado(self):
        """

        Muestra los drivers en la interfaz.

        Llama a la función mostrardriver de la clase Conexion para mostrar los drivers en la interfaz.

        :param self:
        :type self:

        """
        conexion.Conexion.mostrardriver()



    @staticmethod
    def resizeTabdrivers(self):
        """

        Ajusta el tamaño de las columnas en la tabla de drivers.

        Ajusta las columnas para que se redimensionen correctamente en la tabla de drivers.

        :param self:
        :type self:

        """
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print(error, " en resizetabdrivers")



    @staticmethod
    def formatCajaTexto(self=None):
        """

        Formatea el texto en las cajas de texto de apellidos y nombre.

        Convierte el texto ingresado a formato de letra capital.

        :param self:
        :type self:

        """
        try:
            var.ui.txtapellidos.setText(var.ui.txtapellidos.text().title())
            var.ui.txtnombre.setText(var.ui.txtnombre.text().title())

        except Exception as error:
            print(error, " en letracapital")



    @staticmethod
    def crearBackup():
        """

        Crea una copia de seguridad de la base de datos.

        Crea un archivo zip con una copia de seguridad de la base de datos y muestra un mensaje de éxito.

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = str(fecha)+'_backup.zip'
            directorio, filename = var.dlgabrir.getSaveFileName(None,'Guardar copia de seguridad', copia, '.zip')
            if var.dlgabrir.accept and filename != '':
                fichZip = zipfile.ZipFile(copia,'w')
                fichZip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichZip.close()
                shutil.move(str(copia),str(directorio))
                eventos.Eventos.mensaje("Aviso", "Copia de seguridad creada")

        except Exception as error:
            eventos.Eventos.error("Aviso", "Error al crear backup")



    def restaurarBackup(self):
        """

        Restaura una copia de seguridad de la base de datos.

        Permite al usuario seleccionar un archivo zip y restaura la base de datos desde ese archivo.
        Muestra un mensaje de éxito o error.

        """
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar copia de seguridad', '', '*.zip;;All Files(*)')
            file = filename[0]
            if filename[0]:
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                conexion.Conexion.mostrardriver()
                conexion.Conexion.mostrarClientes()
                conexion.Conexion.cargarfacturas()
                conexion.Conexion.cargarconductor()
                eventos.Eventos.mensaje("Aviso", "Copia de seguridad restaurada")

        except Exception as error:
            eventos.Eventos.error("Aviso", "Error al restaurar el backup")



    def exportardatosxls(self):
        """

        Exporta los datos de conductores a un archivo xls.

        Crea un archivo xls con los datos de conductores y muestra un mensaje de éxito o error.

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = str(fecha) + '_Datos.xls'
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar Datos en xls', file, '.xls')
            if var.dlgabrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Conductores')
                sheet1.write(0, 0, 'ID')
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Nombre')
                sheet1.write(0, 4, 'Apellidos')
                sheet1.write(0, 5, 'Dirección')
                sheet1.write(0, 6, 'Provincia')
                sheet1.write(0, 7, 'Municipio')
                sheet1.write(0, 8, 'Móvil')
                sheet1.write(0, 9, 'Salario')
                sheet1.write(0, 10, 'Carnet')
                registros = conexion.Conexion.selectDriverstodos()
                for fila, registro in enumerate(registros, 1):
                    for i, valor in enumerate(registro[:-1]):
                        sheet1.write(fila, i, str(valor))
                wb.save(directorio)
                eventos.Eventos.mensaje("Aviso", "Exportacion de datos completada exitosamente")

        except Exception as error:
            eventos.Eventos.error("Aviso", "Error al exportar datos")



    def validarDNI(self=None):
        """

        Valida el formato de un DNI y muestra un ícono de verificación o error.

        :param dni: Número de DNI a validar.
        :type dni: str

        """
        try:
            dni = var.ui.txtDNI.text()
            dni = dni.upper()
            drivers.Drivers.validarDNI(dni)

        except Exception as error:
            print(error)



    def importarDatosExcel(self):
        """

        Importa datos desde un archivo xls a la base de datos.

        Permite al usuario seleccionar un archivo xls y lo importa a la base de datos.
        Muestra un mensaje de éxito o error.

        """
        try:
            filename = var.dlgabrir.getOpenFileName(None, "Importar datos", "", "*.xls;;All File(*)")
            drivers.Drivers.limpiarPanel(self)
            if filename[0]:
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                numFallo = 0
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            if j != 0:
                                new.append(str(datos.cell_value(i, j)))
                        if drivers.Drivers.validarDNI(str(new[0])):
                            conexion.Conexion.guardardri(new)
                        else:
                            numFallo += 1
                        if i == filas -1:
                            mbox = QtWidgets.QMessageBox()
                            mbox.setWindowTitle('Aviso')
                            mbox.setModal(True)
                            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                            mbox.setText("Importacion exitosa,clientes no insertados " + str(numFallo))
                            mbox.exec()
                conexion.Conexion.mostrardriver()

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setModal(True)
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Error al importar datos en hoja de cálculo')
            mbox.exec()



    @staticmethod
    def abrirCalendarBaja():
        """

        Abre una ventana de confirmación para dar de baja a un conductor.

        Muestra una ventana de confirmación para dar de baja a un conductor.

        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Dar Baja")
            mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("¿Desea darlo de baja?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                if var.ui.lblcodbd.text() != "":
                    var.Baja.show()
                else:
                    eventos.Eventos.error("Aviso", "Elige conductor")
            else:
                eventos.Eventos.error("Aviso", "Conductor no dado de baja")

        except Exception as error:
            print(error," en modulo eventos")



    @staticmethod
    def resizeTabclientes(self):
        """

        Ajusta el tamaño de las columnas en la tabla de clientes.

        :param self:
        :type self:

        """
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(3):
                if i == 0 or i == 3 or i == 4:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print(error, " en resizetabdrivers")



    def validarDNI2(self=None):
        """

        Valida el formato de un DNI y muestra un ícono de verificación o error.

        """
        try:
            dni = var.ui.txtDNI2.text()
            dni = dni.upper()
            clientes.Clientes.validarDNI2(dni)

        except Exception as error:
            print(error)



    @staticmethod
    def selEstado2(self):
        """

        Muestra los clientes en la interfaz.

        :param self:
        :type self:

        """
        conexion.Conexion.mostrarClientes()



    @staticmethod
    def abrirCalendarBajacli():
        """

        Abre una ventana de confirmación para dar de baja a un cliente.

        Muestra una ventana de confirmación para dar de baja a un cliente.

        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Dar Baja")
            mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("¿Desea darlo de baja?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                if var.ui.lblcodbd2.text() != "":
                    var.Bajacli.show()
                else:
                    eventos.Eventos.error("Aviso", "Elige un cliente")
            else:
                eventos.Eventos.error("Aviso", "Cliente no se ha dado de baja")

        except Exception as error:
            print(error, " en modulo eventos abrircalendarbajacli")



    def exportardatosclientesxls(self):
        """

        Exporta los datos de clientes a un archivo xls.

        Crea un archivo xls con los datos de clientes y muestra un mensaje de éxito o error.

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = str(fecha) + '_Datosclientes.xls'
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar Datos en xls', file, '.xls')
            if var.dlgabrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Clientes')
                sheet1.write(0, 0, 'ID')
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Razon Social')
                sheet1.write(0, 3, 'Dirección')
                sheet1.write(0, 4, 'Provincia')
                sheet1.write(0, 5, 'Municipio')
                sheet1.write(0, 6, 'Móvil')
                registros = conexion.Conexion.selectClientesstodos()
                for fila, registro in enumerate(registros, 1):
                    for i, valor in enumerate(registro[:-1]):
                        sheet1.write(fila, i, str(valor))
                wb.save(directorio)
                eventos.Eventos.mensaje("Aviso", "Exportacion completada exitosamente")

        except Exception as error:
            eventos.Eventos.error("Aviso", "Error al exportar datos")



    def importarDatosclientesExcel(self):
        """

        Importa datos desde un archivo xls a la base de datos de clientes.

        Permite al usuario seleccionar un archivo xls y lo importa a la base de datos de clientes.
        Muestra un mensaje de éxito o error.

        """
        try:
            filename = var.dlgabrir.getOpenFileName(None, "Importar datos", "", "*.xls;;All File(*)")
            clientes.Clientes.limpiarPanel2()
            if filename[0]:
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                numFallo = 0
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            if j != 0:
                                new.append(str(datos.cell_value(i, j)))
                        if clientes.Clientes.validarDNI2(str(new[0])):
                            conexion.Conexion.guardarcli(new)
                        else:
                            numFallo += 1
                        if i == filas -1:
                            mbox = QtWidgets.QMessageBox()
                            mbox.setWindowTitle('Aviso')
                            mbox.setModal(True)
                            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                            mbox.setText("Importacion exitosa,clientes no insertados "+str(numFallo))
                            mbox.exec()

                conexion.Conexion.mostrarClientes()

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setModal(True)
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Error al importar datos en hoja de cálculo')
            mbox.exec()



    def abrirCalendarfact(self):
        """

        Abre la ventana para dar de alta una factura.

        Muestra la ventana para dar de alta una factura.

        """
        try:
            var.Altafact.show()

        except Exception as error:
            print(error, "en modulo eneventos")



    def error(title, text):
        """

        Muestra un mensaje de error.

        :param title: Título del mensaje.
        :type title: str
        :param text: Texto del mensaje.
        :type text: str

        """
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle(title)
        mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        mbox.setText(text)
        mbox.exec()



    def mensaje(title, text):
        """

        Muestra un mensaje informativo.

        :param title: Título del mensaje.
        :type title: str
        :param text: Texto del mensaje.
        :type text: str

        """
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle(title)
        mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        mbox.setText(text)
        mbox.exec()



    @staticmethod
    def resizeTabfacturas():
        """

        Ajusta el tamaño de las columnas en la tabla de facturas.

        Ajusta las columnas para que se redimensionen correctamente en la tabla de facturas.

        """
        try:
            header = var.ui.tablaFacturas.horizontalHeader()
            for i in range(3):
                if i == 0:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print(error, " en resize fact")



    @staticmethod
    def resizeTabViajes():
        """

        Ajusta el tamaño de las columnas en la tabla de viajes.

        Ajusta las columnas para que se redimensionen correctamente en la tabla de viajes.

        """
        try:
            header = var.ui.tabViajes.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 3 or i == 6:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print(error, " en resizetabdrivers")
