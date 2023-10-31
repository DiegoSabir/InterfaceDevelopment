from PyQt6 import QtWidgets, QtSql, QtCore
import var, drivers

class Conexion():
    def conexion(self = None):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')
        if not db.open():
            print("error de conexion")
            return False
        else:
            print("base de datos conectada")
            return True

    def cargaprov(self = None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProv.addItem('')
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
                mbox.exec()
            #select de los datos de conductores de la base de datos
            #drivers.Drivers.cargartabla(datosdri)
        except Exception as error:
            print("error en alta conductor", error)