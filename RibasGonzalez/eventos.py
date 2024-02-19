import locale
import os.path
import xlrd
import clientes
import conexion

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

import sys, zipfile, shutil

from auxiliar import *
from datetime import  datetime

import xlwt
import drivers
import var

class Eventos():
    @staticmethod
    def salir(self):
        """


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


        :param self:
        :type self:

        """
        try:
            var.acercaDe.hide()

        except Exception as error:
            print(error , " en modulo eventos")



    def abrirAcercaDe(self):
        """



        """
        try:
            var.acercaDe.show()

        except Exception as error:
            print(error , " en modulo eventos")



    @staticmethod
    def abrirSalir(self):
        """

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


        :param self:
        :type self:

        """
        try:
            pass

        except Exception as error:
            print(error ," en abrir acercade")



    @staticmethod
    def selEstado(self):
        """


        :param self:
        :type self:

        """
        conexion.Conexion.mostrardriver()



    @staticmethod
    def resizeTabdrivers(self):
        """


        :param self:
        :type self:

        """
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(5):
                if i==0 or i==4 or i==3:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i==1 or i==2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print(error," en resizetabdrivers")



    @staticmethod
    def formatCajaTexto(self = None):
        """


        :param self:
        :type self:

        """
        try:
            var.ui.txtapellidos.setText(var.ui.txtapellidos.text().title())
            var.ui.txtnombre.setText(var.ui.txtnombre.text().title())

        except Exception as error:
            print(error," en letracapital")



    @staticmethod
    def crearBackup():
        """



        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = str(fecha)+'_backup.zip'
            directorio, filename = var.dlgabrir.getSaveFileName(None,'Guardar copia de seguridad',copia,'.zip')
            if var.dlgabrir.accept and filename !='':
                fichZip=zipfile.ZipFile(copia,'w')
                fichZip.write(var.bbdd, os.path.basename(var.bbdd),zipfile.ZIP_DEFLATED)
                fichZip.close()
                shutil.move(str(copia),str(directorio))
                eventos.Eventos.mensaje("Aviso", "Copia de seguridad creada")

        except Exception as error:
            eventos.Eventos.error("Aviso", "Error al crear backup")



    def  restaurarBackup(self):
        """



        """
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar copia de seguridad', '', '*.zip;;All Files(*)')
            file = filename[0]
            if filename[0]:
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                conexion.Conexion.mostrardriver()
                eventos.Eventos.mensaje("Aviso", "Copia de seguridad restaurada")

        except Exception as error:
            eventos.Eventos.error("Aviso", "Error al restaurar el backup")



    def exportardatosxls(self):
        """



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



        """
        try:
            dni = var.ui.txtDNI.text()
            dni = dni.upper()
            drivers.Drivers.validarDNI(dni)

        except Exception as error:
            print(error)



    def importarDatosExcel(self):
        """



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
                            mbox.setText("Importacion exitosa,clientes no insertados "+str(numFallo))
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


        :param self:
        :type self:

        """
        conexion.Conexion.mostrarClientes()



    @staticmethod
    def abrirCalendarBajacli():
        """



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



        """
        try:
            var.Altafact.show()

        except Exception as error:
            print(error, "en modulo eneventos")



    def error(title, text):
        """


        :param text:
        :type text:

        """
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle(title)
        mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        mbox.setText(text)
        mbox.exec()



    def mensaje(title, text):
        """


        :param text:
        :type text:

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



        """
        try:
            header = var.ui.tabViajes.horizontalHeader()
            for i in range(5):
                if i==0 or i==3 or i==6:
                    header.setSectionResizeMode(i,QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i==1 or i==2 :
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print(error," en resizetabdrivers")
