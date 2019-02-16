# Proyecto de prueba para HITSBOOK
Este proyecto es un administrador de tareas desarrollado con:
* Python 3
* Django 2

## Directorios
Para este proyecto se agregaron algunos paths para lograr integrar el desarrollo en el frontend. Estos paths son:

* **data**: path para guardar la base de datos sqlite.
* **static**: path donde se almacenan los elementos estáticos generados por *client-web*.
* **client-web**: path del proyecto web
* **server-app**: aplicación django.

## client-web
El path *client-web* contiene el proyecto web (css, javascript, fuentes, etc.) para la aplicación. Utiliza *webpack* para generar los paquetes estáticos.

**Desarrollo**
Para el desarrollo la forma de operar es con la ejecución de:
```bash
yarn run build:dev
```

**Production**
Para el despliegue en producción se ejecuta:
```bash
yarn run build
```

Para hacer referencia desde los templates de Django a los recursos web creados, se ejecuta:
```bash
# Sobreescribir los partial existentes en server-app/templates/_css.html y server-app/templates/_js.html
python scripts/django-wire.py
```
