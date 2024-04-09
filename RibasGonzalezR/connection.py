from PyQt6 import QtWidgets, QtSql, QtGui
from datetime import date, datetime

import customer
import var


class Connection():
    def connection(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print('connection error')
            return False

        else:
            print('database connected')
            return True



    def oneCustomer(codigo):
        """

        Recupera los datos de un conductor específico según su código.

        :param codigo: Código único del conductor.
        :return: Una lista con los detalles del conductor recuperado.

        """
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT * FROM customers WHERE codigo=:codigo')
            query.bindValue(':codigo', int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))

            return registro

        except Exception as error:
            print('error oneDriver', error)