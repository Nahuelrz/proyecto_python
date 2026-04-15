from restaurante import Restaurante


def mostrar_menu():
    print("\n╔════════════════════════════════════════╗")
    print("║   Sistema de Gestión de Restaurante    ║")
    print("╠════════════════════════════════════════╣")
    print("║  1. Agregar cliente                    ║")
    print("║  2. Mostrar clientes                   ║")
    print("║  3. Crear reserva                      ║")
    print("║  4. Mostrar reservas                   ║")
    print("║  5. Cancelar reserva                   ║")
    print("║  6. Salir                              ║")
    print("╚════════════════════════════════════════╝")


def main():
    resto = Restaurante("La Buena Mesa")

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del cliente: ").strip()
            telefono = input("Teléfono: ").strip()
            email = input("Email (opcional, Enter para omitir): ").strip()
            resto.agregar_cliente(nombre, telefono, email)

        elif opcion == "2":
            resto.mostrar_clientes()

        elif opcion == "3":
            nombre = input("Nombre del cliente (debe estar registrado): ").strip()
            fecha = input("Fecha de la reserva (DD/MM/AAAA): ").strip()
            hora = input("Hora de la reserva (HH:MM): ").strip()
            try:
                personas = int(input("Número de personas: ").strip())
            except ValueError:
                print("✘ Número de personas no válido.")
                continue
            mesa = input("Número de mesa (opcional, Enter para omitir): ").strip()
            resto.crear_reserva(nombre, fecha, hora, personas, mesa or None)

        elif opcion == "4":
            resto.mostrar_reservas()

        elif opcion == "5":
            resto.mostrar_reservas()
            if resto.reservas:
                try:
                    idx = int(input("Número de reserva a cancelar: ").strip()) - 1
                    resto.cancelar_reserva(idx)
                except ValueError:
                    print("✘ Entrada no válida.")

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("✘ Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
