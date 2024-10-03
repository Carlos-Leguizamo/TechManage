# TechManage

**TechManage**  es un sistema centralizado de gestión de inventario de computadoras que facilita el control y la
planificación de mantenimientos. Nuestro software le proporciona una plataforma integral para monitorizar el
estado de sus equipos, asegurando que cada computadora esté en óptimas condiciones y lista para su uso. 

***¡Bienvenidos a TechManage! Optimiza y cuida tu inventario tecnológico.***






*** 

![Interfaz](/img_readme/Readme.png "Inferfaz Cabaña")

---

## Pre-requisito

#### Instalar Git

+ Distribuciones Debian
~~~
sudo apt-get install git 
~~~
  
+ Windows

~~~
https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe
~~~   

#### Instalar python
~~~
https://www.python.org/downloads/
~~~

#### Instalar Workbench
~~~
https://dev.mysql.com/downloads/workbench/
~~~

## Instalación

1. Abrir Visual Studio Code.
   
2. Clonar repositorio.
   
~~~
git clone https://github.com/Carlos-Leguizamo/TechManage.git
~~~

3. Creación del entorno virtual en python
~~~
python -m venv env
~~~

4. Activación del entorno virtual
~~~
env\Scripts\activate
~~~

5. Instalación de las dependencias
~~~
pip install -r requirements.txt
~~~

6. Configuración de la base de datos
 
En settings.py se pueden encontrar las credenciales de la base de datos

![DB](img/settings_db.png "DB")

Existen varias herramientas para manejar la base de datos ya sea local o remota:

+ Xampp
+ Laragon
+ Workbench
+ Clever cloud
+ Railway

---

7. Correr las migraciones, para cargar las tablas a la base de datos.
~~~   
python manage.py migrate
~~~


8. Ejecutar el servidor

~~~
python manage.py runserver
~~~

## :earth_africa: Lenguajes:

[![Lenguajes](https://skillicons.dev/icons?i=html,css,python,mysql)](https://skillicons.dev)

## :computer: Framework:

[![Lenguajes](https://skillicons.dev/icons?i=bootstrap,django)](https://skillicons.dev)

## :gear: Herramientas:

[<img alt="github" width="50px" src="https://raw.githubusercontent.com/coderjojo/coderjojo/master/img/github.svg"/>](https://github.com)
[<img alt="git" width="50px" src="https://iconape.com/wp-content/png_logo_vector/git-icon.png"/>](https://git-scm.com/)
[<img alt="clevercloud" width="50px" src="img/clever-cloud.png"/>](https://clever-cloud.com)
[<img alt="workbench" width="60px" src="img/workbench.png"/>](https://clever-cloud.com)
[<img alt="fontawesome" width="50px" src="img/font-awesome.svg"/>](https://www.mysql.com/products/workbench/)

---

### Autores

[John Camilo Garzon](https://github.com/JohnCamiloGarzonVargas) :wave:

[Carlos Leguizamo](https://github.com/Carlos-Leguizamo) :wave:

[Santiago Firigua](https://github.com/SFirigua) :wave:

---
> [!NOTE]
> Muchas gracias por prestar atención.


> [!IMPORTANT]
> Sacamos iconos para el readme de este repositorio.  
> [Repositorio Icon](https://github.com/tandpfun/skill-icons)