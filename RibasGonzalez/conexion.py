from datetime import datetime
from PyQt6 import QtWidgets, QtSql, QtCore
import var, drivers


class Conexion():
    def conexion(self = None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print("error de conexion")
            return False
        else:
            print("base de datos conectada")
            return True


    def cargaprov(self=None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProv.addItem(' ')
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))
        except Exception as error:
            print('error en la carga del combo prov', error)


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
                var.ui.cmbMuni.addItem("Seleccione la localidad")
                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))

        except Exception as error:
            print("error seleccion municipio: ", error)

    @staticmethod
    def guardardri(newdriver):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into drivers (dnidri, altadri, apeldri, nombredri, direcciondri, prodri, '
                          ' mundri, movildri, salario, carnet) VALUES (:dni, :alta, :apel, :nombre, :direccion, '
                          ' :provincia, :municipio, :movil, :salario, :carnet)')
            query.bindValue(':dni', str(newdriver[0]))
            query.bindValue(':alta', str(newdriver[1]))
            query.bindValue(':apel', str(newdriver[2]))
            query.bindValue(':nombre', str(newdriver[3]))
            query.bindValue(':direccion', str(newdriver[4]))
            query.bindValue(':provincia', str(newdriver[5]))
            query.bindValue(':municipio', str(newdriver[6]))
            query.bindValue(':movil', str(newdriver[7]))
            query.bindValue(':salario', str(newdriver[8]))
            query.bindValue(':carnet', str(newdriver[9]))
            print(newdriver)
            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Listo')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Empleado dado de alta")
                mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.setText("Asegurese de que el conductor no existe")
                mbox.exec()

        except Exception as error:
            print("error en alta conductor", error)


    def mostrardrivers(self = None):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')

            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
                drivers.Drivers.cargartabladri(registros)

                #return registros
                print(registros)

        except Exception as error:
            print("error al mostrar los datos", error)


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
            print("error en fichero conexion", error)

    def codDri(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from drivers where dnidri = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                    registro = Conexion.onedriver(codigo)
                    return registro

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("El conductor no existe")
                mbox.exec()
        
        except Exception as error:
            print(error, " en busca de codigo de un conductor")


    def modifDriver(modifdriver):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update drivers set dnidri = :dni, altadri = : alta, apeldri = :apel, nombredri = :nombre, '
                          ' direcciondri = :direccion, provdri = :provincia, munidri = :municipio, '
                          ' movildri = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')

            query.bindValue(':codigo', str(modifdriver[0]))
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
                mbox.setText("Datos Conductor Modificados")
                mbox.exec()
                Conexion.mostrardrivers(self = None)

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()

        except Exception as error:
            print("error en modificar driver en conexion", error)


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
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Todo bien')
                    mbox.exec()

                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText(query.lastError().text()+'Error baja Driver')
                    mbox.exec()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("No existe conductor o conductor o dado de baja anteriormente")
                mbox.exec()

        except Exception as error:
            print('Error al borrar Driver', error)

    def selectDrivers(estado):
        try:
            registros = []
            if int(estado) == 0:
                query = QtSql.QSqlQuery()
                query.prepare('select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
            elif int(estado) == 1:
                query = QtSql.QSqlQuery()
                query.prepare(
                    'select codigo, apeldri, nombredri, movildri, carnet, '
                    'bajadri from drivers where bajadri is null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
            elif int(estado) == 2:
                query = QtSql.QSqlQuery()
                query.prepare(
                    'select codigo, apeldri, nombredri, movildri, carnet, bajadri '
                    'from drivers where bajadri is not null')
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                    drivers.Drivers.cargartabladri(registros)
        except Exception as error:
            print("Error SelectDrivers ", error)

    @staticmethod
    def consulta_drivers(fechaBaja):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()

            if fechaBaja == 2:
                query1.prepare("select codigo, apellidos, nombre, telefono, carnet, fechaBaja from drivers")
            elif fechaBaja == 1:
                query1.prepare(
                    "select codigo, apellidos, nombre, telefono, carnet, fechaBaja from drivers where fechaBaja is null")
            elif fechaBaja == 0:
                query1.prepare(
                    "select codigo, apellidos, nombre, telefono, carnet, fechaBaja from drivers where fechaBaja is not null")

            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print('error mostrar resultados', error)

    def selectDriversTodos(self):
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
            print("error devolver todos los drivers", error)
