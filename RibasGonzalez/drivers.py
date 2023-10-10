import var
from datetime import datetime
class Drivers():

    def limpiarPanel(self):
        try:
            listawidgets = [var.ui.txtDni, var.ui.txtFecha, var.ui.txtApel, var.ui.txtNom,
                            var.ui.txtDir, var.ui.txtMovil, var.ui.txtSalario, var.ui.lblValidarDni]

            for i in listawidgets:
                i.setText(None)

        except Exception as error:
            print("error en limpiar panel driver: ", error)

    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFecha.setText(str(data))
            var.calendar.hide()
        except Exception as error:
            print("error en cargar fecha:", error)

    def validarDNI(self = None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper()
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {"X": '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"

            if len(dni) == 9:  # compruebo que son nueve
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los numeros del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidarDni.setStyleSheet('color:green;')
                    var.ui.lblValidarDni.setText('V')
                else:
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDni.setText(None)
                    var.ui.txtDni.setFocus()
            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.setText(None)
                var.ui.txtDni.setFocus()

        except Exception as error:
            print("error en validar dni ", error)