# TuPrimeraPagina+Espindola

Proyecto Django de ejemplo para la consigna: herencia de plantillas, 3 modelos, formularios para insertar datos y formulario de búsqueda.

## Cómo ejecutar

1. Crear un entorno virtual (recomendado) y activarlo:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate    # Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar migraciones:
```bash
python manage.py migrate
```

4. Crear usuario admin (opcional):
```bash
python manage.py createsuperuser
```

5. Ejecutar el servidor:
```bash
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

## Rutas principales (app `blog`)
- `/` - Home
- `/autor/nuevo/` - Formulario para crear Autor
- `/categoria/nueva/` - Formulario para crear Categoria
- `/post/nuevo/` - Formulario para crear Post
- `/buscar/` - Formulario de búsqueda de Posts por título
