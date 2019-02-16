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

## Desarrollo

### client-web

Para trabajar con este proyecto se requiere instalar [Nodejs](https://nodejs.org/) y *npm*. En este proyecto se usó [Yarn](https://yarnpkg.com/).

El path *client-web* contiene el proyecto web (css, javascript, fuentes, etc.) para la aplicación. Utiliza *webpack* para generar los paquetes estáticos.

La forma habitual de trabajar es ejecutando los siguientes comandos dentro del directorio *project/client-web/*:
```bash
# Instalar las dependencias
yarn install

# Generar los archivos estáticos
yarn run build:dev
```

### server-app

La aplicación fue desarrollada con (Python 3)[https://www.python.org/] y [Django](https://www.djangoproject.com/).

Dentro del directorio *project/server-app/* la forma habitual de trabajar en desarrollo es con los siguientes comandos:
```bash
# Instalar dependencias
pip install -r requirements.txt

# Generar la base de datos
python manager.py makemigrations

# Iniciar el servidor
python manager.py runserver
```

## Desarrollo

Para el despliegue en producción se ejecuta:
```bash
# Generar los archivos estáticos para el ambiente productivo
yarn run build
```

Para hacer referencia desde los templates de Django a los recursos web creados, se ejecuta:
```bash
# Sobreescribir los partial existentes en server-app/templates/_css.html y server-app/templates/_js.html
python scripts/django-wire.py
```
