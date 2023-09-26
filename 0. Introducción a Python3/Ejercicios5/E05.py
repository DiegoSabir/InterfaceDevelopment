"""
Crear una clase base llamada Vehiculo, que tiene atributos comunes como marca, modelo, año y precio. 
Luego, creamos dos clases derivadas, Coche y Motocicleta, que heredan de la clase base Vehiculo y 
agregan atributos adicionales específicos para cada tipo de vehículo (puertas y cilindrada).
Cada clase derivada tiene su propio método obtener_informacion, que llama al método 
de la clase base obtener_informacion utilizando super() y luego agrega la información 
específica del tipo de vehículo. 
Esto demuestra cómo se puede utilizar la herencia para reutilizar y extender funcionalidad en 
una jerarquía de clases.
"""