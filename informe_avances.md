# Informe de Avances — Restaurante "El Sabor"

**Proyecto:** Sistema de Gestión de Restaurante  
**Fecha de entrega:** 29 de abril de 2026  
**Autores:** Biel y Nahuel  
**Repositorio:** https://github.com/Nahuelrz/proyecto_python

---

## 1. Descripción del Proyecto

El proyecto consiste en un sistema de gestión para el restaurante ficticio "El Sabor", desarrollado en Python. El sistema permite administrar clientes, reservas, el menú y los pedidos del restaurante mediante una interfaz de consola interactiva.

---

## 2. Tareas Desarrolladas hasta la Fecha

### 2.1 Estructura del proyecto
Se definió y creó la estructura modular del proyecto, dividiendo la lógica en múltiples archivos `.py` para facilitar el mantenimiento y la legibilidad del código.

```
proyecto_python/
├── main.py           # Punto de entrada principal
├── cliente.py        # Clase Cliente
├── restaurante.py    # Clase Restaurante (lógica principal)
├── reserva.py        # Clase Reserva
├── reservas.py       # Módulo de gestión de reservas
├── menu.py           # Módulo de gestión del menú
├── pedidos.py        # Módulo de gestión de pedidos
├── utilidades.py     # Funciones auxiliares y validaciones
├── data/
│   ├── reservas.json
│   ├── menu.json
│   └── pedidos.json
└── README.md
```

### 2.2 Clase `Cliente`
Se implementó la clase `Cliente` en `cliente.py` con los atributos `nombre`, `telefono` y `email`. Incluye el método `__str__` para mostrar la información de forma legible.

### 2.3 Clase `Reserva`
Se implementó la clase `Reserva` en `reserva.py`, que almacena los datos de una reserva: cliente asociado, fecha, hora, número de personas y mesa (opcional).

### 2.4 Clase `Restaurante`
Se implementó la clase principal `Restaurante` en `restaurante.py`, que gestiona las listas de clientes y reservas. Incluye métodos para:
- Agregar y buscar clientes
- Crear, mostrar y cancelar reservas

### 2.5 Menú principal (`main.py`)
Se desarrolló el flujo interactivo del programa con un menú en consola que permite al usuario navegar por las distintas funciones del sistema mediante `input()`.

### 2.6 Configuración del repositorio
Se inicializó el repositorio Git y se realizó la conexión con GitHub. Se subieron todos los archivos al repositorio remoto correctamente.

---

## 3. Decisiones Tomadas

| Decisión | Justificación |
|---|---|
| Usar Programación Orientada a Objetos (POO) | Permite representar de forma natural las entidades del restaurante (clientes, reservas) y facilita la escalabilidad del proyecto. |
| Dividir el código en módulos separados | Mejora la organización, evita archivos muy largos y facilita trabajar en equipo sin conflictos. |
| Persistencia con archivos JSON | Es una solución sencilla que no requiere instalar bases de datos externas, adecuada para el alcance del proyecto. |
| Interfaz por consola (sin GUI) | Reduce la complejidad técnica y permite centrarse en la lógica del programa, que es el objetivo principal del curso. |

---

## 4. Problemas Encontrados y Soluciones

### Problema 1: Importaciones circulares entre módulos
**Descripción:** Al importar `Cliente` desde `restaurante.py` y al mismo tiempo intentar importar algo de `restaurante.py` en otro módulo, Python lanzaba un error de importación circular (`ImportError`).  
**Solución:** Se reorganizó la estructura de imports para que el flujo de dependencias fuera unidireccional: `main.py` → `restaurante.py` → `cliente.py` / `reserva.py`, sin que los módulos de nivel inferior importen módulos de nivel superior.

---

### Problema 2: Errores al ingresar datos no válidos por consola
**Descripción:** Al solicitar el número de personas para una reserva, si el usuario ingresaba letras en lugar de un número, el programa se cerraba con un `ValueError`.  
**Solución:** Se añadieron bloques `try/except` alrededor de todas las conversiones de tipo (`int()`, `float()`), mostrando un mensaje de error amigable y permitiendo al usuario volver a intentarlo.

---

### Problema 3: Pérdida de datos al cerrar el programa
**Descripción:** Los clientes y reservas creados durante la ejecución se perdían al cerrar el programa, ya que se almacenaban únicamente en memoria (listas de Python).  
**Solución:** Se planificó la persistencia de datos mediante archivos JSON en la carpeta `data/`. Los módulos `reservas.py`, `menu.py` y `pedidos.py` incluirán funciones de carga y guardado automático. Esta funcionalidad está en desarrollo.

---

### Problema 4: Conflictos de nombres entre archivos
**Descripción:** Durante el desarrollo, existía un módulo llamado `reserva.py` (clase) y otro `reservas.py` (gestión). En algunos imports se confundían los nombres, generando errores difíciles de rastrear.  
**Solución:** Se estableció una convención clara: los archivos con nombre en singular (`reserva.py`, `cliente.py`) contienen las **clases**, mientras que los archivos en plural (`reservas.py`, `pedidos.py`) contienen las **funciones de gestión** de cada módulo.

---

### Problema 5: Coordinación del trabajo en equipo con Git
**Descripción:** Al trabajar ambos integrantes sobre los mismos archivos, se produjeron conflictos de merge en Git que impedían hacer `push` correctamente.  
**Solución:** Se acordó dividir las responsabilidades: cada integrante trabaja principalmente sobre módulos distintos. Antes de hacer `push`, se realiza siempre un `git pull` para integrar los cambios del otro y resolver conflictos localmente.

---

## 5. Estado Actual del Proyecto

| Módulo | Estado |
|---|---|
| `cliente.py` | Completado |
| `reserva.py` | Completado |
| `restaurante.py` | Completado |
| `main.py` | Completado |
| `reservas.py` | En desarrollo |
| `menu.py` | En desarrollo |
| `pedidos.py` | En desarrollo |
| `utilidades.py` | En desarrollo |
| Persistencia JSON | En desarrollo |

---

## 6. Próximos Pasos

- Implementar la lógica de gestión del menú (`menu.py`) con carga y guardado en JSON.
- Implementar la toma de pedidos (`pedidos.py`) y la generación de tickets.
- Desarrollar las funciones auxiliares en `utilidades.py` (validación de fechas, horas y entradas del usuario).
- Integrar la persistencia JSON en todos los módulos.
- Realizar pruebas completas del flujo principal del sistema.

---

## 7. Evidencias

> A continuación se adjuntan capturas de pantalla del entorno de desarrollo y del funcionamiento del programa.

**Captura 1 — Estructura del proyecto en VS Code:**  
*(adjuntar captura)*

**Captura 2 — Ejecución del menú principal en consola:**  
*(adjuntar captura)*

**Captura 3 — Creación de un cliente y una reserva:**  
*(adjuntar captura)*

**Captura 4 — Repositorio en GitHub con los commits realizados:**  
*(adjuntar captura)*

---

## 8. Enlace al Repositorio

[https://github.com/Nahuelrz/proyecto_python](https://github.com/Nahuelrz/proyecto_python)
