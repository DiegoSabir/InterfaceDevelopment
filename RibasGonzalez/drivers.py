from datetime import datetime

import var
import locale, conexion

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets,QtCore, QtGui

import eventos

class Drivers():
    def limpiarPanel(self):
        """

        Limpia los campos del panel de control de conductores.

        Este método limpia los campos de entrada de texto, los campos de verificación de licencia
        y los campos de lista desplegable de provincia y municipio en el panel de control de conductores.

        """
        try:
            listawidgets=[var.ui.lblcodbd, var.ui.txtDNI, var.ui.txtfecha, var.ui.txtapellidos, var.ui.txtnombre,
                          var.ui.txtdir, var.ui.txtmovil, var.ui.txtsalario, var.ui.lblValidarDNI ]
            for i in listawidgets:
                i.setText(None)
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                i.setChecked(False)
            var.ui.cmbProv.setCurrentText('')
            var.ui.cmbMuni.setCurrentText('')

        except Exception as error:
            print(str(error) + " en validar drivers")



    def cargaFecha(qDate):
        """

        Carga la fecha seleccionada en el campo de texto de fecha.

        Este método toma la fecha seleccionada del calendario y la formatea en el formato 'dd/mm/yyyy',
        luego la establece como texto en el campo de texto de fecha y oculta el calendario.

        :param qDate: La fecha seleccionada del calendario.

        """
        try:
            data=('{:02d}/{:02d}/{:4d}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtfecha.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print(str(error) + " en validar drivers")



    def validarDNI(dni):
        """

        Valida un número de DNI español.

        Este método toma un número de DNI como entrada y verifica si es válido según el algoritmo utilizado en España.
        Muestra una marca de verificación si el DNI es válido y una marca de error si no lo es.

        :param dni: El número de DNI a validar.

        :return: True si el DNI es válido, False si no lo es.

        :rtype: bool

        """
        try:
            var.ui.txtDNI.setText(dni)  # Corrección aquí
            tabla = "TRWAGMYFPDXBNJZSKVHLCKE"
            digExt = "XYZ"
            reempDigExt = {"X": '0', "Y": '1', "Z": '2'}
            numeros = "1234567890"
            imgCorrecto = QPixmap('img/tickcirclehd_106142.ico')
            imgIncorrecto = QPixmap('img/crosscircleregular_106260.ico')

            if len(dni) == 9:
                digControl = dni[8]
                dni = dni[:8]
                if dni[0] in digExt:
                    dni = dni.replace(dni[0], reempDigExt[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == digControl:
                    var.ui.lblValidarDNI.setPixmap(imgCorrecto)
                    var.ui.txtfecha.setFocus()
                    return True
                else:
                    var.ui.lblValidarDNI.setPixmap(imgIncorrecto)
                    var.ui.txtDNI.setText(None)
                    var.ui.txtDNI.setFocus()
                    return False
            else:
                var.ui.lblValidarDNI.setPixmap(imgIncorrecto)
                var.ui.txtDNI.setText(None)
                var.ui.txtDNI.setFocus()
                return False

        except Exception as error:
            print(str(error) + " en validar drivers")



    def altaDriver(self):
        """

        Da de alta un nuevo conductor en la base de datos o revierte la baja de un conductor existente.

        Este método verifica si el DNI del conductor ya existe en la base de datos. Si el conductor ya existe y está dado de baja,
        ofrece la opción de darlo de alta nuevamente. Si el conductor no existe o está dado de alta, verifica que se ingresen todos
        los datos obligatorios y luego intenta guardar el nuevo conductor en la base de datos. Muestra un mensaje de éxito si el
        conductor se agrega correctamente, o un mensaje de error si no se puede agregar.

        """
        try:
            dni = var.ui.txtDNI.text()
            if conexion.Conexion.verificarDri(dni):
                conexion.Conexion.volverDarAlta(dni)

                Drivers.limpiarPanel(self)
                conexion.Conexion.mostrardriver()
            else:
                if not all([var.ui.txtDNI.text(), var.ui.txtnombre.text(), var.ui.txtapellidos.text(),
                            var.ui.txtmovil.text()]):
                    eventos.Eventos.error("Aviso", "Faltan datos obligatorios")
                    return
                driver = [
                    var.ui.txtDNI, var.ui.txtfecha, var.ui.txtapellidos, var.ui.txtnombre,
                    var.ui.txtdir, var.ui.txtmovil, var.ui.txtsalario
                ]
                newDriver = []
                for i in driver:
                    newDriver.append(i.text().title())

                prov = var.ui.cmbProv.currentText()
                newDriver.insert(5, prov)
                muni = var.ui.cmbMuni.currentText()
                newDriver.insert(6, muni)

                licencias = []
                chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
                for i in chklicencia:
                    if i.isChecked():
                        licencias.append(i.text())
                newDriver.append('-'.join(licencias))
                valor=conexion.Conexion.guardardri(newDriver)
                if valor==True:
                    eventos.Eventos.mensaje("Aviso", "El conductor fue añadido con exito")
                    conexion.Conexion.mostrardriver()
                    conexion.Conexion.cargarconductor()
                elif valor == False:
                    eventos.Eventos.error("Aviso", "No se ha podido dar de alta")

        except Exception as error:
            print(str(error) + " en altadriver drivers")



    def validarMovil(self=None):
        """

        Valida el número de teléfono móvil ingresado.

        Este método verifica si el número de teléfono móvil ingresado es una cadena de 9 números enteros. Si no cumple con esta
        condición, muestra un mensaje de error y limpia el campo de texto del teléfono móvil.

        """
        try:
            movil = var.ui.txtmovil.text()
            numeros = "1234567890"
            var.ui.txtmovil.setText(movil)  # Corrección aquí
            if len(movil) == 9:
                digControl = movil[:9]
                if len(movil) != len([n for n in movil if n in numeros])== digControl:
                    raise Exception
            else:
                raise Exception

        except Exception as error:
            eventos.Eventos.error("Aviso", "El telefono debe ser una cadena de 9 numeros enteros")
            var.ui.txtmovil.setText("")



    def validarSalario(self=None):
        """

        Valida el salario ingresado.

        Este método verifica si el salario ingresado es una cadena que contiene solo dígitos numéricos.
        Si cumple con esta condición, formatea el salario como una cantidad monetaria y lo muestra en el campo de texto del salario.
        Si no cumple con esta condición, muestra un mensaje de error y limpia el campo de texto del salario.

        """
        try:
            sal = var.ui.txtmovil.text()
            numeros = "1234567890"
            var.ui.txtmovil.setText(sal)# Corrección aquí
            if len(sal) == len([n for n in sal if n in numeros]):
                var.ui.txtsalario.setText(str(locale.currency(float(var.ui.txtsalario.text()),grouping=True)))
            else:
                raise Exception

        except Exception as error:
            eventos.Eventos.error("Aviso", "Valor de Salario Incorrecto (00000000.00)")
            var.ui.txtsalario.setText("")



    def cargarTabladri(registros):
        """

        Carga los registros de conductores en la tabla de conductores.

        Este método toma una lista de registros de conductores y los muestra en la tabla de conductores de la interfaz gráfica.

        :param registros: La lista de registros de conductores.

        """
        try:
            index = 0

            for registro in registros:
                var.ui.tabDrivers.setRowCount(index + 1)
                var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabDrivers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print(str(error) + " en cargartabladri drivers")



    def cargarDriver(self):
        """

        Carga los detalles del conductor seleccionado en la tabla de conductores.

        Este método se utiliza para cargar los detalles del conductor seleccionado en la tabla de conductores de la interfaz gráfica.
        Limpia el panel de detalles del conductor, obtiene la fila seleccionada de la tabla, busca el registro del conductor correspondiente,
        muestra los detalles en el panel y luego actualiza la tabla de conductores.

        """
        try:
            Drivers.limpiarPanel(self)
            row = var.ui.tabDrivers.selectedItems()
            fila =[dato.text() for dato in row]
            registro = conexion.Conexion.oneDriver(fila[0])
            Drivers.auxiliar(registro)
            conexion.Conexion.mostrardriver()
            Drivers.colorearFila(registro[0])

        except Exception as error:
            print(str(error) + " en cargarDriver drivers")



    def auxiliar(registro):
        """

        Llena el panel de detalles del conductor con la información del conductor seleccionado.

        Este método se utiliza para llenar el panel de detalles del conductor con la información del conductor seleccionado en la tabla de conductores.
        Recibe como argumento el registro del conductor seleccionado y actualiza los campos correspondientes en la interfaz gráfica.

        :param registro: El registro del conductor seleccionado.

        """
        try:
            datos=[var.ui.lblcodbd, var.ui.txtDNI, var.ui.txtfecha, var.ui.txtapellidos, var.ui.txtnombre,
                   var.ui.txtdir, var.ui.cmbProv, var.ui.cmbMuni, var.ui.txtmovil, var.ui.txtsalario]
            for i,dato in enumerate(datos):
                if i == 6 or i == 7 :
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            if 'A' in registro [10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registro [10]:
                var.ui.chkA.setChecked(True)
            if 'C' in registro [10]:
                var.ui.chkA.setChecked(True)
            if 'D' in registro [10]:
                var.ui.chkA.setChecked(True)

        except Exception as error:
            eventos.Eventos.error("Aviso", "No existe en la base de datos")



    def buscaDri(self):
        """
        Busca un conductor por su DNI y muestra sus detalles en el panel correspondiente.

        Este método busca un conductor en la base de datos utilizando el DNI proporcionado en el campo correspondiente.
        Si se encuentra un conductor con el DNI proporcionado, muestra sus detalles en el panel de detalles del conductor.
        Además, marca el botón de opción "Todos" como seleccionado en la tabla de conductores y colorea la fila del conductor encontrado.

        """
        try:
            dni = var.ui.txtDNI.text()
            registro = conexion.Conexion.codDri(dni)
            Drivers.auxiliar(registro)
            codigo = var.ui.lblcodbd.text()
            var.ui.rbtTodos.setChecked(True)
            conexion.Conexion.mostrardriver()
            Drivers.colorearFila(codigo)

        except Exception as error:
            print(error, "en busca de buscadri")



    def colorearFila(codigo):
        """

        Colorea la fila correspondiente a un conductor en la tabla de conductores.

        Este método recorre todas las filas de la tabla de conductores y compara el código proporcionado con el código de cada fila.
        Si encuentra una coincidencia, colorea toda la fila en amarillo claro para resaltarla visualmente.

        :param codigo: El código del conductor que se desea resaltar.

        """
        for fila in range(var.ui.tabDrivers.rowCount()):
            if var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                for columna in range(var.ui.tabDrivers.columnCount()):
                    item = var.ui.tabDrivers.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))



    def modifDri(self):
        """

        """
        try:
            driver=[var.ui.lblcodbd,var.ui.txtDNI, var.ui.txtfecha, var.ui.txtapellidos, var.ui.txtnombre,
                    var.ui.txtdir, var.ui.txtmovil, var.ui.txtsalario]
            modifDriver=[]
            for i in driver:
                modifDriver.append(i.text().title())
            prov = var.ui.cmbProv.currentText()
            modifDriver.insert(6,prov)
            muni = var.ui.cmbMuni.currentText()
            modifDriver.insert(7,muni)
            licencias=[]
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())
            modifDriver.append('-'.join(licencias))
            conexion.Conexion.modifDriver(modifDriver)

        except Exception as error:
            print(error, " en modifdri")



    def borraDri(qDate):
        """

        Modifica los datos de un conductor en la base de datos.

        Este método recoge los datos ingresados en los campos de la interfaz gráfica correspondientes a un conductor y los envía a la base de datos
        para actualizar la información del conductor. También gestiona las licencias de conducción seleccionadas.

        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.Baja.hide()
            dni = var.ui.txtDNI.text()
            conexion.Conexion.borrarDri(dni, str(data))
            conexion.Conexion.mostrardriver()
            conexion.Conexion.cargarconductor()

        except Exception as error:
            eventos.Eventos.error("Aviso", "El conductor no existe o no se puede borrar")
