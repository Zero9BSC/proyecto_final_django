# Gaming Zone

*Franco Nicolás Jones y Florencia Hnatiuk*👋

> Este es un proyecto realizado para el curso de Python en coderhouse. Se trata de un blog en el que podrás navegar y crear posts categorizados..

## Installation git clone

Para acceder al proyecto clonándolo, deberás ejecutar en consola: 
```sh
git clone https://github.com/Zero9BSC/proyecto_final_django.git
```
## Cómo instalar y ejecutar el proyecto
Se debe crear el entorno virtual de python:

```cmd
cd ProyectoFinal

virtualenv django
```
Luego activamos el entorno con el siguiente comando:
```cmd
django\Scripts\activate
```

Luego procedemos a instalar Django para correr el entorno:
```cmd
pip install Django
```
Ya estamos listos para correr nuestro entorno.

## Como iniciar el proyecto
Para correr nuestro blog deben iniciar nuestro proyecto en la carpeta "my_blog" de la siguiente manera:
```cmd
cd my_blog
python manage.py runserver
```

Si todo fue bien esto iniciara un servidor web [Blog](http://localhost:8000) en el cual ya podremos trabajar.

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
