# TechManage

**TechManage**  es un sistema centralizado de gestión de inventario de computadoras que facilita el control y la
planificación de mantenimientos. Nuestro software le proporciona una plataforma integral para monitorizar el
estado de sus equipos, asegurando que cada computadora esté en óptimas condiciones y lista para su uso. 

***¡Bienvenidos a TechManage! Optimiza y cuida tu inventario tecnológico.***

|




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

![DB](./img/settings_db.png "DB")

Existen varias herramientas para manejar la base de datos ya sea local o remota:

+ Xampp
+ Laragon
+ Workbench
+ Clever cloud
+ Railway

--- 

7. Correr el programa

~~~
python manage.py runserver
~~~

## :earth_africa: Lenguajes:

<img src="./img/html5-original.svg" alt="Html 5" width="50" height="40">
<img src="./img/python-original.svg" alt="Python" width="50" height="40">
<img src="./img/css3.svg" alt="Css 3" width="50" height="40">
<img src="./img/mysql-original-wordmark.svg" alt="Css 3" width="50" height="40">



## :computer: Framework:

![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## :gear: Herramientas de programación:

[<img alt="github" width="50px" src="https://raw.githubusercontent.com/coderjojo/coderjojo/master/img/github.svg"/>](https://github.com)
[<img alt="git" width="50px" src="https://iconape.com/wp-content/png_logo_vector/git-icon.png"/>](https://git-scm.com/)

## :wrench: Sistema operativo :

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)



Adicionalmente tiene:

* [x] Responsive Celular
* [x] Responsive Tablet
* [x] Responsive PC 

Con media query

~~~css
Responsive Celular
@media (max-width: 760px) {
}

Responsive Tablet
@media (min-width: 768px) and (max-width: 1024px) {
} 

Responsive PC
@media (min-width: 1250PX) and (max-width: 1920px) {
}
~~~



### Autores

@JohnCamiloGarzonVargas :wave:

@Carlos Leguizamo :wave:

> [!NOTE]
> Muchas gracias por prestar atención.


> [!IMPORTANT]
> Sacamos iconos para el readme de este repositorio.  
> [Repositorio Icon](https://github.com/ZooaDeV/ZooaDev/blob/main/README.md)