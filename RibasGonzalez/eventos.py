import var, sys

class Eventos():
    def salir(self):
        try:
            sys.exit(0)
        except Exception as error:
            print(error, "en modulo eventos")

    @staticmethod
    def abrirCalendar(self):
        try:
            var.calendar.show()
        except Exception as error:
            print("error al abrir calendar", error)

    @staticmethod
    def acercade():
        try:
            pass
        except Exception as error:
            print("error al abrir acercade", error)