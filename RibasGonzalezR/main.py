import customer
import locale
import sys
import var

from MainWindow import *
from PyQt6.QtCore import QTimer, QSize

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        """

        Inicializa la ventana principal y conecta los eventos a los widgets.

        Este método inicializa la ventana principal y establece las conexiones de eventos para los widgets
        y acciones en la interfaz de usuario.

        """
        super(Main, self).__init__()

        # Configuración de la interfaz de usuario
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        # Instanciación de objetos adicionales
        var.calendar = Calendar()