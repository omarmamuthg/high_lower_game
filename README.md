# Juego de Comparación de Seguidores

Este es un juego interactivo desarrollado en Python donde el objetivo es comparar dos perfiles y adivinar cuál tiene más seguidores. El juego utiliza datos predefinidos y genera una interfaz de línea de comandos para la interacción del usuario.

## Características

- **Selección Aleatoria de Datos**: Utiliza el módulo `random` para seleccionar datos aleatorios de una lista predefinida.
- **Interfaz Interactiva**: Proporciona una experiencia de usuario amigable en la línea de comandos.
- **Contador de Puntajes**: Lleva un registro del puntaje del jugador a medida que avanza en el juego.
- **Arte ASCII**: Utiliza el módulo `art` para mejorar la presentación visual del juego.

## Cómo Funciona

1. **Inicialización del Juego**:
    - El juego inicia mostrando un mensaje de bienvenida y el logo del juego.

2. **Selección de Datos**:
    - Selecciona datos aleatorios de una lista predefinida en `data.py`.
    - Verifica que los datos seleccionados no se repitan durante la sesión del juego.

3. **Comparación de Perfiles**:
    - Muestra dos perfiles con su número de seguidores, descripción y país.
    - El jugador debe adivinar cuál de los dos perfiles tiene más seguidores.

4. **Actualización del Puntaje**:
    - Si el jugador acierta, se incrementa el puntaje y se actualiza la lista de perfiles.
    - Si el jugador falla, se muestra el puntaje final y el juego reinicia.

## Instrucciones de Uso

1. Clona el repositorio a tu máquina local.
2. Asegúrate de tener Python instalado.
3. Ejecuta el script principal.
4. Sigue las instrucciones en la línea de comandos para jugar.
