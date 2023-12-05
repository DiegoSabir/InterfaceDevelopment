from PyQt6 import QtWidgets, QtSql, QtGui, QtCore
from windowaux import *
from datetime import date, datetime


import drivers
import clientes
import var


class Conexion():

    """
    * Establecer la conexión a la base de datos SQLite.
    * Define la ubicación de la base de datos (bbdd.sqlite).
    * Utiliza QSqlDatabase para establecer la conexión con la base de datos SQLite.
    * Si la conexión tiene éxito, imprime "base de datos conectada"; de lo contrario, muestra "error de conexión".
    """
    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print("error de conexion")
            return False
        else:
            print("base de datos conectada")
            return True



    """
    * Cargar datos en un combo box relacionado con provincias.
    * Realiza una consulta para obtener las provincias desde la base de datos y carga los resultados 
      en un combo box (cmbProv) en la interfaz gráfica.
    """
    def cargaprov(self=None):
        try:
            var.ui.cmbProv.clear()
            var.ui.cmbProvCli.clear()

            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbProv.addItem('')
                var.ui.cmbProvCli.addItem('')

                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))
                    var.ui.cmbProvCli.addItem(query.value(0))

        except Exception as error:
            print('Error en la carga del combo prov', error)




    """
    * Cargar datos en un combo box relacionado con municipios según la provincia seleccionada.
    * Obtiene la provincia seleccionada por el usuario.
    * Realiza una consulta para obtener los municipios relacionados con esa provincia y los carga 
      en el combo box (cmbMuni) en la interfaz.
    """
    def selMuni(self=None):
        try:
            id = 0
            var.ui.cmbMuni.clear()

            prov = var.ui.cmbProv.currentText()

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
                var.ui.cmbMuni.addItem('')

                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))

        except Exception as error:
            print("Error en la seleccion de municipio: ", error)


    def selMuniCli(self=None):
        try:
            id = 0
            var.ui.cmbMuniCli.clear()

            prov = var.ui.cmbProvCli.currentText()

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
                var.ui.cmbMuniCli.addItem('')

                while query1.next():
                    var.ui.cmbMuniCli.addItem(query1.value(0))

        except Exception as error:
            print("Error en la seleccion de municipio: ", error)




    """
    * Guardar los datos de un nuevo conductor en la base de datos.
    * Verifica que se ingresen los datos mínimos necesarios para un conductor (DNI, apellidos, nombre, 
      fecha de alta y móvil).
    * Realiza una inserción en la tabla de conductores con la información proporcionada.
    """
    @staticmethod
    def guardardri(newdriver):
        try:
            if (newdriver[0].strip() == "" or newdriver[1].strip() == "" or newdriver[2].strip() == ""
                    or newdriver[3].strip() == "" or newdriver[7].strip() == ""):

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mensaje = 'Faltan Datos. Debe introducir al menos:\n\nDNI, Apellidos, Nombre, Fecha de alta y Móvil'
                mbox.setText(mensaje)
                mbox.exec()

            else:
                query = QtSql.QSqlQuery()
                query.prepare('insert into drivers (codigo, dnidri, altadri, apeldri, nombredri, direcciondri, prodri, '
                              ' mundri, movildri, salario, carnet) VALUES (null, :dni, :alta, :apel, :nombre, :direccion, '
                              ' :provincia, :municipio, :movil, :salario, :carnet)')
                query.bindValue(':dni', str(newdriver[1]))
                query.bindValue(':alta', str(newdriver[2]))
                query.bindValue(':apel', str(newdriver[3]))
                query.bindValue(':nombre', str(newdriver[4]))
                query.bindValue(':direccion', str(newdriver[5]))
                query.bindValue(':provincia', str(newdriver[6]))
                query.bindValue(':municipio', str(newdriver[7]))
                query.bindValue(':movil', str(newdriver[8]))
                query.bindValue(':salario', str(newdriver[9]))
                query.bindValue(':carnet', str(newdriver[10]))

                if query.exec():
                    return True
                else:
                    return False

                Conexion.mostrardrivers(self=None)

        except Exception as error:
            print("Error al guardar driver", error)





    @staticmethod
    def guardarcli(newcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into drivers (codigo, dnicli, altacli, razoncli, direccioncli, procli, '
                                  ' mundri, movilcli) VALUES (null, :dni, :alta, :razon :direccion, '
                                  ' :provincia, :municipio, :movil)')

            query.bindValue(':dni', str(newcliente[1]))
            query.bindValue(':alta', str(newcliente[2]))
            query.bindValue(':razon', str(newcliente[3]))
            query.bindValue(':direccion', str(newcliente[4]))
            query.bindValue(':provincia', str(newcliente[5]))
            query.bindValue(':municipio', str(newcliente[6]))
            query.bindValue(':movil', str(newcliente[7]))

            if query.exec():
                return True
            else:
                return False

            Conexion.mostrarclientes(self=None)

        except Exception as error:
            print("Error al guardar cliente", error)





    """
    * Mostrar los conductores en la interfaz gráfica según ciertos criterios.
    * Recupera datos de conductores desde la base de datos según si están dados de alta o no.
    * Carga estos datos en una tabla en la interfaz gráfica.
    """
    def mostrardrivers(self=None):
        try:
            registros = []

            if var.ui.rbtAlta.isChecked():
                estado = 1
                Conexion.selectDrivers(estado)

            else:
                query1=QtSql.QSqlQuery()
                query1.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')

                if query1.exec():
                    while query1.next():
                        row = [query1.value(i) for i in range(query1.record().count())] # función lambda
                        registros.append(row)

            if registros:
                drivers.Drivers.cargartabladri(registros)
                return registros
            else:
                var.ui.tabDrivers.setRowCount(0)

        except Exception as error:
            print("Error al mostrar drivers", error)




    def mostrarclientes(self=None):
        try:
            registros = []

            if var.ui.rbtAltaCli.isChecked():
                estado = 1
                Conexion.selectClientes(estado)

            else:
                query1=QtSql.QSqlQuery()
                query1.prepare('select codigo, razoncli, movildri, bajacli from clientes')

                if query1.exec():
                    while query1.next():
                        row = [query1.value(i) for i in range(query1.record().count())] # función lambda
                        registros.append(row)

            if registros:
                clientes.Clientes.cargartablacli(registros)
                return registros
            else:
                var.ui.tabClientes.setRowCount(0)

        except Exception as error:
            print("Error al mostrar clientes", error)




    """
    * Obtener los datos de un conductor específico.
    * Realiza una consulta para obtener todos los datos relacionados con un conductor específico y los devuelve.
    """
    def onedriver(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))

            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print("Error en fichero conexion datos de un driver", error)






    def onecliente(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from clientes where codigo = :codigo')
            query.bindValue(':codigo', int(codigo))

            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print("Error en fichero conexion datos de un driver", error)





    """
    * Encontrar un conductor por su número de DNI.
    * Realiza una consulta en la base de datos para encontrar al conductor con el DNI proporcionado.
    * Si encuentra un conductor con ese DNI, llama al método onedriver(codigo) para obtener todos 
      los datos del conductor y los devuelve.
    * Si no encuentra un conductor con el DNI especificado, muestra un mensaje de advertencia indicando que 
      el conductor no existe o que hubo un error en la búsqueda.
    """
    def codDri(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers where dnidri = :dnidri')
            query.bindValue(':dnidri', str(dni))

            if query.exec():
                while query.next():
                    codigo = query.value(0)
                if codigo is not None:
                    registro = Conexion.onedriver(codigo)
                    return registro

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("El conductor no existe o error en busqueda")
            mbox.exec()





    def codCli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select * from clientes where dnicli = :dnicli')
            query.bindValue(':dnicli', str(dni))

            if query.exec():
                while query.next():
                    codigo = query.value(0)
                if codigo is not None:
                    registro = Conexion.onecliente(codigo)
                    return registro

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("El cliente no existe o error en busqueda")
            mbox.exec()






    """
    * Modificar los datos de un conductor en la base de datos.
    * Compara los datos modificados con los datos originales del conductor.
    * Realiza una actualización en la base de datos si los datos son diferentes.
    """
    def modifDriver(modifdriver):
        try:
            registro = Conexion.onedriver(int(modifdriver[0]))
            if modifdriver == registro[:-1]:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('No hay datos que modificar. Desea cambiar la fecha o eliminar fecha de baja?')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No |
                                          QtWidgets.QMessageBox.StandardButton.Cancel)
                msg.button(QtWidgets.QMessageBox.StandardButton.Yes).setText("Alta")
                msg.button(QtWidgets.QMessageBox.StandardButton.No).setText("Modificar")
                msg.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
                opcion = msg.exec()

                if opcion == QtWidgets.QMessageBox.StandardButton.Yes:
                    if registro[11] != '':
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update drivers set bajadri = NULL where dnidri = :dni')
                        query1.bindValue(':dni', str(modifdriver[1]))

                        if query1.exec():
                            msg = QtWidgets.QMessageBox()
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                            msg.setText('Datos Conductor Modificados')
                            msg.exec()
                            Conexion.selectDrivers(1)

                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('El conductor está en alta. Nada que modificar')
                        msg.exec()
                        Conexion.selectDrivers(1)

                elif opcion == QtWidgets.QMessageBox.StandardButton.No:
                    var.calendar = Calendar()
                    var.calendar.show()
                    dia = datetime.now().day
                    mes = datetime.now().month
                    ano = datetime.now().year
                    data = var.calendar.selectionChanged.connect(drivers.Drivers.cargaFecha(QtCore.QDate))
                    data = drivers.Drivers.cargaFecha(QtCore.QDate)
                    print(data)

                    if registro[11] != '':
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update drivers set bajadri = :data where dnidri = :dni')
                        query1.bindValue(':data', str(data))
                        query1.bindValue(':dni', str(modifdriver[1]))

                        if query1.exec():
                            msg = QtWidgets.QMessageBox()
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                            msg.setText('Baja Modificada. Nueva Fecha Baja:', str(data))
                            msg.exec()
                            Conexion.selectDrivers(2)

                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('El conductor está en alta. Nada que modificar')
                        msg.exec()
                        Conexion.selectDrivers(1)

                elif opcion == QtWidgets.QMessageBox.StandardButton.Cancel:
                    pass

            else:
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set dnidri = :dni, altadri = :alta, apeldri = :apel, nombredri = :nombre, '
                              'direcciondri = :direccion, prodri = :provincia, mundri = :municipio, movildri = :movil, '
                              'salario = :salario, carnet = :carnet where codigo = :codigo')

                query.bindValue(':codigo', int(modifdriver[0]))
                query.bindValue(':dni', str(modifdriver[1]))
                query.bindValue(':alta', str(modifdriver[2]))
                query.bindValue(':apel', str(modifdriver[3]))
                query.bindValue(':nombre', str(modifdriver[4]))
                query.bindValue(':direccion', str(modifdriver[5]))
                query.bindValue(':provincia', str(modifdriver[6]))
                query.bindValue(':municipio', str(modifdriver[7]))
                query.bindValue(':movil', str(modifdriver[8]))
                query.bindValue(':salario', str(modifdriver[9]))
                query.bindValue(':carnet', str(modifdriver[10]))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Datos del Conductor Modificados")
                    mbox.exec()

                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText(query.lastError().text())
                    mbox.exec()

        except Exception as error:
            print("Error en modificar driver en conexion", error)



    """
    * Marcar a un conductor como dado de baja.
    * Verifica si un conductor ya está marcado como dado de baja.
    * Si no lo está, establece la fecha de baja en la base de datos.
    """
    def borraDriv(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajadri from drivers where dnidri = :dni')
            query1.bindValue(':dni', str(dni))

            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            if str(valor) == '':
                fecha = datetime.today()
                fecha = fecha.strftime('%d/%m/%Y')
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set bajadri = :fechabaja where dnidri = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))

                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Conductor con dado de Baja')
                    msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('No existe conductor o conductor dado de baja anteriormente')
                msg.exec()

        except Exception as error:
            print("Error en baja driver en conexion ", error)




    def borrarCli(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajacli from clientes where dnicli = :dni')
            query1.bindValue(':dni', str(dni))

            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            if str(valor) == '':
                fecha = datetime.today()
                fecha = fecha.strftime('%d/%m/%Y')
                query = QtSql.QSqlQuery()
                query.prepare('update clientes set bajacli = :fechabaja where dnicli = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))

                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Cliente con dado de Baja')
                    msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('No existe cliente o cliente dado de baja anteriormente')
                msg.exec()

        except Exception as error:
            print("Error en baja driver en conexion ", error)









    """
    * Seleccionar conductores según su estado (de alta, de baja, etc.).
    * Selecciona conductores según su estado y los muestra en una tabla en la interfaz gráfica.
    """
    def selectDrivers(estado):
        try:
            registros = []
            if int(estado) == 0:
                query = QtSql.QSqlQuery()
                query.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]   # función lambda
                        registros.append(row)

                if registros:
                    drivers.Drivers.cargartabladri(registros)

                else:
                    var.ui.tabDrivers.setRowCount(0)

            elif int(estado) == 1:
                query = QtSql.QSqlQuery()
                query.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers where bajadri is null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]  # función lambda
                        registros.append(row)

                if registros:
                    drivers.Drivers.cargartabladri(registros)

                else:
                    var.ui.tabDrivers.setRowCount(0)

            elif int(estado) == 2:
                query = QtSql.QSqlQuery()
                query.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers where bajadri is not null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]  # función lambda
                        registros.append(row)

                if registros:
                    drivers.Drivers.cargartabladri(registros)

                else:
                    var.ui.tabDrivers.setRowCount(0)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en cargar tabla o selección de datos')
            msg.exec()





    def selectClientes(estado):
        try:
            registros = []
            if int(estado) == 0:
                query = QtSql.QSqlQuery()
                query.prepare('select codigocli, razoncli, movilcli, bajacli from clientes')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]   # función lambda
                        registros.append(row)

                if registros:
                    clientes.Clientes.cargartablacli(registros)

                else:
                    var.ui.tabClientes.setRowCount(0)

            elif int(estado) == 1:
                query = QtSql.QSqlQuery()
                query.prepare('select codigocli, razoncli, movilcli, bajacli from clientes where bajacli is null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]  # función lambda
                        registros.append(row)

                if registros:
                    clientes.Clientes.cargartablacli(registros)

                else:
                    var.ui.tabClientes.setRowCount(0)

            elif int(estado) == 2:
                query = QtSql.QSqlQuery()
                query.prepare('select codigocli, razoncli, movilcli, bajacli from drivers where bajacli is not null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]  # función lambda
                        registros.append(row)

                if registros:
                    clientes.Clientes.cargartablacli(registros)

                else:
                    var.ui.tabClientes.setRowCount(0)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en cargar tabla o selección de datos')
            msg.exec()





    """
    * Obtener todos los conductores.
    * Realiza una consulta para obtener todos los conductores de la base de datos y devuelve esos datos.
    """
    @staticmethod
    def selectDriverstodos():
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers order by apeldri')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
                return registros

        except Exception as error:
            print("Error al devolver todos los drivers", error)
