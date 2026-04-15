class Cliente:
    """Clase que representa un cliente del restaurante."""

    def __init__(self, nombre, telefono, email=""):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        info = f"Cliente: {self.nombre} | Teléfono: {self.telefono}"
        if self.email:
            info += f" | Email: {self.email}"
        return info
