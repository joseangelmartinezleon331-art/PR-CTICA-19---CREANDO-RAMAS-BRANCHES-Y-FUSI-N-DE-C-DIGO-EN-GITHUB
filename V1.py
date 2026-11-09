# --- SISTEMA DE CAJA CON DESCUENTOS ---

def calcular_descuento():
    print("\n--- NUEVO CÁLCULO ---")
    
    try:
        # Solicitar datos
        precio = float(input("Precio del producto: $"))
        descuento = float(input("Porcentaje de descuento: "))
        
        # Validaciones lógicas
        if precio < 0 or descuento < 0:
            print("ERROR: El precio y el descuento no pueden ser negativos.")
            return
        elif descuento > 100:
            print("ERROR: El descuento no puede ser mayor al 100%.")
            return
            
        # Cálculos
        ahorro = precio * (descuento / 100)
        total = precio - ahorro
        
        # Imprimir resultado
        print(f"\n✅ Descuento de ${ahorro:.2f} aplicado.")
        print(f"💰 El cliente debe pagar: ${total:.2f}")
        
    except ValueError:
        # Esto atrapa el error si el usuario escribe letras
        print("❌ ERROR: Por favor, ingresa solo números.")

# --- Bucle principal del programa ---
while True:
    calcular_descuento()
    
    # Preguntar si desea continuar
    continuar = input("\n¿Calcular otro producto? (s/n): ").lower()
    if continuar != 's':
        print("Cerrando la caja registradora...")
        break
