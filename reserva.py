class Reserva:
    """Clase que representa una reserva en el restaurante."""

    def __init__(self, cliente, fecha, hora, num_personas, mesa=None):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        self.num_personas = num_personas
        self.mesa = mesa

    def __str__(self):
        info = (
            f"Reserva de {self.cliente.nombre} | "
            f"Fecha: {self.fecha} | Hora: {self.hora} | "
            f"Personas: {self.num_personas}"
        )
        if self.mesa:
            info += f" | Mesa: {self.mesa}"
        return info
