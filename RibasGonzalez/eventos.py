import var

class Eventos():
    def saludar(self):
        try:
            var.ui.lblTitulo.setText("Hola has usado el boton")
        except Exception as error:
            print(error, "es modulo eventos")