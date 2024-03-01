import conexion
import clientes
import eventos
import informes
import var

from PyQt6 import QtWidgets, QtCore, QtGui

class Facturas:
    def limpiarPanel3(self=None):
        """

        Limpia los campos del panel de facturación en la interfaz gráfica.

        Este método se utiliza para limpiar los campos de la interfaz gráfica relacionados con la facturación, como el código de facturación,
        el CIF del cliente, la fecha de la factura y la distancia en kilómetros. También restablece los valores predeterminados de los
        menús desplegables relacionados con la provincia y el municipio de origen y destino.

        """
        try:
            listawidgets = [var.ui.lblcodfacturacion, var.ui.txtcifcli, var.ui.txtfechafact, var.ui.txtkm,
                            var.ui.lblsubtotal, var.ui.lbldescuento, var.ui.lbliva, var.ui.lbltotalfactura]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbCond.setCurrentText('')
            var.ui.tabViajes.clearContents()
            var.ui.tabViajes.setRowCount(0)
            var.ui.cmbProbVentas.setCurrentText('')
            var.ui.cmbProbVentas2.setCurrentText('')
            var.ui.cmbMuniVentas.setCurrentText('')
            var.ui.cmbMuniVentas2.setCurrentText('')

        except Exception as error:
            print(str(error) + " en limpiarpanel 3")



    def validarKm(self=None):
        """

        Valida el campo de kilómetros en la interfaz gráfica.

        Este método se utiliza para validar que el campo de kilómetros en la interfaz gráfica contenga solo números enteros.

        """
        try:
            km = var.ui.txtkm.text()
            numeros = "1234567890"
            var.ui.txtkm.setText(km)  # Corrección aquí
            if len(km):
                if len(km) != len([n for n in km if n in numeros]):
                    raise Exception
            else:
                raise Exception

        except Exception as error:
            eventos.Eventos.error("Aviso", "Los km deben ser de enteros")
            var.ui.txtkm.setText("")



    def buscarClifact(self):
        """

        Busca y muestra información sobre un cliente en la interfaz gráfica de facturación.

        Este método se utiliza para buscar información sobre un cliente utilizando su número de identificación fiscal (DNI).
        Una vez encontrado, muestra la información del cliente en la interfaz gráfica de facturación y colorea la fila
        correspondiente en la tabla de clientes.

        """
        try:
            dni = var.ui.txtcifcli.text()
            registro = conexion.Conexion.codCli(dni)
            clientes.Clientes.auxiliar(registro)
            codigo = var.ui.lblcodbd2.text()
            var.ui.rbtTodos2.setChecked(True)
            conexion.Conexion.mostrarClientes()

        except Exception as error:
            print(str(error) + " en cargarcliente clientes")



    def cargaFechafact(qDate):
        """

        Carga la fecha seleccionada en el campo de fecha de la interfaz gráfica de facturación.

        Este método se utiliza para asignar la fecha seleccionada en el calendario a un campo de texto de la interfaz
        gráfica de facturación.

        :param qDate: La fecha seleccionada en el calendario.

        """
        try:
            data=('{:02d}/{:02d}/{:4d}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtfechafact.setText(str(data))
            var.Altafact.hide()

        except Exception as error:
            print(str(error) + " en cargarfecha fact driver")



    def altafactura(self):
        """

        Procesa el alta de una nueva factura.

        Este método recoge los datos ingresados en la interfaz gráfica de facturación, como el CIF del cliente, la fecha
        de la factura y el conductor seleccionado, y los pasa a la función correspondiente en la capa de conexión para
        realizar el alta de la factura en la base de datos.

        """
        try:
            registro = [var.ui.txtcifcli.text(), var.ui.txtfechafact.text(), var.ui.cmbCond.currentText().split('.')[0]]
            conexion.Conexion.altafacturacion(registro)

        except Exception as error:
            print("error altafact",error)



    def cargarTablaFacturas(registros):
        """

        Carga los registros de facturas en la tabla de la interfaz gráfica.

        Este método toma una lista de registros de facturas y los muestra en la tabla de facturas en la interfaz gráfica,
        colocando cada registro en una fila de la tabla.

        :param registros: La lista de registros de facturas.

        """
        try:
            index = 0
            for registro in registros:
                var.ui.tablaFacturas.setRowCount(index + 1)
                var.ui.tablaFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tablaFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tablaFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tablaFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                btn = QtWidgets.QPushButton()
                btn.setFixedSize(30, 28)
                btn.setIcon(QtGui.QIcon('./img/basura.png'))
                btn.clicked.connect(informes.Informes.reportfactura)
                var.ui.tablaFacturas.setCellWidget(index, 2, btn)
                index += 1

        except Exception as error:
            print("error en cargarTablafacturas", error)



    def cargarFactura(self):
        """

        Carga los detalles de una factura seleccionada en la interfaz gráfica.

        Este método se utiliza para cargar los detalles de una factura seleccionada en la tabla de facturas en la
        interfaz gráfica. Limpia el panel de detalles de la factura, obtiene los detalles de la factura seleccionada,
        muestra estos detalles en el panel y carga los viajes asociados con la factura.

        """
        try:
            listawidgets = [var.ui.lblsubtotal, var.ui.lbldescuento, var.ui.lbliva, var.ui.lbltotalfactura]
            for i in listawidgets:
                i.setText(None)
            Facturas.limpiarPanel3(self)
            row = var.ui.tablaFacturas.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneFactura(fila[0])
            Facturas.auxiliar(registro)
            conexion.Conexion.viajesFactura(registro[0])

        except Exception as error:
            print(str(error) + " en cargarfact")



    def auxiliar(registro):
        """

        Llena el panel de detalles de la factura con la información de la factura seleccionada.

        Este método se utiliza para llenar el panel de detalles de la factura con la información de la factura
        seleccionada en la interfaz gráfica. Obtiene los detalles del conductor asociado a la factura y
        muestra estos detalles junto con los demás detalles de la factura en la interfaz gráfica.

        :param registro: La información de la factura seleccionada.

        """
        try:
            registro2 = conexion.Conexion.oneDriver(registro[3])
            driver = str(registro2[0]) + "." + registro2[3]
            datos = [var.ui.lblcodfacturacion, var.ui.txtcifcli, var.ui.txtfechafact, var.ui.cmbCond]
            for i, dato in enumerate(datos):
                if i == 3:
                    dato.setCurrentText(str(driver))
                else:
                    dato.setText(str(registro[i]))

        except Exception as error:
            eventos.Eventos.error("Aviso", "No existe en la base de datos")



    def colorearFila(numfactura):
        """

        Colorea la fila correspondiente a una factura seleccionada en la tabla de facturas.

        Este método colorea la fila correspondiente a una factura seleccionada en la tabla de facturas
        en la interfaz gráfica. Se utiliza para resaltar visualmente la factura seleccionada.

        :param numfactura: El número de la factura seleccionada.

        """
        for fila in range(var.ui.tablaFacturas.rowCount()):
            if var.ui.tablaFacturas.item(fila, 0).text() == str(numfactura):
                for columna in range(var.ui.tablaFacturas.columnCount()):
                    item = var.ui.tablaFacturas.item(fila, columna)
                    if item is not None:
                        item.setBackground(QtGui.QColor(255, 241, 150))



    def comprobarTarifa(self=None):
        """

        Comprueba y establece automáticamente el tipo de tarifa basándose en la selección de provincias y localidades.

        Este método comprueba la selección de provincias y localidades en los combos de origen y destino, y establece
        automáticamente el tipo de tarifa (provincial, local o nacional) en la interfaz gráfica.

        """
        try:
            provinciaOrigen = var.ui.cmbProbVentas.currentText()
            provinciaDestino = var.ui.cmbProbVentas2.currentText()
            localidadOrigen = var.ui.cmbMuniVentas.currentText()
            localidadDestino = var.ui.cmbMuniVentas2.currentText()

            if provinciaOrigen == provinciaDestino:
                var.ui.rbtProvincial.setChecked(True)
                if localidadOrigen == localidadDestino:
                    var.ui.rbtLocal.setChecked(True)
            else:
                var.ui.rbtNacional.setChecked(True)

        except Exception as error:
            print(error)



    def cargaTablaViajes(valores):
        """

        Carga la tabla de viajes con los valores proporcionados y calcula el subtotal, IVA y total de la factura.

        Este método carga la tabla de viajes con los valores proporcionados, calcula el subtotal, el IVA y el total
        de la factura y actualiza los respectivos campos de la interfaz gráfica.

        :param valores: Los valores de los viajes a cargar en la tabla. Cada valor debe ser una lista con los siguientes
                        elementos: [id_viaje, origen, destino, tarifa, km].

        """
        try:
            var.ui.tabViajes.clearContents()
            var.ui.tabViajes.setRowCount(0)
            subtotal = 0.0
            descuento = 0
            index = 0
            for registro in valores:
                var.ui.tabViajes.setRowCount(index + 1)
                var.ui.tabViajes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                var.ui.tabViajes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabViajes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                var.ui.tabViajes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                var.ui.tabViajes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))

                totalViaje = round(float(registro[4]) * float(registro[3]), 2)
                subtotal = subtotal + totalViaje
                #descuento = subtotal * / 100
                iva = subtotal * 0.21
                var.ui.lblsubtotal.setText(str('{:.2f}'.format(round(subtotal, 2))) + " €")
                var.ui.lbliva.setText(str('{:.2f}'.format(round(iva, 2))) + " €")
                var.ui.lbltotalfactura.setText(str('{:.2f}'.format(round(subtotal + iva, 2))) + " €")
                var.ui.tabViajes.setItem(index, 5, QtWidgets.QTableWidgetItem(str('{:.2f}'.format(totalViaje))))
                var.ui.tabViajes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabViajes.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                btn_borrar = QtWidgets.QPushButton()
                btn_borrar.setFixedSize(30, 28)
                btn_borrar.setIcon(QtGui.QIcon('./img/basura.png'))
                btn_borrar.clicked.connect(Facturas.borrarViaje)
                var.ui.tabViajes.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                var.ui.tabViajes.setColumnWidth(6, 50)
                var.ui.tabViajes.setCellWidget(index, 6, btn_borrar)
                index += 1

        except Exception as error:
            print(str(error) + " en cargatablviajes facturas")



    def guardarViaje(self):
        """

        Guarda un nuevo viaje asociado a una factura.

        Este método guarda un nuevo viaje asociado a una factura seleccionada.
        Verifica que se haya seleccionado una factura y que se hayan ingresado los datos obligatorios del viaje (kilómetros y localidades de origen y destino).
        Calcula la tarifa del viaje según la distancia y el tipo de viaje (local, provincial o nacional) y luego llama al
        método `guardarViaje` de la clase `Conexion` para almacenar el viaje en la base de datos.
        Finalmente, actualiza la tabla de viajes asociados a la factura.

        """
        try:
            if var.ui.lblcodfacturacion.text():
                if var.ui.txtkm.text() and str(var.ui.cmbMuniVentas.currentText()) != "" and str(var.ui.cmbMuniVentas2.currentText()) != "":
                    tarifa = '0.80'
                    if (var.ui.rbtLocal.isChecked()):
                        tarifa = '0.20'
                    elif(var.ui.rbtProvincial.isChecked()):
                        tarifa = '0.40'

                    viaje = [str(var.ui.lblcodfacturacion.text()), str(var.ui.cmbProbVentas.currentText()),
                             str(var.ui.cmbMuniVentas.currentText()), str(var.ui.cmbProbVentas2.currentText()),
                             str(var.ui.cmbMuniVentas2.currentText()), tarifa, str(var.ui.txtkm.text())]
                    conexion.Conexion.guardarViaje(viaje)
                    conexion.Conexion.viajesFactura(var.ui.lblcodfacturacion.text())
                else:
                    eventos.Eventos.error('Aviso', "Faltan campos obligatorios")
            else:
                eventos.Eventos.error('Aviso', "Selecciona primero una factura")

        except Exception as error:
            print(error)



    def cargarViaje(self):
        """

        Carga los datos de un viaje seleccionado en los campos correspondientes del formulario.

        Este método obtiene los datos del viaje seleccionado en la tabla de viajes y los muestra en los campos
        correspondientes del formulario de ingreso de viajes. Primero obtiene la fila seleccionada, luego obtiene los datos
        del viaje a partir del identificador único de viaje y actualiza los campos del formulario con la información del viaje.

        """
        try:
            row = var.ui.tabViajes.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneViajes(fila[0])

            provinciaOrigen, localidadOrigen = registro[2].split(" - ")
            provinciaDestino, localidadDestino = registro[3].split(" - ")

            var.ui.cmbProbVentas.setCurrentText(provinciaOrigen)
            var.ui.cmbMuniVentas.setCurrentText(localidadOrigen)
            var.ui.cmbProbVentas2.setCurrentText(provinciaDestino)
            var.ui.cmbMuniVentas2.setCurrentText(localidadDestino)

            var.ui.txtkm.setText(registro[5])

        except Exception as error:
            print(str(error) + " en cargarviaje")



    def borrarViaje(self):
        """

        Elimina un viaje seleccionado de la base de datos y actualiza la lista de viajes asociados a una factura.

        Este método elimina el viaje seleccionado en la tabla de viajes y luego actualiza la lista de viajes asociados a
        una factura específica. Primero obtiene la fila seleccionada, luego obtiene el identificador único del viaje y
        procede a eliminarlo de la base de datos. Después, actualiza la lista de viajes asociados a la factura correspondiente.

        """
        try:
            row = var.ui.tabViajes.selectedItems()
            fila = [dato.text() for dato in row]
            conexion.Conexion.borrarViaje(fila[0])
            conexion.Conexion.viajesFactura(var.ui.lblcodfacturacion.text())

        except Exception as error:
            print(error)



    def modifViaje(self):
        """

        Modifica la información de un viaje existente.

        Obtiene los datos del viaje desde los campos de la interfaz y actualiza la información en la base de datos.

        :raises Exception: Captura cualquier excepción que ocurra durante la ejecución del método.

        """
        try:
            if var.ui.lblcodfacturacion.text():
                if var.ui.txtkm.text() and str(var.ui.cmbMuniVentas.currentText()) != "" and str(var.ui.cmbMuniVentas2.currentText()) != "":
                    tarifa = '0.80'
                    if (var.ui.rbtLocal.isChecked()):
                        tarifa = '0.20'
                    elif (var.ui.rbtProvincial.isChecked()):
                        tarifa = '0.40'
                    row = var.ui.tabViajes.selectedItems()
                    fila = [dato.text() for dato in row]
                    if fila:
                        id_viaje = fila[0]
                    km = var.ui.txtkm.text().title()

                    provincia_origen = var.ui.cmbProbVentas.currentText()
                    localidad_origen = var.ui.cmbMuniVentas.currentText()
                    provincia_destino = var.ui.cmbProbVentas2.currentText()
                    localidad_destino = var.ui.cmbMuniVentas2.currentText()

                    nuevo_origen = f"{provincia_origen} - {localidad_origen}"
                    nuevo_destino = f"{provincia_destino} - {localidad_destino}"
                    if conexion.Conexion.updateViaje(id_viaje, nuevo_origen, nuevo_destino, tarifa, km):
                        conexion.Conexion.viajesFactura(var.ui.lblcodfacturacion.text())
                        eventos.Eventos.mensaje("Aviso", "Viaje actualizado correctamente")
                    else:
                        eventos.Eventos.error("Error", "No se pudo actualizar el viaje")
                else:
                    eventos.Eventos.error('Aviso',"Faltan campos obligatorios")
            else:
                eventos.Eventos.error('Aviso',"Selecciona primero una factura")

        except Exception as error:
            print(error, " en modifViaje")



    def limpiarViajes(self=None):
        """

        Limpia los widgets del panel de facturación.

        Se encarga de resetear los valores de los widgets relacionados con la facturación.

        """
        try:
            listawidgets = [var.ui.txtkm]
            for i in listawidgets:
                i.setText(None)
            var.ui.cmbProbVentas.setCurrentText('')
            var.ui.cmbProbVentas2.setCurrentText('')
            var.ui.cmbMuniVentas.setCurrentText('')
            var.ui.cmbMuniVentas2.setCurrentText('')

        except Exception as error:
            print(str(error) + " en limpiarpanel 3")
