from PyQt6 import QtWidgets, QtCore, QtGui

import conexion
import var

class Drivers():


    """
    * Limpia varios elementos de la interfaz gráfica relacionados con los datos del conductor.
    * Verifica el estado de un botón de radio (var.ui.rbtAlta) y llama a métodos de conexion para seleccionar
      los conductores basándose en ese estado.
    """
    @staticmethod
    def limpiapanel(self):
        try:
            listawidgets = [var.ui.lblcodbd, var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtNome,
                            var.ui.txtApel, var.ui.txtDirdriver, var.ui.txtSalario, var.ui.txtMovil,
                            var.ui.lblValidardni]

            for i in listawidgets:
                i.setText(None)

            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                i.setChecked(False)

            var.ui.cmbProv.setCurrentText('')
            var.ui.cmbMuni.setCurrentText('')

            if var.ui.rbtAlta.isChecked():
                estado = 1
                conexion.Conexion.selectDrivers(estado)
            else:
                registros = conexion.Conexion.mostrardrivers(self)
                Drivers.cargartabladri(registros)

        except Exception as error:
            print('Error al limpiar el panel driver: ', error)



    """
    * Recibe una fecha (qDate) y la formatea para mostrarla en un campo de texto de la 
      interfaz gráfica (var.ui.txtDatadriver)
    """
    def cargaFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtDatadriver.setText(str(data))
            return data
            var.calendar.hide()

        except Exception as error:
            print("Error al cargar fecha: ", error)



    """
    * Valida un número de identificación nacional (DNI).
    * Verifica si el DNI es válido siguiendo una serie de reglas y condiciones.
    * Actualiza elementos de la interfaz gráfica (var.ui.lblValidardni, var.ui.txtDni) para reflejar el 
      estado de validez del DNI.
    """
    def validarDNI(dni):
        try:
            dni = str(dni).upper() #poner mayúscula
            var.ui.txtDni.setText(str(dni))
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:          #comprueba que son nueve
                dig_control = dni[8]    #tomo la letra del dni
                dni = dni[:8]           #tomo los números del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) %23] == dig_control:
                    var.ui.lblValidardni.setStyleSheet('color:green;')  # si es válido se pone una V en color verde
                    var.ui.lblValidardni.setText('V')
                    return True
                else:
                    var.ui.lblValidardni.setStyleSheet('color:red;')    #y si no una X en color rojo
                    var.ui.lblValidardni.setText('X')
                    var.ui.txtDni.clear(None)
                    var.ui.txtDni.setFocus()
            else:
                var.ui.lblValidardni.setStyleSheet('color:red;')
                var.ui.lblValidardni.setText('X')
                var.ui.txtDni.clear(None)
                var.ui.txtDni.setFocus()

        except Exception as error:
            print("Error en la validacion del dni", error)



    """
    * Registra un nuevo conductor utilizando datos proporcionados en la interfaz gráfica (var.ui) y almacenados en newdriver.
    * Convierte los datos en formato legible y los almacena en la base de datos a través de métodos de conexion.
    * Muestra un cuadro de diálogo (QtWidgets.QMessageBox) dependiendo del resultado de la operación.
    """
    def altadriver(self):
        try:
            driver = [var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                      var.ui.txtDirdriver, var.ui.txtMovil, var.ui.txtSalario]

            newdriver = []
            for i in driver:
                newdriver.append(i.text().title())

            prov = var.ui.cmbProv.currentText()
            newdriver.insert(5,prov)
            muni = var.ui.cmbMuni.currentText()
            newdriver.insert(6,muni)

            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())
            newdriver.append('-'.join(licencias))
            valor = conexion.Conexion.guardardri(newdriver)

            if valor == True:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Empleado dado de alta")
                mbox.exec()
            elif valor == False:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Asegúrese de que el conductor no existe")
                mbox.exec()

        except Exception as error:
            print("Error al dar de alta", error)



    """
    * Actualiza la tabla de conductores (var.ui.tabDrivers) con datos obtenidos de la base de datos y 
      proporcionados en registros.
    """
    def cargartabladri(registros):
        try:
            var.ui.tabDrivers.clearContents()
            index = 0
            for registro in registros:
                var.ui.tabDrivers.setRowCount(index+1) #crea una fila
                var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                var.ui.tabDrivers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))
                var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1

        except Exception as error:
            print("Error al cargar los datos en la tabla", error)



    """
    * Este método se encarga de cargar los datos de un conductor seleccionado en la tabla de conductores (var.ui.tabDrivers).
    * Obtiene la fila seleccionada, extrae los datos y llama a conexion.Conexion.onedriver() para obtener los detalles 
      del conductor seleccionado.
    * Finalmente, llama a Drivers.cargadatos() para mostrar estos datos en la interfaz gráfica.
    """
    def cargadriver(self):
        try:
            fila = var.ui.tabDrivers.selectedItems()
            row = [dato.text() for dato in fila]
            registro = conexion.Conexion.onedriver(row[0])
            Drivers.cargadatos(registro)

        except Exception as error:
            print("Error al cargar los datos de un cliente marcando en la tabla: ", error)



    """
    * Busca un conductor en la base de datos basándose en el DNI proporcionado en var.ui.txtDni.
    * Llama a métodos de conexion para obtener los detalles del conductor y luego carga estos datos en la interfaz 
      gráfica utilizando Drivers.cargadatos().
    * Dependiendo de la opción seleccionada en la interfaz (var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja), realiza 
      una búsqueda específica de conductores y actualiza la visualización en la tabla de conductores.
    """
    def buscaDri(self):
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codDri(dni)
            Drivers.cargadatos(registro)

            if var.ui.rbtTodos.isChecked():
                estado = 0
                conexion.Conexion.selectDrivers(estado)
            elif var.ui.rbtAlta.isChecked():
                estado = 1
                conexion.Conexion.selectDrivers(estado)
            elif var.ui.rbtBaja.isChecked():
                estado = 2
                conexion.Conexion.selectDrivers(estado)

            codigo = var.ui.lblcodbd.text()
            for fila in range(var.ui.tabDrivers.rowCount()):
                if var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                    for columna in range(var.ui.tabDrivers.columnCount()):
                        item = var.ui.tabDrivers.item(fila, columna)
                        if item is not None:
                            item.setBackground(QtGui.QColor(255, 241, 150))

        except Exception as error:
            print(error, "al buscar datos de un conductor")



    """
    * Carga los datos de un conductor en los diferentes elementos de la interfaz gráfica.
    * Recibe registro, que es una lista con los detalles del conductor.
    * Actualiza los campos de texto, cuadros de selección y casillas de verificación de la interfaz gráfica (var.ui) 
      con la información del conductor.
    * Verifica las licencias almacenadas en registro y establece el estado de las casillas de verificación 
      (chkA, chkB, chkC, chkD) en consecuencia.
    """
    def cargadatos(registro):
        try:
            datos = [var.ui.lblcodbd, var.ui.txtDni, var.ui.txtDatadriver, var.ui.txtApel, var.ui.txtNome,
                     var.ui.txtDirdriver, var.ui.cmbProv, var.ui.cmbMuni, var.ui.txtMovil, var.ui.txtSalario]

            for i, dato in enumerate(datos):
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            else:
                var.ui.chkA.setChecked(False)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            else:
                var.ui.chkB.setChecked(False)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            else:
                var.ui.chkC.setChecked(False)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)
            else:
                var.ui.chkD.setChecked(False)

        except Exception as error:
            print("Error al cargar los datos en el panel de gestión", error)


    """
    * Se encarga de modificar los detalles de un conductor en la base de datos.
    * Obtiene los nuevos detalles de conductor desde los campos de la interfaz gráfica (var.ui).
    * Llama a conexion.Conexion.modifDriver() para aplicar estos cambios en la base de datos.
    """
    def modifDri(self):
        try:
            driver = [var.ui.lblcodbd, var.ui.txtDni, var.ui.txtDatadriver,var.ui.txtApel,
                      var.ui.txtNome, var.ui.txtDirdriver, var.ui.txtMovil, var.ui.txtSalario]

            modifdriver = []
            for i in driver:
                modifdriver.append(i.text().title())

            prov = var.ui.cmbProv.currentText()
            modifdriver.insert(6, prov)
            muni = var.ui.cmbMuni.currentText()
            modifdriver.insert(7, muni)

            licencias = []
            chklicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chklicencia:
                if i.isChecked():
                    licencias.append(i.text())

            modifdriver.append('-'.join(licencias))
            conexion.Conexion.modifDriver(modifdriver)

        except Exception as error:
            print("Error al modificar driver", error)



    """
    * Elimina un conductor de la base de datos utilizando el DNI proporcionado en var.ui.txtDni.
    * Invoca a conexion.Conexion.borraDriv() y actualiza la tabla de conductores después de borrar el conductor. 
    """
    def borrarDriv(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.borraDriv(dni)
            conexion.Conexion.selectDrivers(1)

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("El conductor no existe o no se puede borrar")
            mbox.exec()



    """
    * Según la opción seleccionada en la interfaz gráfica (var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja), 
      selecciona conductores basados en su estado.
    * Llama a conexion.Conexion.selectDrivers() con el estado correspondiente para actualizar la visualización 
      de la tabla de conductores.
    """
    def selEstado(self):
        if var.ui.rbtTodos.isChecked():
            estado = 0
            conexion.Conexion.selectDrivers(estado)

        elif var.ui.rbtAlta.isChecked():
            estado = 1
            conexion.Conexion.selectDrivers(estado)

        elif var.ui.rbtBaja.isChecked():
            estado = 2
            conexion.Conexion.selectDrivers(estado)
