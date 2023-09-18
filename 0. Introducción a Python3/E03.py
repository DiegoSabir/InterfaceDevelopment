"""
Dados unha cifra en segundos fai a transformación en horas, minutos e segundos. 
"""
seconds = int(input("Enter a seconds quantity: "))

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(f"{hours} Hours, {minutes} Minutes, {seconds} Seconds")

"""
Repite o exercicio de forma inversa, dada unha cifra en horas, minutos e segundos,
transforma en segundos.
"""
hours2 = int(input("Enter a hours quantity: "))
minutes2 = int(input("Enter a minutes quantity: "))
seconds2 = int(input("Enter a seconds quantity: "))

totalSeconds = hours2 * 3600 + minutes2 * 60 + seconds2

print(f"Total: {totalSeconds} Seconds")