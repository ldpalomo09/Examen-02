# Examen-02
Examen 02 de Programacion Avanzada

Examen 02 Estudiantes: Luis Palomo, Mario Marin, Jose Redondo Configuracion del proyecto.

Herramientas e instaladores de uso en el proyecto.

IDE Python 3.8.1 https://www.filehorse.com/es/descargar-python-64/45890/

Extensions Python Linting Debugging (multi-threaded) Microsoft

Base de datos Postgrest 12 https://www.postgresql.org/download/ Como motor de base de datos, decidimos usarlo por las ventajas que este presenta.

Instalación ilimitada y gratuita: Podemos instalarlo en todos los equipos que queramos. Independientemente de la plataforma y la arquitectura que usemos, PostgreSQL está disponible para los diferentes SO, Unix, Linux y Windows, en 32 y 64 bits. Ésto hace de PostgreSQL un sistema multiplataforma y también hace que sea más rentable con instalaciones a gran escala.

Gran escalabilidad: Nos permite configurar PostgreSQL en cada equipo según el hardware. Por lo que es capaz de ajustarse al número de CPU y a la cantidad de memoria disponible de forma óptima. Con ello logramos una mayor cantidad de peticiones simultáneas a la base de datos de forma correcta.

Estabilidad y confiabilidad: Tiene más de 20 años de desarrollo activo y en constante mejora. No se han presentado nunca caídas de la base de datos. Ésto es debido a su capacidad de establecer un entorno de Alta disponibilidad y gracias a Hot-Standby, que nos permite que los clientes puedan realizar consultas de solo lectura mientras que los servidores están en modo de recuperación o espera. Así podemos hacer tareas de mantenimiento o recuperación sin bloquear completamente el sistema.

pgAdmin: Se trata de una herramienta gráfica con la que podemos administrar nuestras bases de datos de forma fácil e intuitiva. Podemos ejecutar sentencias SQL, e incluso crear copias de seguridad o realizar tareas de mantenimiento.

Estándar SQL: implementa casi todas las funcionalidades del estándar ISO/IEC 9075:2011, así pues, resulta sencillo realizar consultas e incluir scripts de otros Motores de Bases de Datos.

Potencia y Robustez: PostgreSQL cumple en su totalidad con la característica ACID Compliant. ACID es un acrónimo de Atomicity, Consistency, Isolation y Durability (Atomicidad, Consistencia, Aislamiento y Durabilidad en español). Por ello permite que las transacciones no interfieran unas con otras. Con ello se garantiza la información de las Bases de Datos y que los datos perduren en el sistema.

Extensibilidad: tenemos a nuestra disponibilidad una gran variedad de extensiones distribuidas por el grupo de desarrolladores de PostgreSQL. También por terceros o incluso nosotros mismos podemos crear nuestras propias extensiones. Éstas extensiones pueden ser lenguajes de programación, tales como, Perl, Java, Python, C++ y muchos más.

Git Bash Terminal https://git-scm.com/downloads

Pasos en el IDE, la pagina web y funcinalidad

Para dar inicio al programa es necesario crear un usuario llamado superuser, este usuario tendra acceso a las herramientas administrativoas.

superuser Uso: Asigna el equipo, cambia usuarios y borra usuarios, lista comentarios

Librerias

flask:es el micro framework minimalista, rápido y ligero que debes aprender; Django es el framework web más famoso. Flask es un framework que permite desarrollar aplicaciones web de forma sencilla, está especialmente guiado para desarrollo web fácil y rápido con Python. $ pip install Flask

Web serve: * Running on http://localhost:4000/

Por qué usar Flask? Flask es un “micro” Framework: Para desarrollar una App básica o que se quiera desarrollar de una forma ágil y rápida Flask puede ser muy conveniente, para determinadas aplicaciones no se necesitan muchas extensiones y es suficiente.

Incluye un servidor web de desarrollo: No se necesita una infraestructura con un servidor web para probar las aplicaciones sino de una manera sencilla se puede correr un servidor web para ir viendo los resultados que se van obteniendo.

Tiene un depurador y soporte integrado para pruebas unitarias: Si tenemos algún error en el código que se está construyendo se puede depurar ese error y se puede ver los valores de las variables. Además está la posibilidad de integrar pruebas unitarias.

Es compatible con Python3.

Es compatible con wsgi: Wsig es un protocolo que utiliza los servidores web para servir las páginas web escritas en Python.

Buen manejo de rutas: Cuando se trabaja con Apps Web hechas en Python se tiene el controlador que recibe todas las peticiones que hacen los clientes y se tienen que determinar que ruta está accediendo el cliente para ejecutar el código necesario.

Soporta de manera nativa el uso de cookies seguras.

Se pueden usar sesiones.

Flask no tiene ORMs: Pero se puede usar una extensión.

Sirve para construir servicios web (como APIs REST) o aplicaciones de contenido estático.

Flask es Open Source y está amparado bajo una licencia BSD.

Sqlalchemy: SQLAlchemy es más famoso por su mapeador de objetos relacional (ORM), un componente opcional que proporciona el patrón del mapeador de datos, donde las clases se pueden mapear en la base de datos de forma abierta, de múltiples maneras, lo que permite que el modelo de objetos y el esquema de la base de datos se desarrollen en una Manera limpiamente desacoplada desde el principio.

pip install flask-sqlalchemy

Lo primero es lo primero, necesitamos conectarnos a nuestra base de datos, que es idéntica a la forma en que nos conectamos usando SQLAlchemy Core (Core).

Csfprotected: se encarga de llevar la secciona de los usarios a las paginas

Config.py: Podemos usar Secret key, Conectarse a la base, Notificaciones en modo inactivo.

pgadmin: Ver la base de datos de administracion.
https://www.pgadmin.org/

Forms: para renderizar todas las cosas en la pagina web.

Verificar la utilidad del readme con la documentacion del proyecto.

Los archivos principales de python son: app.py, config.py, forms.py y models.py.

Models = tiene la definicion de las tablas Usuarios, comentarios y equipos y las relaciones entre ellas

config = contiene la configuracion necesaria para conectar la aplicacion a una base de datos postgres.

forms = ayuda a renderisar los forms y facilita a la carga de datos por medio de los metodos GET y POST

app.py es aqui el corazon del programa, es el quien todos los metodos necesarios para la creacion, carga, actualizacion y borrado de datos

Alcances del programa:

El programa cuando se ejecuta crea dentro de la una base de datos en el path definido durante la instalacion y con la creacion de la base de daros se crea 3 tablas, usuarios, comentarios y teams. Dentro del file config.py esta la ruta del URI para la misma y junto con el password del sys admin para poder usar al maximo la base de datos.
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:palomo@localhost/examen02'

El usuario que debe de crear primero es el superuser, dentro del codigo se asignan derechos administrativos a la cuenta superuser.
En la ventada de login se presenta la opcion de Login y de crear cuenta nueva.
Las cuentas se validan, si el nombre existe o no cumple los requisitos de permite crear la misma.
Usuarios regulares solo pueden agregar comentatios.
El usuario superuser es quien puede asignar los equipos a los usuarios.
El usuario superuser tiene los accesos a (a) Cambiar password a usuarios existentes (b) Borrar usuarios (c) Listar usuarios segun el equipo
No que el programa no hace

No se asignan lideres de equipo
No se valida password complejo.
No se configuro la pregunta de seguridad.
No se logro generar json para crear logs en el programa.
