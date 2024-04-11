from PyQt6 import QtWidgets, QtCore, QtSql

import connection
import var
import re


class Customer():
    @staticmethod
    def checkEmail(email):
        """
        Método estático para validar un email.

        :param email: El email a validar.
        :type email: str

        :return: True si el email es válido, False si no lo es.
        :rtype: bool
        """
        try:
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(pattern, email):
                return True
            else:
                return False

        except Exception as error:
            print("error en validar email ", error)



    @staticmethod
    def loadDate(qDate):
        """
        Método estático para cargar una fecha en un campo de texto.

        :param qDate: La fecha a cargar.
        :type qDate: QtCore.QDate

        :return: No hay valor de retorno.
        :rtype: None
        """
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDataDriver.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en cargar data", error)



    @staticmethod
    def cleanInterface():
        """
        Método estático para limpiar todos los widgets en el panel.

        :return: No hay valor de retorno.
        :rtype: None
        """
        try:
            listaWidgets = [var.ui.lblId, var.ui.txtSurname, var.ui.txtName, var.ui.txtBirthdate, var.ui.txtAddress, var.ui.txtTelephone, var.ui.txtEmail]
            for i in listaWidgets:
                i.clear()

            chk = [var.ui.chkAll]
            for i in chk:
                i.setChecked(False)

            #var.ui.tabViajes.setRowCount(0)

            #Recargar todos los viajes
            #conexion.Conexion.selectFactura()

        except Exception as error:
            print("error ao limpiar panel", error)



    @staticmethod
    def altaDriver():
        """
        Método estático para dar de alta un conductor en la base de datos.

        :return: No hay valor de retorno.
        :rtype: None
        """
        try:
            if var.ui.lblId.text() != "":
                codigo = var.ui.lblId.text()
                if Drivers.comprobarfechabaja(codigo):
                    if Drivers.validarDNI(var.ui.txtDNI.text()):
                        conexion.Conexion.borrarfechabaja(codigo)
                        Drivers.selEstado()
                    else:
                        mbox = QtWidgets.QMessageBox()
                        mbox.setWindowTitle('Aviso')
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                        mbox.setText("DNI no válido")
                        mbox.exec()
                        var.ui.lblValidarDNI.setText('X')
                        var.ui.lblValidarDNI.setStyleSheet('color:red;')
                        var.ui.txtDNI.clear()
                        var.ui.txtDNI.setFocus()
            else:
                if Drivers.validarDNI(var.ui.txtDNI.text()):
                    driver = [var.ui.txtDNI,
                              var.ui.txtDataDriver,
                              var.ui.txtNombre,
                              var.ui.txtApel,
                              var.ui.txtDirDriver,
                              var.ui.txtMovilDriver,
                              var.ui.txtSalario]
                    newdriver = []
                    for i in driver:
                        newdriver.append(i.text().title())

                    prov = var.ui.cmbProv.currentText()
                    newdriver.insert(5, prov)
                    muni = var.ui.cmbMuni.currentText()
                    newdriver.insert(6, muni)

                    licencias = []
                    chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
                    for i in chklicencia:
                        if i.isChecked():
                            licencias.append(i.text())
                    newdriver.append('/'.join(licencias))

                    conexion.Conexion.guardardri(newdriver)
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("DNI no válido")
                    mbox.exec()
                    var.ui.lblValidarDNI.setText('X')
                    var.ui.lblValidarDNI.setStyleSheet('color:red;')
                    var.ui.txtDNI.clear()
                    var.ui.txtDNI.setFocus()

            conexion.Conexion.cargardriverfac()

        except Exception as error:
            print("Error con alta driver", error)


