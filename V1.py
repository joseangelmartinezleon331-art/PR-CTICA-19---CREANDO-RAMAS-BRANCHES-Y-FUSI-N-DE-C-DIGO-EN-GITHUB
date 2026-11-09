# --- PROGRAMA PARA CALCULAR DESCUENTOS ---

print("--- CALCULADORA DE DESCUENTOS ---")

# 1. Solicitar los datos al usuario
# Usamos float() porque los precios pueden tener decimales
precio_original = float(input("Ingresa el precio original del producto: $"))
porcentaje_descuento = float(input("Ingresa el porcentaje de descuento (ej. 15 para 15%): "))

# 2. Calcular el monto del descuento
# La fórmula es: (Precio * Porcentaje) / 100
monto_descuento = (precio_original * porcentaje_descuento) / 100

# 3. Calcular el precio final
precio_final = precio_original - monto_descuento

# 4. Mostrar los resultados en pantalla
# El :.2f sirve para redondear a 2 decimales (formato de moneda)
print("\n--- TICKET DE COMPRA ---")
print(f"Precio original:    ${precio_original:.2f}")
print(f"Descuento aplicado: -${monto_descuento:.2f} ({porcentaje_descuento}%)")
print(f"TOTAL A PAGAR:      ${precio_final:.2f}")
print("------------------------")