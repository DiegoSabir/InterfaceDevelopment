from PyQt6 import QtWidgets, QtSql, QtGui
from datetime import date, datetime

import clientes
import conexion
import eventos
import drivers
import var
import facturas

class Conexion():
    def conexion(self=None):
        """

        Establece la conexión con la base de datos SQLite.

        Este método se utiliza para establecer la conexión con la base de datos SQLite especificada en la
        variable 'bbdd'. Primero, asigna el nombre del archivo de la base de datos a la variable 'bbdd'.
        Luego, utiliza la clase QSqlDatabase de PyQt para añadir una base de datos SQLite al sistema y
        establecer el nombre del archivo de la base de datos. Si la conexión es exitosa, imprime un mensaje
        indicando que la base de datos ha sido encontrada y devuelve True. Si hay algún error durante la
        conexión, imprime un mensaje de error y devuelve False.

        :return: True si la conexión es exitosa, False si hay algún error.

        """
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print('error conexion')
            return False

        else:
            print('base datos encontrada')
            return True



    def cargarprov(self=None):
        """

        Carga las provincias en un combo box de la interfaz de usuario.

        Este método se utiliza para cargar las provincias disponibles en la base de datos en un combo box
        de la interfaz de usuario. Primero, limpia cualquier elemento existente en el combo box. Luego,
        ejecuta una consulta SQL para seleccionar todas las provincias de la tabla 'provincias' en la base
        de datos. Por cada provincia recuperada, la añade como un elemento al combo box.

        """
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProv.addItem('')
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))

        except Exception as error:
            print(error, " en cargarprov")



    def selMuni(self=None):
        """

        Selecciona los municipios de una provincia y los carga en el combobox correspondiente.

        Este método se utiliza para seleccionar los municipios de una provincia específica y cargarlos en
        el combobox de municipios correspondiente. Primero, limpia el combobox de municipios. Luego, obtiene
        el nombre de la provincia seleccionada del combobox de provincias y consulta la base de datos para
        obtener el ID de esa provincia. Después, utiliza el ID de la provincia para obtener los municipios
        asociados a esa provincia en la base de datos y los carga en el combobox de municipios. Si ocurre
        algún error durante el proceso, imprime un mensaje de error.

        """
        try:
            id = 0
            var.ui.cmbMuni.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT idprov FROM provincias WHERE provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('SELECT municipio FROM municipios WHERE idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbMuni.addItem('')
                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))

        except Exception as error:
            print(error, " en selMuni")



    @staticmethod
    def guardardri(newDriver):
        """

        Guarda un nuevo conductor en la base de datos.

        :param newDriver: Una lista que contiene los datos del nuevo conductor.

        :return: True si se guardó el conductor correctamente, False en caso contrario.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO drivers (dnidri, altadri, apeldri, nombredri, direcciondri, provdri, '
                          'munidri, movildri, salario, carnet) VALUES(:dni, :alta, :apel, :nombre, :direccion, '
                          ':provincia, :municipio, :movil, :salario, :carnet)')
            query.bindValue(':dni', str(newDriver[0]))
            query.bindValue(':alta', str(newDriver[1]))
            query.bindValue(':apel', str(newDriver[2]))
            query.bindValue(':nombre', str(newDriver[3]))
            query.bindValue(':direccion', str(newDriver[4]))
            query.bindValue(':provincia', str(newDriver[5]))
            query.bindValue(':municipio', str(newDriver[6]))
            query.bindValue(':movil', str(newDriver[7]))
            query.bindValue(':salario', str(newDriver[8]))
            query.bindValue(':carnet', str(newDriver[9]))
            if query.exec():
                return True
            else:
                return False

        except Exception as error:
            print(error, " en guardardri")



    def mostrardriver(self=None):
        """

        Recupera y muestra los registros de conductores según la selección del usuario en la interfaz.

        :return: Una lista de registros de conductores recuperados de la base de datos.

        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            if var.ui.rbtTodos.isChecked():
                query.prepare('SELECT codigo, apeldri, nombredri, movildri, carnet, bajadri FROM drivers')
            if var.ui.rbtAlta.isChecked():
                query.prepare('SELECT codigo, apeldri, nombredri, movildri, carnet, bajadri FROM drivers WHERE bajadri IS NULL')
            if var.ui.rbtBaja.isChecked():
                query.prepare('SELECT codigo, apeldri, nombredri, movildri, carnet, bajadri FROM drivers WHERE bajadri IS NOT NULL')

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            if registros:
                drivers.Drivers.cargarTabladri(registros)
            else:
                var.ui.tabDrivers.setRowCount(0)
            return registros


        except Exception as error:
            print('error mostrardriver', error)



    def oneDriver(codigo):
        """

        Recupera los datos de un conductor específico según su código.

        :param codigo: Código único del conductor.
        :return: Una lista con los detalles del conductor recuperado.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM drivers WHERE codigo=:codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))

            return registro
        except Exception as error:
            print('error oneDriver', error)



    def codDri(dni):
        """

        Recupera los datos de un conductor específico según su DNI.

        :return: Una lista con los datos del conductor recuperado.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM drivers WHERE dnidri=:dnidri')
            query.bindValue(':dnidri', str(dni))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error codDri', error)



    def modifDriver(modifDriver):
        """

        Modifica los datos de un conductor en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update drivers set dnidri= :dni, altadri= :alta, apeldri= :apel, nombredri= :nombre, '
                          ' direcciondri= :direccion, provdri= :provincia, munidri= :municipio, '
                          ' movildri= :movil, salario= :salario, carnet= :carnet where codigo= :codigo')
            query.bindValue(':codigo', int(modifDriver[0]))
            query.bindValue(':dni', str(modifDriver[1]))
            query.bindValue(':alta', str(modifDriver[2]))
            query.bindValue(':apel', str(modifDriver[3]))
            query.bindValue(':nombre', str(modifDriver[4]))
            query.bindValue(':direccion', str(modifDriver[5]))
            query.bindValue(':provincia', str(modifDriver[6]))
            query.bindValue(':municipio', str(modifDriver[7]))
            query.bindValue(':movil', str(modifDriver[8]))
            query.bindValue(':salario', str(modifDriver[9]))
            query.bindValue(':carnet', str(modifDriver[10]))
            if query.exec():
                eventos.Eventos.mensaje("Aviso", "Conductor modificado con exito")
                Conexion.mostrardriver()
            else:
                eventos.Eventos.error("Aviso", query.lastError().text())

        except Exception as error:
            print('error modifdriver', error)



    def borrarDri(dni, fecha):
        """

        Borra un conductor de la base de datos y registra la fecha de baja.

        :param dni: El DNI del conductor que se va a dar de baja.
        :param fecha: La fecha en la que se da de baja al conductor.

        """
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajadri from drivers where '
                          ' dnidri=:dni')
            query1.bindValue(':dni',str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set bajadri= :fechabaja where dnidri=:dni')
                query.bindValue(':fechabaja',str(fecha))
                query.bindValue(':dni',str(dni))
                if query.exec():
                    Conexion.mostrardriver()
                    var.Baja.hide()
                    eventos.Eventos.mensaje("Aviso", "Conductor dado de baja")

        except Exception as error:
            print('error modifdriver', error)



    @staticmethod
    def selectDriverstodos():
        """

        Selecciona todos los registros de conductores de la base de datos y los devuelve en una lista.

        :return: Una lista de todos los registros de conductores de la base de datos.

        """
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select * from drivers order by apeldri')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print('error selectDrivertodos', error)



    @staticmethod
    def verificarDri(dni):
        """

        Verifica si existe un conductor en la base de datos con el DNI especificado.

        :param dni: El DNI del conductor a verificar.

        :return: True si el conductor existe en la base de datos, False en caso contrario.

        """
        try:
            query = QtSql.QSqlQuery()
            consulta = "SELECT COUNT(*) FROM drivers WHERE dnidri = :dni"
            query.prepare(consulta)
            query.bindValue(':dni', dni)

            if query.exec():
                query.next()
                cantidad = query.value(0)
                return cantidad > 0

        except Exception as error:
            print("Error:", str(error))



    def volverDarAlta(dni):
        """

        Vuelve a dar de alta a un conductor que ha sido dado de baja previamente en la base de datos.

        :param dni: El DNI del conductor que se va a dar de alta.

        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Dar Alta")
            mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico.ico"))
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("El conductor está dado de baja.\n¿Desea darlo de alta de nuevo?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("update drivers set bajadri = :baja where dnidri = :dni")
                query.bindValue(":dni", dni)
                query.bindValue(":baja", None)
                if query.exec():
                    eventos.Eventos.mensaje("Aviso", "Conductor dado de alta")
                    conexion.Conexion.cargarconductor()
                else:
                    eventos.Eventos.error("Aviso", "El conductor no se pudo dar de alta")
            else:
                eventos.Eventos.error("Aviso", "Conductor no dado de alta")

        except Exception as error:
            print("Error al dar alta de nuevo conductor en BD", error)



    def oneCliente(codigo):
        """

        Recupera los datos de un cliente específico de la base de datos.

        :return: Una lista que contiene los datos del cliente recuperado.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from clientes where codigo = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print("error en oneCliente", error)



    def mostrarClientes(self=None):
        """

        Recupera y muestra los clientes en la tabla de clientes según la opción seleccionada en los botones de radio.

        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            if var.ui.rbtTodos2.isChecked():
                query.prepare('select codigo, social, movilcli, provcli from clientes')
            if var.ui.rbtAlta2.isChecked():
                query.prepare(
                    'select codigo, social, movilcli, provcli from clientes where bajacli is null')
            if var.ui.rbtBaja2.isChecked():
                query.prepare(
                    'select codigo, social, movilcli, provcli from clientes where bajacli is not null')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            if registros:
                clientes.Clientes.cargarTablaClientes(registros)
            else:
                var.ui.tabClientes.setRowCount(0)

        except Exception as error:
            print("error en mostrarclientes", error)



    def selMuni2(self=None):
        """

        Llena el combo box de municipios según la provincia seleccionada en el combo box de provincias.

        """
        try:
            id = 0
            var.ui.cmbMuni2.clear()
            prov = var.ui.cmbProv2.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id',int(id))
            if query1.exec():
                var.ui.cmbMuni2.addItem('')
                while query1.next():
                    var.ui.cmbMuni2.addItem(query1.value(0))

        except Exception as error:
            print(error, " en selMuni2")



    def cargarprov2(self=None):
        """

        Carga la lista de provincias en el combo box de provincias de la interfaz de usuario.

        """
        try:
            var.ui.cmbProv2.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProv2.addItem('')
                while query.next():
                    var.ui.cmbProv2.addItem(query.value(0))

        except Exception as error:
            print(error, " en cargarprov")



    def verificarCli(dni):
        """

        Verifica si existe un cliente con el DNI proporcionado en la base de datos.

        :param dni: El DNI del cliente a verificar.

        :return: True si existe un cliente con el DNI proporcionado, False en caso contrario.

        """
        try:
            query = QtSql.QSqlQuery()
            consulta = "SELECT COUNT(*) FROM clientes WHERE dnicli = :dni"
            query.prepare(consulta)
            query.bindValue(':dni', dni)

            if query.exec():
                query.next()
                cantidad = query.value(0)
                return cantidad > 0

        except Exception as error:
            print("Error:", str(error))



    @staticmethod
    def guardarcli(newCliente):
        """

        Guarda un nuevo cliente en la base de datos.

        :param newCliente: Una lista que contiene los datos del nuevo cliente

        :return: True si el cliente se guarda correctamente, False si ocurre algún error.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into clientes (dnicli, social, direccioncli, provcli, '
                          'municli, movilcli) VALUES(:dni, :social, :direccion, '
                          ':provincia, :municipio, :movil)')
            query.bindValue(':dni', str(newCliente[0]))
            query.bindValue(':social', str(newCliente[1]))
            query.bindValue(':direccion', str(newCliente[2]))
            query.bindValue(':provincia', str(newCliente[3]))
            query.bindValue(':municipio', str(newCliente[4]))
            query.bindValue(':movil', str(newCliente[5]))
            if query.exec():
                return True
            else:
                return False

        except Exception as error:
            print(error, " en guardarcli")



    def volverDarAlta2(dni):
        """

        Da de alta a un cliente que previamente fue dado de baja en la base de datos.

        :param dni: El número de DNI del cliente que se va a dar de alta.

        """
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Dar Alta")
            mbox.setWindowIcon(QtGui.QIcon("img/aviso.ico"))
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("El cliente está dado de baja.\n¿Desea darlo de alta de nuevo?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("update clientes set bajacli = :baja where dnicli = :dni")
                query.bindValue(":dni", dni)
                query.bindValue(":baja", None)
                if query.exec():
                    eventos.Eventos.mensaje("Aviso", "Cliente dado de alta")
                else:
                    eventos.Eventos.error("Aviso", "El cliente no se pudo dar de alta")
            else:
                eventos.Eventos.error("Aviso", "Cliente no dado de alta")

        except Exception as error:
            print("Error al dar alta de nuevo cliente en BD", error)



    def modifCliente(modifCliente):
        """

        Modifica los datos de un cliente en la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update clientes set dnicli= :dni, social= :social, '
                          ' direccioncli= :direccion, provcli= :provincia, municli= :municipio, '
                          ' movilcli= :movil where codigo= :codigo')
            query.bindValue(':codigo', int(modifCliente[0]))
            query.bindValue(':dni', str(modifCliente[1]))
            query.bindValue(':social', str(modifCliente[2]))
            query.bindValue(':direccion', str(modifCliente[3]))
            query.bindValue(':provincia', str(modifCliente[4]))
            query.bindValue(':municipio', str(modifCliente[5]))
            query.bindValue(':movil', str(modifCliente[6]))
            if query.exec():
                eventos.Eventos.mensaje("Aviso", "Cliente modificado con exito")
            else:
                eventos.Eventos.error("Aviso", query.lastError().text())

        except Exception as error:
            print('error modifclienter', error)



    def borrarCli(dni, fecha):
        """

        Da de baja a un cliente en la base de datos.

        :param dni: El DNI del cliente que se marcará como dado de baja.
        :param fecha: La fecha en la que se dará de baja al cliente.

        """
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajacli from clientes where dnicli=:dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)
                query = QtSql.QSqlQuery()
                query.prepare('update clientes set bajacli= :fechabaja where dnicli=:dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))
                if query.exec():
                    Conexion.mostrarClientes()
                    var.Bajacli.hide()
                    eventos.Eventos.mensaje("Aviso", "Cliente dado de baja")

        except Exception as error:
            print('error borrarcvli', error)



    @staticmethod
    def selectClientesstodos():
        """

        Selecciona todos los clientes de la base de datos y los devuelve en una lista de registros.

        :return: Una lista de registros que contiene todos los clientes de la base de datos.

        """
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select * from clientes order by social')
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print('error selectDrivertodos', error)



    def codCli(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from clientes where dnicli=:dnicli')
            query.bindValue(':dnicli', str(dni))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error codcli', error)



    def cargarconductor(self=None):
        """

        Carga los conductores activos en el combo box de conductores.

        """
        try:
            var.ui.cmbCond.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, apeldri from drivers where bajadri is null order by codigo')
            if query.exec():
                var.ui.cmbCond.addItem('')
                while query.next():
                    var.ui.cmbCond.addItem(str(query.value(0)) + "." + str(query.value(1)))

        except Exception as error:
            print(error, " cargar cond")



    def verificarClibaja(dni):
        """

        Verifica si un cliente con el DNI especificado está activo (sin baja).

        :param dni: El DNI del cliente a verificar.

        :return: True si el cliente está activo (sin baja), False de lo contrario.

        """
        try:
            query = QtSql.QSqlQuery()
            consulta = "SELECT COUNT(*) FROM clientes WHERE dnicli = :dni and bajacli is null"
            query.prepare(consulta)
            query.bindValue(':dni', dni)

            if query.exec():
                query.next()
                cantidad = query.value(0)
                return cantidad > 0

        except Exception as error:
            print("Error:", str(error))



    def altafacturacion(registro):
        """

        Registra una nueva factura en la base de datos.

        :param registro: Una lista que contiene el DNI del cliente, la fecha de la factura y el código del conductor.

        """
        try:
            if not all([var.ui.txtcifcli.text(), var.ui.txtfechafact.text(), var.ui.cmbCond.currentText().split('.')[0]]):
                eventos.Eventos.error("Aviso", "Faltan datos obligatorios")
            else:
                dni = var.ui.txtcifcli.text()
                if Conexion.verificarClibaja(dni):
                    query = QtSql.QSqlQuery()
                    query.prepare('insert into facturas(dnicli, fecha, driver) values(:dni, :fecha, :driver)')
                    query.bindValue(":dni", str(registro[0]))
                    query.bindValue(":fecha", str(registro[1]))
                    query.bindValue(":driver", str(registro[2]))
                    if query.exec():
                        eventos.Eventos.mensaje("Aviso", "Factura guardada")
                        Conexion.cargarfacturas()
                else:
                    eventos.Eventos.error("Aviso", "Cliente no existente o dado de baja")

        except Exception as error:
            print(error, " cargar cond")



    @staticmethod
    def cargarfacturas():
        """

        Carga las facturas almacenadas en la base de datos y las muestra en la tabla de facturas.

        """
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare('select numfac, dnicli from facturas')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            facturas.Facturas.cargarTablaFacturas(registros)

        except Exception as error:
            print(error, "cargarfacturas")



    def oneFactura(codigo):
        """

        Recupera los detalles de una factura específica según su número de factura.

        :param codigo: El número de factura de la factura que se desea recuperar.

        :return: Una lista que contiene los detalles de la factura.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from facturas where numfac = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(4):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print("error en onefactura", error)



    def selMuni3(self=None):
        """

        Selecciona y carga los municipios correspondientes a una provincia seleccionada en el combo box de provincias.

        """
        try:
            id = 0
            var.ui.cmbMuniVentas.clear()
            prov = var.ui.cmbProbVentas.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbMuniVentas.addItem('')
                Conexion.datosViaje()
                while query1.next():
                    var.ui.cmbMuniVentas.addItem(query1.value(0))

        except Exception as error:
            print(error, " en selMuni2")



    def cargarprov3(self=None):
        """

        Carga las provincias en el combo box de provincias.

        """
        try:
            var.ui.cmbProbVentas.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProbVentas.addItem('')
                Conexion.datosViaje()
                while query.next():
                    var.ui.cmbProbVentas.addItem(query.value(0))

        except Exception as error:
            print(error, " en cargarprov")



    def selMuni4(self=None):
        """

        Selecciona los municipios según la provincia elegida en cmbProbVentas2 que es el destino y los carga en cmbMuniVentas2 que tambien es del destino.

        :param self: Parámetro opcional, puede ser nulo.

        """
        try:
            id = 0
            var.ui.cmbMuniVentas2.clear()
            prov = var.ui.cmbProbVentas2.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbMuniVentas2.addItem('')
                Conexion.datosViaje()
                while query1.next():
                    var.ui.cmbMuniVentas2.addItem(query1.value(0))

        except Exception as error:
            print(error, " en selMuni2")



    def cargarprov4(self=None):
        """

        Carga las provincias en el combo box cmbProbVentas2 que es el de destino.

        :param self: Parámetro opcional, puede ser nulo.

        """
        try:
            var.ui.cmbProbVentas2.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProbVentas2.addItem('')
                Conexion.datosViaje()
                while query.next():
                    var.ui.cmbProbVentas2.addItem(query.value(0))

        except Exception as error:
            print(error, " en cargarprov")



    @staticmethod
    def datosViaje():
        """

        :return: modulo que devuelve registro de un viaje
        :rtype: bytearray

        Este modulo carga los datos de los widgets del panel de gestion,
        selecciona la tarifa en funcion del tipo de viaje
        y devuelve un array con los datos.

        """
        try:
            facturas.Facturas.comprobarTarifa()
            tarifas = [0.20, 0.40, 0.80]
            datosviaje = [var.ui.cmbProbVentas.currentText(), var.ui.cmbMuniVentas, var.ui.cmbProbVentas2.currentText(),
                          var.ui.cmbMuniVentas2]
            if str(datosviaje[0]) == str(datosviaje[2]):
                if str(datosviaje[1]) == str(datosviaje[3]):
                    datosviaje.append(str(tarifas[2]))
                    return datosviaje
                else:
                    datosviaje.append(str(tarifas[1]))
                    return datosviaje
            else:
                datosviaje.append(str(tarifas[0]))
                return datosviaje

        except Exception as error:
            print(error, " en datos viaje")



    def viajesFactura(dato):
        """

        Carga los viajes asociados a una factura en la tabla de viajes de la interfaz de facturas.

        :param dato: Número de factura.

        """
        try:
            valores = []
            query = QtSql.QSqlQuery()
            query.prepare("select idviaje, origen, destino, tarifa, km from viajes where factura = :dato")
            query.bindValue(':dato', str(dato))
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    valores.append(row)
            facturas.Facturas.cargaTablaViajes(valores)

        except Exception as error:
            print("ERROR CARGAR viaje a la vista", error)



    def cargarLineaViaje(registro):
        """

        Registra un nuevo viaje en la base de datos.

        :param registro: Lista que contiene los datos del viaje: [origen, destino, tarifa, kilometros, factura].

        """
        try:
            if any(not elemento.strip() for elemento in registro):
                eventos.Eventos.error("Aviso", "Faltan datos del viaje o numero de factura")
            else:
                query = QtSql.QSqlQuery()
                query.prepare("insert into viajes(factura, origen, destino, tarifa, km) values (:factura, :origen, :destino, :tarifa, :kilometros)")
                query.bindValue(":factura", int(registro[5]))
                query.bindValue(":origen", int(registro[1]))
                query.bindValue(":destino", int(registro[2]))
                query.bindValue(":tarifa", int(registro[3]))
                query.bindValue(":kilometros", str(registro[4]))
                if query.exec():
                    eventos.Eventos.mensaje('Aviso', 'Viaje grabado en base de datos')
                    facturas.Facturas.cargaTablaViajes()

        except Exception as error:
            print(error, " en cargarprov")



    def guardarViaje(viaje):
        """

        Guarda un nuevo viaje en la base de datos.

        :param viaje: Lista que contiene los detalles del viaje en el siguiente orden: [factura, origen_ciudad, origen_provincia, destino_ciudad, destino_provincia, tarifa, kilometros].

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("insert into viajes (factura, origen, destino, tarifa, km) values (:factura, :origen, :destino, :tarifa, :kilometros)")
            query.bindValue(":factura", viaje[0])
            query.bindValue(":origen", viaje[1] + " - " + viaje[2])
            query.bindValue(":destino", viaje[3] + " - " + viaje[4])
            query.bindValue(":tarifa", viaje[5])
            query.bindValue(":kilometros", viaje[6])
            if query.exec():
                eventos.Eventos.mensaje('Aviso', "Viaje guardado")
            else:
                eventos.Eventos.error('Aviso', "Error al guardar el viaje")

        except Exception as error:
            print(error)



    def oneViajes(codigo):
        """

        Devuelve los detalles de un viaje específico identificado por su código.

        :param codigo: El código único del viaje que se desea obtener.

        :return: Una lista que contiene los detalles del viaje, incluyendo la factura, origen, destino, tarifa, kilometros y otros detalles.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from viajes where idviaje = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(6):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print("error en oneviaje", error)



    def borrarViaje(id):
        """

        Elimina un viaje de la base de datos según su ID.

        :param id: El ID único del viaje que se desea eliminar.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("delete from viajes where idviaje = :id")
            query.bindValue(":id", int(id))
            if query.exec():
                eventos.Eventos.mensaje('Aviso', "Viaje eliminado correctamente")
            else:
                eventos.Eventos.error('Aviso', "Error al borrar el viaje")

        except Exception as error:
            print(error)



    def updateViaje(viaje_id, nuevo_origen, nuevo_destino,tarifa, km):
        """

        Actualiza un viaje en la base de datos.

        :param viaje_id: ID del viaje a ser actualizado.
        :param nuevo_origen: Nueva ubicación de origen del viaje.
        :param nuevo_destino: Nueva ubicación de destino del viaje.
        :param tarifa: Nueva tarifa del viaje.
        :param km: Nuevos kilómetros del viaje.
        :return: True si la actualización fue exitosa, False en caso contrario.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("update viajes set origen=:origen, destino=:destino, tarifa=:tarifa, km=:kilometros where idviaje=:id")
            query.bindValue(":id", viaje_id)
            query.bindValue(":origen", nuevo_origen)
            query.bindValue(":destino", nuevo_destino)
            query.bindValue(":tarifa", tarifa)
            query.bindValue(":kilometros", km)

            return query.exec()

        except Exception as error:
            print("Error en updateViaje:", error)
            return False



    def cargarfacturasClientes(self=None):
        """

        Carga los números de factura y DNIs de clientes desde la tabla facturas para un DNI específico.

        """
        try:
            dni = var.ui.txtcifcli.text()
            if var.ui.txtcifcli != "":
                registros = []
                query = QtSql.QSqlQuery()
                query.prepare('select numfac, dnicli from facturas where dnicli = :dnicli')
                query.bindValue(':dnicli', str(dni))
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                facturas.Facturas.cargarTablaFacturas(registros)
            else:
                eventos.Eventos.error("Aviso","Debe introducir un dni")

        except Exception as error:
            print(error, "cargarfacturas")