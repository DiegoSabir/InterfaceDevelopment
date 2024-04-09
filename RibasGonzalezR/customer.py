from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt

import var
import connection

class Customer():
    def cleanScreen(self=None):
        try:
            listwidgets = [var.ui.lblId, var.ui.txtSurname, var.ui.txtName, var.ui.txtBirthdate, var.ui.txtAddress, var.ui.txtTelephone, var.ui.txtEmail]
            for i in listwidgets:
                i.setText(None)

        except Exception as error:
            print(str(error) + " clearing the screen")


    def loadDate(qDate):
        """

        Carga la fecha seleccionada en el campo de texto de fecha.

        Este método toma la fecha seleccionada del calendario y la formatea en el formato 'dd/mm/yyyy',
        luego la establece como texto en el campo de texto de fecha y oculta el calendario.

        :param qDate: La fecha seleccionada del calendario.

        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtBirthdate.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print(str(error) + " loading date")



    def printRow(codigo):
        try:
            for fila in range(var.ui.tabCustomers.rowCount()):
                if var.ui.tabCustomers.item(fila, 0).text() == str(codigo):
                    for columna in range(var.ui.tabCustomers.columnCount()):
                        item = var.ui.tabCustomers.item(fila, columna)
                        if item is not None:
                            item.setBackground(QtGui.QColor(255, 241, 150))

        except Exception as error:
            print("error en colorearFila", error)



    def loadCustomer(self):
        try:
            Customer.cleanScreen()
            row = var.ui.tabCustomers.selectedItems()
            fila = [dato.text() for dato in row]
            registro = connection.Connection.oneCustomer(fila[0])
            Customer.auxiliar(registro)
            connection.Connection.showCustomers()
            Customers.printRow(registro[0])

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
            datos = [var.ui.lblId, var.ui.txtSurname, var.ui.txtName, var.ui.txtBirthdate, var.ui.txtAddress, var.ui.txtTelephone, var.ui.txtEmail]
            for i, dato in enumerate(datos):
                if i == 5 or i == 6:
                    dato.setCurrentText(str(registro[i]))
                else:

                    dato.setText(str(registro[i]))

        except Exception as error:
            eventos.Eventos.error("Aviso", "No existe en la base de datos")