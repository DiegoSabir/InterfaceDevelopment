from PyQt6 import QtWidgets, QtSql, QtCore, QtGui
from datetime import date, datetime

import drivers, var
import mensage_box


class Conexion():
    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print("[ ERROR DE CONEXION ]:")
        else:
            print("[ BASE DE DATOS CONECTADA ]")

    def cargaProv(self=None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProv.addItem(" ")
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))
        except Exception as error:
            print("Error en la carga del combo ", error)

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
            print("Error al cargar los municipios")

    @staticmethod
    def guardarDri(newDriver):
        try:
            if (newDriver[0].strip() == "" or newDriver[1].strip() == "" or newDriver[2].strip() == "" or newDriver[
                3].strip() == "" or newDriver[7].strip() == ""):
                texto = "Faltan datos. Debe introducir al menor: \nDNI, Apellidos, Nombre, Fecha alta y Movil"
                mensage_box.Mensage_box.mensage_warning(texto)
            else:
                query = QtSql.QSqlQuery()
                query.prepare('insert into drivers (dnidri, altadri, apeldri, nombredri, direcciondri, provinciadri, '
                              'munidri, movildri, salario, carnet) VALUES (:dni, :alta, :apel, :nombre, :direccion,'
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
                    texto = 'Empleado dado de alta'
                    mensage_box.Mensage_box.mensage_information(texto)
                else:
                    texto = query.lastError().text()
                    mensage_box.Mensage_box.mensage_warning(texto)
                Conexion.mostrarDrivers(self=None)
            # Select de los datos de conductores de la base de datos
            # drivers.Drivers.cargarTabla(datosdri)
        except Exception as error:
            print("Error al guardar el driver", error)

    def mostrarDrivers(self = None):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare("select codigo,apeldri,nombredri,movildri,carnet,bajadri from drivers")

            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
                drivers.Drivers.cargarTablaDri(registros)
                print(registros)

        except Exception as error:
            print("Error al cargar los datos", error)

    def oneDriver(codigo):
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
            print("Error en fichero conexion datos de 1 driver: ", error)

    def codDri(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from drivers where dnidri = :dnidri')
            query.bindValue(':dnidri', str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                    registro = Conexion.oneDriver(codigo)
                    return registro
                texto = "El conductor no existe"
                mensage_box.Mensage_box.mensage_warning(texto)

        except Exception as error:
            print("Error al cargar DNI: ", error)

    def modifDriver(modifDriver):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update drivers set dnidri = :dni, altadri = :alta, apeldri = :apel, nombredri = :nombre, '
                          'direcciondri = :direccion, provinciadri = :provincia, munidri = :municipio, movildri = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')
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
                texto = 'Datos del Conductor Modificado Correctamente'
                mensage_box.Mensage_box.mensage_information(texto)
                Conexion.mostrarDrivers(self=None)
            else:
                texto = query.lastError().text()
                mensage_box.Mensage_box.mensage_warning(texto)

        except Exception as error:
            print("Error en conexion al querer modificar el usuario: ", error)

    def borrarDri(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajadri from drivers where dnidri = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            if str(valor) == "":
                fecha = datetime.today()
                fecha = fecha.strftime('%d/%m/%y')
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set bajadri = :fechabaja where dnidri = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))
                if query.exec():
                    texto = 'Conductor dado de baja'
                    mensage_box.Mensage_box.mensage_information(texto)
                    Conexion.mostrarDrivers()

            else:
                texto = 'No existe conductor o conductor o dado de baja anteriormente'
                mensage_box.Mensage_box.mensage_warning(texto)
        except Exception as error:
            print("Error al borrar dri en conexion: ", error)


    def consulta_drivers(fechaBaja):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()

            if fechaBaja == 0:
                query1.prepare("select codigo, apeldri,nombredri,movildri, carnet, bajadri from drivers")
            elif fechaBaja == 1:
                query1.prepare(
                    "select codigo, apeldri,nombredri,movildri, carnet, bajadri from drivers where bajadri is null")
            elif fechaBaja == 2:
                query1.prepare(
                    "select codigo, apeldri,nombredri,movildri, carnet, bajadri from drivers where bajadri is not null")

            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print('Erros mostrar Resultados', error)


    def consulta_drivers_todos(self):
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from drivers order by apeldri")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
                return registros
        except Exception as error:
            print("Error al devolver todos los drivers", error)