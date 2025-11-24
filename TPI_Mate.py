# --------------------------------------------------------------
# TRABAJO INTEGRADOR: MATEMÁTICAS Y PROGRAMACIÓN
# TEMA: Simulador de Compuertas Lógicas
# ALUMNO: Diaz Juan José
#
# DESCRIPCIÓN:
# Este programa permite simular el comportamiento de las compuertas
# lógicas fundamentales (AND, OR, NOT, XOR) utilizando Álgebra de Boole.
# Incluye representaciones gráficas en ASCII y validación de entradas.
# --------------------------------------------------------------

import os

def limpiar_pantalla():
    # Para Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Para macOS y Linux (el nombre es 'posix')
    else:
        _ = os.system('clear')

def pedir_valor(mensaje):
    """
    Pide al usuario un valor binario (0 o 1).
    Si el usuario ingresa algo inválido, se vuelve a pedir hasta que sea correcto.
    """
    while True:
        valor = input(mensaje)
        # Validamos si el valor es exactamente "0" o "1"
        if valor in ("0", "1"):
            return int(valor)
        else:
            print("❌ Error: Debes ingresar 0 o 1 (Sistema Binario).")

def calcular_and(a, b):
    """Simula compuerta AND: Salida 1 solo si ambas entradas son 1."""
    return a and b

def calcular_or(a, b):
    """Simula compuerta OR: Salida 1 si al menos una entrada es 1."""
    return a or b

def calcular_not(a):
    """Simula compuerta NOT: Invierte el valor de entrada."""
    return not a

def calcular_xor(a, b):
    """Simula compuerta XOR: Salida 1 si las entradas son diferentes."""
    # Equivalente lógico: (A and not B) or (not A and B)
    return (a and not b) or (not a and b)

def mostrar_menu():
    """Muestra el menú interactivo en consola."""
    print("\n" + "═" * 50)
    print("🧠   SIMULADOR DE ÁLGEBRA DE BOOLE   🧠")
    print("═" * 50)
    print("1. AND  (Conjunción - A ∧ B)")
    print("2. OR   (Disyunción - A ∨ B)")
    print("3. NOT  (Negación - ¬A)")
    print("4. XOR  (O Exclusivo - A ⊕ B)")
    print("5. Salir")
    print("═" * 50)
    return input("Elige una opción (1-5): ")

def obtener_datos_operacion(opcion):
    """
    Maneja la lógica de pedir datos según la compuerta elegida.
    Optimiza el código evitando repetición de inputs.
    """
    operaciones = {
        '1': {'nombre': 'AND', 'entradas': 2, 'funcion': calcular_and},
        '2': {'nombre': 'OR', 'entradas': 2, 'funcion': calcular_or},
        '3': {'nombre': 'NOT', 'entradas': 1, 'funcion': calcular_not},
        '4': {'nombre': 'XOR', 'entradas': 2, 'funcion': calcular_xor}
    }
    
    if opcion not in operaciones:
        return None, None, None, None
    
    info = operaciones[opcion]
    
    # Lógica para pedir 1 o 2 valores según corresponda
    if info['entradas'] == 1:
        a = pedir_valor("Ingresa el valor (0 o 1): ")
        b = None
        resultado = info['funcion'](a)
    else:
        a = pedir_valor("Ingresa el primer valor (0 o 1): ")
        b = pedir_valor("Ingresa el segundo valor (0 o 1): ")
        resultado = info['funcion'](a, b)
    
    return info['nombre'], resultado, a, b

def mostrar_arte_ascii(operacion, a, b, resultado):
    """
    Dibuja la compuerta lógica en la consola para visualización educativa.
    """
    print("\n" + "🎨 ESQUEMA LÓGICO:".center(50, "─"))
    res_int = int(resultado) # Convertir True/False a 1/0 para visualización
    
    if operacion == "AND":
        print(f"""
       ┌─────┐
    {a} ─┤     │
       │ AND ├── {res_int}
    {b} ─┤     │
       └─────┘
        """)
        
    elif operacion == "OR":
        print(f"""
       ┌─────┐
    {a} ─┤     │
       │ OR  ├── {res_int}
    {b} ─┤     │
       └─────┘
        """)
        
    elif operacion == "NOT":
        print(f"""
       ┌─────┐
       │     │
    {a} ─┤ NOT ├── {res_int}
       │     │
       └─────┘
        """)
        
    elif operacion == "XOR":
        print(f"""
       ┌─────┐
    {a} ─┤     │
       │ XOR ├── {res_int}
    {b} ─┤     │
       └─────┘
        """)

def mostrar_resultado_detallado(operacion, a, b, resultado):
    """Imprime el resultado final combinando matemáticas y programación."""
    limpiar_pantalla()
    print("\n" + "📊 RESULTADO MATEMÁTICO:".center(50, "═"))
    res_int = int(resultado)
    
    if operacion == "NOT":
        print(f"   Expresión: ¬{a} = {res_int}")
    else:
        print(f"   Expresión: {a} {operacion} {b} = {res_int}")
    
    mostrar_arte_ascii(operacion, a, b, resultado)
    print("-" * 50)

# --------------------------------------------------------------
# FUNCIÓN PRINCIPAL (Entry Point)
# --------------------------------------------------------------

def main():
    limpiar_pantalla()
    print("🚀 INICIANDO SISTEMA DE LÓGICA DIGITAL...")
    
    while True:
        opcion = mostrar_menu()

        if opcion == "5":
            print("\n👋 Fin de la simulación.")
            break
        
        nombre_op, resultado, a, b = obtener_datos_operacion(opcion)
        
        if nombre_op is None:
            limpiar_pantalla()
            print("❌ Opción inválida. Intenta nuevamente.")
            continue
        
        mostrar_resultado_detallado(nombre_op, a, b, resultado)
        input("\n⏎ Presiona Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()