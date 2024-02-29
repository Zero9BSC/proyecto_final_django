# Gaming Zone

*Franco Nicolás Jones👋

> Este es un proyecto realizado para el curso de Python en coderhouse. Se trata de un blog en el que podrás navegar y crear posts categorizados..

> Puede ver una preview del proyecto funcionando entrando en el siguiente [Link](https://drive.google.com/file/d/1UQogxk6BA6FiGMrn9pE7OHwpk2uwgWmD/view?usp=drivesdk)
## Installation git clone

Para acceder al proyecto clonándolo, deberás ejecutar en consola: 
```sh
git clone https://github.com/Zero9BSC/proyecto_final_django.git
```
## Cómo instalar y ejecutar el proyecto
Se debe crear el entorno virtual de python:

```cmd
cd proyecto_final_django

python -m venv django
```
Luego activamos el entorno con el siguiente comando:
```cmd
django\Scripts\activate
```

## Requerimientos
Para instalar los requerimientos procederemos de la siguiente forma.
```cmd
pip install -r requirements.txt
```


## Como iniciar el proyecto
Para correr nuestro blog deben iniciar nuestro proyecto en la carpeta "my_blog" de la siguiente manera:
```cmd
cd my_blog
```
Luego realizamos una migracion de nuestros Models para asegurarnos que corra todo bien:
```cmd
python manage.py migrate  
```

Por ultimo iniciamos nuestro servidor local de la siguiente manera:
```cmd
python manage.py runserver
```

Si todo fue bien esto iniciara un servidor web de nuestro [Blog(Click para ir al inicio)](http://localhost:8000) en el cual ya podremos trabajar.

Para gestionar el servidor primero debemos crear un super usuario con el siguiente comando desde la terminal y cargar los datos que nos pide:
```cmd
python manage.py createsuperuser
```

Para acceder al menu de administrador debe colocar en la barra de navegacion http://localhost:8000/admin/ o darle click al siguiente [Link](http://localhost:8000/admin/) y loguearse con los datos anteriormente cargados.


## Techs

🛠️ Python

🛠️ Django

🛠️ HTML

🛠️ CSS


## Backend

Cada Modelo será creado de la siguiente manera: 

🌱 Post: Cada post será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |

🌱 PostNoticias: Cada Post de noticias será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |


🌱 PostReviews: Cada Post de reviews será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |


🌱 PostGaming: Cada Post de gaming será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |

🌱 PostSoftware: Cada Post de software será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |


🌱 PostHardware: Cada Post de hardware será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    titulo     |   CharField   |   titulo      |
|   subtitulo   |   CharField   |   subtitulo   |
|      fecha    |   DateField   |    fecha      |
|   texto       |   CharField   |   texto       |


🌱 Contacto: Cada contacto será según lo siguiente:

|    Campo      |   Tipo        |   Valor       |
| ------------- | ------------- | ------------- |
|    nombre     |   CharField   |   nombre      |
|   email       |   EmailField  |   email       |
|   consulta    |   CharField   |    consulta   |
