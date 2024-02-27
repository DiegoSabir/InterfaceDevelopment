from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt

import conexion
import var
import eventos

class Clientes():
    def limpiarPanel2(self=None):
        """

        Limpia los campos del panel de clientes en la interfaz de usuario.

        Este método se utiliza para limpiar los campos del panel de clientes en la interfaz de usuario.
        Recorre una lista de widgets que forman parte del panel de clientes y establece el texto de cada
        uno de ellos en nulo. Además, restablece los valores seleccionados en los combos de provincias y
        municipios.

        """
        try:
            listawidgets = [var.ui.lblcodbd2, var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2, var.ui.txtmovil2, var.ui.lblValidarDNI2]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbProv2.setCurrentText('')
            var.ui.cmbMuni2.setCurrentText('')

        except Exception as error:
            print(str(error) + " en validar drivers")



    def buscarCliente(self):
        """

        Busca un cliente por su DNI en la base de datos y carga sus datos en la interfaz de usuario.

        Este método se activa al hacer clic en el botón de buscar cliente. Obtiene el DNI del campo de texto
        correspondiente en la interfaz de usuario, busca el cliente en la base de datos utilizando el método
        'codCli' de la clase 'Conexion', carga los datos del cliente encontrado en la interfaz de usuario
        utilizando el método 'auxiliar', establece el botón de radio 'Todos' como seleccionado, actualiza la
        tabla de clientes y colorea la fila correspondiente en la tabla.

        """
        try:
            dni = var.ui.txtDNI2.text()
            registro = conexion.Conexion.codCli(dni)
            Clientes.auxiliar(registro)
            codigo = var.ui.lblcodbd2.text()
            var.ui.rbtTodos2.setChecked(True)
            conexion.Conexion.mostrarClientes()
            Clientes.colorearFila(codigo)

        except Exception as error:
            print(str(error) + " en cargarcliente clientes")



    def cargarCliente(self):
        """

        Carga los datos de un cliente seleccionado en la tabla de clientes en la interfaz de usuario.

        Este método se activa cuando se selecciona una fila en la tabla de clientes. Limpia el panel de
        cliente en la interfaz de usuario, obtiene los datos del cliente seleccionado, los muestra en
        los campos correspondientes de la interfaz de usuario utilizando el método 'auxiliar', actualiza
        la tabla de clientes y colorea la fila correspondiente en la tabla.

        """
        try:
            Clientes.limpiarPanel2()
            row = var.ui.tabClientes.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneCliente(fila[0])
            Clientes.auxiliar(registro)
            conexion.Conexion.mostrarClientes()
            Clientes.colorearFila(registro[0])

        except Exception as error:
            print(str(error) + " en cargar clientes clientes")



    def auxiliar(registro):
        """

        Llena los campos de la interfaz de usuario con los datos del registro proporcionado.

        Recibe un registro que contiene los datos de un cliente y actualiza los campos correspondientes
        en la interfaz de usuario con estos datos. Los campos actualizados incluyen el código, DNI,
        nombre, dirección, teléfono, provincia y municipio del cliente.

        :param registro: Lista que contiene los datos del cliente.

        """
        try:
            datos = [var.ui.lblcodbd2, var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2, var.ui.txtmovil2, var.ui.cmbProv2, var.ui.cmbMuni2]
            for i, dato in enumerate(datos):
                if i == 5 or i == 6:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))

        except Exception as error:
            eventos.Eventos.error("Aviso", "No existe en la base de datos")



    def colorearFila(codigo):
        """

        Colorea la fila correspondiente al cliente con el código especificado en la tabla de clientes.

        Recibe el código del cliente y busca la fila correspondiente en la tabla 'tabClientes' de la interfaz.
        Si encuentra la fila, colorea todos los elementos de la fila con un color amarillo claro.

        :param codigo: Código del cliente para identificar la fila que se debe colorear.

        """
        try:
            for fila in range(var.ui.tabClientes.rowCount()):
                if var.ui.tabClientes.item(fila, 0).text() == str(codigo):
                    for columna in range(var.ui.tabClientes.columnCount()):
                        item = var.ui.tabClientes.item(fila, columna)
                        if item is not None:
                            item.setBackground(QtGui.QColor(255, 241, 150))

        except Exception as error:
            print("error en colorearFila", error)



    def cargarTablaClientes(registros):
        """

        Carga los registros de clientes en la tabla de la interfaz gráfica.

        Recibe una lista de registros de clientes y los muestra en la tabla 'tabClientes' de la interfaz.
        Para cada registro en la lista, crea una nueva fila en la tabla y muestra los datos en las columnas correspondientes.

        :param registros: Lista de registros de clientes a mostrar en la tabla.

        """
        try:
            index = 0
            for registro in registros:
                var.ui.tabClientes.setRowCount(index + 1)
                var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("error en cargarTablaclientes", error)



    def validarDNI2(dni):
        """

        Valida un número de documento de identidad (DNI) introducido en el campo correspondiente de la interfaz gráfica.

        Extrae el número de DNI ingresado en el campo de texto 'txtDNI2' de la interfaz.
        Verifica que el DNI tenga exactamente 9 caracteres y que cumpla con el algoritmo de validación estándar español.
        Si el DNI es válido, muestra una marca de verificación en un QLabel asociado y devuelve True.
        Si el DNI no es válido, muestra una marca de error en el QLabel asociado, limpia el campo de texto y devuelve False.

        :return: True si el DNI es válido, False si no lo es.

        """
        try:
            var.ui.txtDNI2.setText(dni)  # Corrección aquí
            tabla = "TRWAGMYFPDXBNJZSKVHLCKE"
            digExt = "XYZ"
            reempDigExt = {"X": '0', "Y": '1', "Z": '2'}
            numeros = "1234567890"
            imgCorrecto = QPixmap('img/aceptar.ico')
            imgIncorrecto = QPixmap('img/cancelar.ico')

            if len(dni) == 9:
                digControl = dni[8]
                dni = dni[:8]
                if dni[0] in digExt:
                    dni = dni.replace(dni[0], reempDigExt[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == digControl:
                    var.ui.lblValidarDNI2.setPixmap(imgCorrecto)
                    var.ui.txtfecha.setFocus()
                    return True
                else:
                    var.ui.lblValidarDNI2.setPixmap(imgIncorrecto)
                    var.ui.txtDNI2.setText(None)
                    var.ui.txtDNI2.setFocus()
                    return False
            else:
                var.ui.lblValidarDNI2.setPixmap(imgIncorrecto)
                var.ui.txtDNI2.setText(None)
                var.ui.txtDNI2.setFocus()
                return False

        except Exception as error:
            print(str(error) + " en validar drivers")



    def validarMovil2(self=None):
        """

        Valida el número de teléfono introducido en el campo correspondiente de la interfaz gráfica.

        Extrae el número de teléfono ingresado en el campo de texto 'txtmovil2' de la interfaz.
        Verifica que el número tenga exactamente 9 dígitos y que todos los caracteres sean dígitos numéricos del 0 al 9.
        Si el número no cumple con estas condiciones, muestra un mensaje de error al usuario y limpia el campo de texto.

        """
        try:
            movil = var.ui.txtmovil2.text()
            numeros = "1234567890"
            var.ui.txtmovil2.setText(movil)  # Corrección aquí
            if len(movil) == 9:
                digControl = movil[:9]
                if len(movil) != len([n for n in movil if n in numeros]) == digControl:
                    raise Exception
            else:
                raise Exception

        except Exception as error:
            eventos.Eventos.error("Aviso", "El telefono debe ser una cadena de 9 numeros enteros")
            var.ui.txtmovil2.setText("")



    def altaCliente(self):
        """

        Gestiona el proceso de alta de un nuevo cliente en el sistema.

        Verifica si el cliente ya existe en la base de datos utilizando el DNI proporcionado.
        Si el cliente ya existe, se le vuelve a dar de alta, lo que significa que se activa nuevamente
        en caso de que haya sido dado de baja anteriormente. Luego, se limpia el panel de entrada de datos
        de cliente y se actualiza la tabla de clientes mostrando los cambios.

        Si el cliente no existe en la base de datos, se verifican los datos obligatorios necesarios para el alta
        (DNI, razón social y número de teléfono móvil). Si alguno de estos campos falta, se muestra un mensaje de advertencia
        y se detiene el proceso de alta.

        Si se proporcionan todos los datos obligatorios, se recopilan los datos del cliente ingresados por el usuario y
        se preparan para ser guardados en la base de datos. Se realiza una validación adicional para asegurarse de que
        se haya seleccionado una provincia y un municipio válidos antes de guardar el cliente.

        Una vez que se guardan los datos del cliente en la base de datos, se muestra un mensaje indicando que el cliente
        se ha añadido correctamente, y se actualiza la lista de clientes en la interfaz gráfica.

        En caso de que ocurra algún error durante el proceso, se imprime un mensaje de error en la consola.

        :return: No devuelve ningún valor explícito.

        """
        try:
            dni = var.ui.txtDNI2.text()
            if conexion.Conexion.verificarCli(dni):
                conexion.Conexion.volverDarAlta2(dni)
                Clientes.limpiarPanel2(self)
                conexion.Conexion.mostrarClientes()
            else:
                if not all([var.ui.txtDNI2.text(), var.ui.txtsocial.text(), var.ui.txtmovil2.text()]):
                    eventos.Eventos.mensaje("Aviso", "Faltan datos obligatorios")
                    return
                cliente = [
                    var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2, var.ui.txtmovil2
                ]
                newCliente = []
                for i in cliente:
                    newCliente.append(i.text().title())

                prov = var.ui.cmbProv2.currentText()
                newCliente.insert(3, prov)
                muni = var.ui.cmbMuni2.currentText()
                newCliente.insert(4, muni)
                valor=conexion.Conexion.guardarcli(newCliente)
                if valor == True:
                    eventos.Eventos.mensaje("Aviso", "El cliente fue añadido con exito")
                    conexion.Conexion.mostrarClientes()
                elif valor == False:
                    eventos.Eventos.error("Aviso", "No se ha podido dar de alta")

        except Exception as error:
            print(str(error) + " en altacliente clientes")



    def modifCli(self):
        """

        Gestiona el proceso de modificación de datos de un cliente existente en el sistema.

        Recolecta los datos ingresados por el usuario para realizar la modificación del cliente.
        Estos datos incluyen el código del cliente, DNI, razón social, dirección, número de teléfono móvil,
        provincia y municipio. Todos los datos son extraídos de los campos de entrada de la interfaz gráfica.

        Una vez recolectados los datos, se realiza la modificación del cliente en la base de datos utilizando
        el método `modifCliente` de la clase `Conexion`. Se actualizan los campos correspondientes en la base de datos
        con los nuevos valores proporcionados por el usuario.

        En caso de que ocurra algún error durante el proceso, se imprime un mensaje de error en la consola.

        """
        try:
            driver = [var.ui.lblcodbd2,var.ui.txtDNI2, var.ui.txtsocial, var.ui.txtdir2, var.ui.txtmovil2]
            modifCliente = []
            for i in driver:
                modifCliente.append(i.text().title())
            prov = var.ui.cmbProv2.currentText()
            modifCliente.insert(4, prov)
            muni = var.ui.cmbMuni2.currentText()
            modifCliente.insert(5, muni)
            conexion.Conexion.modifCliente(modifCliente)
            conexion.Conexion.mostrarClientes()

        except Exception as error:
            print(error, " en modifcli")



    def borraCli(qDate):
        """

        Gestiona el proceso de borrado de un cliente en el sistema.

        Recibe como parámetro un objeto `QDate` que representa la fecha en la que se solicita el borrado del cliente.
        El método convierte esta fecha en un formato legible y luego oculta la ventana de confirmación de borrado.

        A continuación, se obtiene el DNI del cliente de la interfaz gráfica y se utiliza junto con la fecha proporcionada
        para eliminar al cliente de la base de datos, utilizando el método `borrarCli` de la clase `Conexion`.

        Si el cliente no existe o no se puede borrar por algún motivo, se muestra un mensaje de error al usuario.

        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.Bajacli.hide()
            dni = var.ui.txtDNI2.text()
            conexion.Conexion.borrarCli(dni, str(data))
            conexion.Conexion.mostrarClientes()

        except Exception as error:
            eventos.Eventos.error("Aviso", "El cliente no existe o no se puede borrar")