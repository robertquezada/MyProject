# Sistema de ventas de artículos de camping en Python con recomendaciones

# Lista de artículos disponibles
articulos = {
    "tienda": {"nombre": "Tienda de campaña", "precio": 50},
    "saco": {"nombre": "Saco de dormir", "precio": 30},
    "linterna": {"nombre": "Linterna", "precio": 15},
    "estufa": {"nombre": "Estufa portátil", "precio": 25}
}

# Carrito de compras y compras previas
carrito = []
compras_previas = []

def mostrar_articulos():
    print("Artículos disponibles:")
    for clave, valor in articulos.items():
        print(f"{clave.capitalize()}: {valor['nombre']} - ${valor['precio']}")

def agregar_al_carrito():
    while True:
        articulo = input("Ingrese el nombre del artículo que desea agregar al carrito (o 'salir' para terminar): ").lower()
        if articulo == 'salir':
            break
        if articulo in articulos:
            carrito.append(articulos[articulo])
            print(f"Se ha agregado {articulos[articulo]['nombre']} al carrito.")
            compras_previas.append(articulos[articulo])
        else:
            print("Artículo no encontrado.")

def ver_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("Contenido del carrito:")
        total = 0
        for item in carrito:
            print(f"{item['nombre']} - ${item['precio']}")
            total += item['precio']
        print(f"Total: ${total}")

def finalizar_compra():
    if not carrito:
        print("El carrito está vacío. No se puede finalizar la compra.")
    else:
        ver_carrito()
        print("Gracias por su compra. ¡Que disfrute su camping!")
        carrito.clear()  # Vaciar el carrito después de la compra

def recomendar_articulos():
    if not compras_previas:
        print("No hay compras previas para hacer recomendaciones.")
        return
    
    recomendaciones = set()
    print("\nBasado en tus compras previas, podrías estar interesado en:")
    for articulo in compras_previas:
        if articulo['nombre'] == "Tienda de campaña":
            recomendaciones.add("Saco de dormir")
            recomendaciones.add("Linterna")
        elif articulo['nombre'] == "Saco de dormir":
            recomendaciones.add("Tienda de campaña")
            recomendaciones.add("Estufa portátil")
        elif articulo['nombre'] == "Linterna":
            recomendaciones.add("Tienda de campaña")
            recomendaciones.add("Saco de dormir")
        elif articulo['nombre'] == "Estufa portátil":
            recomendaciones.add("Saco de dormir")
            recomendaciones.add("Tienda de campaña")
    
    # Mostrar recomendaciones sin duplicados
    for recomendacion in recomendaciones:
        print(f"- {recomendacion}")

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Ver artículos disponibles")
        print("2. Agregar artículo al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Ver recomendaciones")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            mostrar_articulos()
        elif opcion == '2':
            agregar_al_carrito()
        elif opcion == '3':
            ver_carrito()
        elif opcion == '4':
            finalizar_compra()
        elif opcion == '5':
            recomendar_articulos()
        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()




