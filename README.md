## Proyecto-Integrador---To-Do-App-Django
Este proyecto es una aplicación web simple para gestionar listas de tareas. Permite a los usuarios crear, leer, actualizar y eliminar tareas, así como también iniciar sesión y registrarse para utilizar la aplicación.

# Características
- Iniciar sesión y registrarse como usuario.
- Ver una lista de tareas.
- Crear nuevas tareas.
- Editar tareas existentes.
- Marcar tareas como completadas.
- Eliminar tareas.
- Cerrar sesión.

# Requisitos
- Django
- Python 3.12.2
- Django Rest Framework

# Instalación
- Clona este repositorio a tu máquina local.
- Crea un entorno virtual para el proyecto. Puedes hacerlo con el siguiente comando: python3 -m venv myenv. myenv es el nombre del proyecto, puedes poner el que desees.
- Activa el entorno virtual. Dependiendo de tu sistema operativo, el comando puede variar: para Windows *myenv\Scripts\activate*, para MacOS y Linux *source myenv/bin/activate*
- Instala django y django Rest Framework con *pip install django django restframework*
- Realiza las migraciones de la base de datos con *python manage.py migrate*
- Ejecuta el servidor de desarrollo con *python manage.py runserver*

# Uso
- Una vez hayas ejecutado el servidor de desarrollo, accede a la direccion que se te proporciona en la terminal.
- Si ya tienes una cuenta, inicia sesión con tu nombre de usuario y contraseña. Si no, haz clic en el boton "Registrarse" para crear una nueva cuenta.
- Después de iniciar sesión, serás redirigido automáticamente a la lista de tareas. Aquí podrás ver todas las tareas asociadas a tu cuenta.
- Las tareas se mostrarán en una lista, con información como el título, la descripción, el estado y la fecha de creación.
- Para crear una nueva tarea, haz clic en el enlace "Crear nueva tarea" en la parte inferior de la página de la lista de tareas. Esto te llevará a un formulario donde puedes ingresar los detalles de la nueva tarea, como el título, la descripción y el estado.
- Para editar una tarea existente, haz clic en el enlace "Editar" junto a la tarea que deseas modificar en la lista de tareas.
- Esto te llevará al formulario de edición de la tarea, donde puedes actualizar los detalles según sea necesario.
- Puedes marcar una tarea como completada haciendo clic en el botón correspondiente junto a la tarea en la lista de tareas.
- Para eliminar una tarea, haz clic en el enlace "Eliminar" junto a la tarea que deseas eliminar en la lista de tareas.
- Esto mostrará una confirmación y, si estás seguro, podrás eliminar la tarea permanentemente.
- Cuando hayas terminado de trabajar con la aplicación, puedes cerrar sesión haciendo clic en el enlace "Cerrar sesión" en la esquina superior derecha de la página.

# Créditos
Este proyecto fue creado por Randy Benjamin Cuevas Sanchez 


