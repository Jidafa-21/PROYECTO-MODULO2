# 📚 Sistema de Control de Biblioteca

Aplicación web para la gestión del catálogo, ejemplares y préstamos de una biblioteca institucional, desarrollada con **Django**.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Django](https://img.shields.io/badge/Django-6.0.6-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/DB-SQLite-lightgrey)

---

## Descripción

El sistema permite administrar el catálogo de libros y sus ejemplares físicos, así como gestionar el ciclo completo de préstamos: solicitud por parte del usuario, aprobación o rechazo por parte del administrador, y registro de devolución. Cuenta con dos roles de usuario (**administrador** y **usuario estándar**), cada uno con permisos y vistas diferenciadas.

## Características

- 🔐 Registro, inicio y cierre de sesión de usuarios
- 👤 Perfiles de usuario con rol, teléfono, dirección y estado
- 📖 Catálogo de libros con búsqueda por título
- 🗂️ Gestión de ejemplares físicos (ubicación y estado: disponible, prestado, dañado, baja)
- 📩 Solicitud de préstamo por parte del usuario
- ✅ Aprobación / rechazo de solicitudes por parte del administrador
- 🔄 Registro de préstamos directos y devoluciones, con actualización automática del estado del ejemplar

## Tecnologías

- **Backend:** Python 3, Django 6.0.6
- **Base de datos:** SQLite
- **Frontend:** HTML + CSS (plantillas de Django)

## Requisitos previos

- Python 3.11 o superior
- pip

## Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone git@github.com:Jidafa-21/PROYECTO-MODULO2.git
cd PROYECTO-MODULO2

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
source venv/Scripts/activate      # Windows (Git Bash)
# venv\Scripts\activate           # Windows (CMD/PowerShell)
# source venv/bin/activate        # macOS/Linux

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Aplicar migraciones
python manage.py migrate

# 6. Crear usuario administrador
python manage.py createsuperuser

# 7. Levantar el servidor
python manage.py runserver
```

Abrir en el navegador:

- **Aplicación:** http://127.0.0.1:8000/libros/
- **Panel de administración de Django:** http://127.0.0.1:8000/admin/

## Estructura del proyecto

```
PROYECTO-MODULO2/
├── config/         # Configuración del proyecto (settings, urls raíz)
├── core/           # App base
├── usuarios/       # Registro, login, perfiles y roles
├── libros/         # Catálogo de libros y ejemplares
├── prestamos/      # Solicitudes, préstamos y devoluciones
├── static/css/     # Estilos del proyecto
├── templates/      # Plantilla base
├── manage.py
└── requirements.txt
```

## Licencia

Proyecto académico — uso educativo.
