# Restaurante "La Buena Mesa" - Sistema de Gestión

Sistema de gestión integral para restaurante desarrollado en Python.

## Descripción del Proyecto

Este proyecto simula el sistema de gestión de un restaurante llamado "El Sabor". Permite administrar reservas, gestionar el menú, tomar pedidos y generar tickets, ofreciendo una experiencia completa tanto para el personal del restaurante como para los clientes.

## Estructura del proyecto

```
proyecto_python/
│
├── main.py          # Punto de entrada principal
├── reservas.py      # Módulo de gestión de reservas
├── menu.py          # Módulo de gestión del menú
├── pedidos.py       # Módulo de gestión de pedidos
├── utilidades.py    # Funciones auxiliares y validaciones
├── cliente.py       # Modulo gestion del cliente
├── restaurante.py   # Modulo restaurante 
│
├── data/
│   ├── reservas.json  # Datos de reservas
│   ├── menu.json      # Datos del menú
│   └── pedidos.json   # Datos de pedidos
│
└── README.md        # Este archivo
```

## Funcionalidades

| Módulo       | Funcionalidad    | Descripción                                                        |
|--------------|------------------|--------------------------------------------------------------------|
| Reservas     | Crear, ver, cancelar | Gestión completa de reservas con fecha, hora y número de comensales |
| Menú         | CRUD de platos   | Añadir, modificar, eliminar y visualizar platos por categorías     |
| Pedidos      | Toma de pedidos  | Asociar pedidos a mesas, calcular totales y generar tickets        |
| Persistencia | Archivos JSON    | Los datos se guardan automáticamente entre sesiones                |

## Tecnologías y Conceptos Utilizados

### Contenido del curso aplicado

- Variables y tipos de datos: strings, integers, floats, booleanos
- Estructuras condicionales: if, elif, else
- Bucles: for y while
- Estructuras de datos: listas y diccionarios
- Funciones: múltiples funciones organizadas por módulo
- Interacción con usuario: uso extensivo de `input()`

### Investigación adicional

- Manejo de archivos JSON: persistencia de datos entre ejecuciones
- Módulo datetime: validación y formateo de fechas/horas
- Organización modular: código dividido en múltiples archivos `.py`
- Validaciones avanzadas: control de errores y entradas del usuario

## Colaboradores
- Biel Ramos Rifà
- Nahuel Ramírez Murieda