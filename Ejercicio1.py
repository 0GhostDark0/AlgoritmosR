# Solicitar valores de corriente y voltaje al usuario
corriente = float(input("Ingrese el valor de corriente (A): "))
voltaje = float(input("Ingrese el valor de voltaje (V): "))

# Calcular la potencia
potencia = corriente * voltaje

# Mostrar el resultado
print(f"La potencia que consume el circuito es: {potencia:.2f} W")