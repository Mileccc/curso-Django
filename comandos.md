# COMANDOS PRINCIPALES
___
### 1. Crear proyecto
```py
django-admin startproject [nombre_proyecto]
```
___
### 2. Crear app
```py
python manage.py startapp [nombre_app]
```
___
### 3. Crear migración
```python
python manage.py migrate
```
___
### 4. Levantar servidor
```python
python manage.py runserver
```

### 5. Crear env
1. Crear archivo ``.env`` en la raiz del proyecto

2. Añadir al .env los datos criticos como:
```json
SECRET_KEY="codigo"
DEBUG=True
DATABASE_NAME=db.sqlite3
```
3. Instalar environ:
```bash
pip install django-environ
```
4. Modificar settings.py para usar django-environ:
```python
import environ
import os

# Inicializar django-environ
env = environ.Env(
    # Establecer valores predeterminados
    DEBUG=(bool, False)
)

# Leer el archivo .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Configuraciones de Django
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')

# Configuración de la base de datos
DATABASES = {
    'default': env.db(),
}

# Otras configuraciones...

```
5. Actualizar .gitignore:
```txt
# Django
*.log
*.pot
*.pyc
__pycache__/
db.sqlite3
media

# Environment variables
.env

# macOS
.DS_Store

# Python
*.py[cod]
*$py.class

# Environments
venv/
env/
ENV/
venv.bak/
venv.bak/

# Pytest
.coverage
.tox/
.cache

# Migrations
*/migrations/*

# Documentation
docs/_build/

# MyPy
.mypy_cache/
.dmypy.json

# PyCharm
.idea/

# VS Code
.vscode/
```
___

### 6. 