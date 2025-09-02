# Proyecto Urban Grocers qa_project-Urban-Grocers-app-es
-"Este proyecto contiene pruebas automatizadas para la API de Urban Grocers,  para la funcionalidad de creación de kits de productos"]
- Documentación <the url of the launched server>/docs/
- # Tecnologías y técnicas utilizadas
- Python
- Pytest
- Requests
- ## Instrucciones para ejecutar las pruebas

### Prerrequisitos
- Python 3.x instalado
- Librerías: requests, pytest

### Pasos para ejecutar
1. Clona el repositorio
2. Instala las dependencias: `pip install requests pytest`
3. Actualiza la URL del servidor en `configuration.py`
4. Ejecuta las pruebas: `pytest create_kit_name_kit_test.py`

### Estructura de archivos
- `configuration.py` - Configuración de URLs
- `data.py` - Datos de prueba
- `sender_stand_request.py` - Funciones de solicitudes
- `create_kit_name_kit_test.py` - Pruebas principales
