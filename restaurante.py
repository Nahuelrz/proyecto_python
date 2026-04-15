from cliente import Cliente
from reserva import Reserva


class Restaurante:
    """Clase principal que gestiona clientes y reservas del restaurante."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
        self.reservas = []

    # ── Gestión de clientes ──────────────────────────────────

    def agregar_cliente(self, nombre, telefono, email=""):
        cliente = Cliente(nombre, telefono, email)
        self.clientes.append(cliente)
        print(f"✔ Cliente '{nombre}' agregado correctamente.")
        return cliente

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        print(f"\n{'═' * 50}")
        print(f"  Clientes de {self.nombre}")
        print(f"{'═' * 50}")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"  {i}. {cliente}")
        print()

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None

    # ── Gestión de reservas ──────────────────────────────────

    def crear_reserva(self, nombre_cliente, fecha, hora, num_personas, mesa=None):
        cliente = self.buscar_cliente(nombre_cliente)
        if cliente is None:
            print(f"✘ Cliente '{nombre_cliente}' no encontrado. Regístrelo primero.")
            return None
        reserva = Reserva(cliente, fecha, hora, num_personas, mesa)
        self.reservas.append(reserva)
        print(f"✔ Reserva creada para '{nombre_cliente}' el {fecha} a las {hora}.")
        return reserva

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
            return
        print(f"\n{'═' * 60}")
        print(f"  Reservas de {self.nombre}")
        print(f"{'═' * 60}")
        for i, reserva in enumerate(self.reservas, 1):
            print(f"  {i}. {reserva}")
        print()

    def cancelar_reserva(self, indice):
        if 0 <= indice < len(self.reservas):
            eliminada = self.reservas.pop(indice)
            print(f"✔ Reserva de '{eliminada.cliente.nombre}' cancelada.")
        else:
            print("✘ Índice de reserva no válido.")
