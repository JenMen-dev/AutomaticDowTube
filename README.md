
(errores actuales: down_list_mp3.py down_list_mp4.py, solo descargan la primera cancion de la lista, al finalizar esta, lanza un error (descrito mas abajo en errores posibles)).

# AutomaticDowTube

_Descarga contenido de yotube en distintos formatos. ¡Script de extrema sencillez! para el manejo del usuario _

## Comenzando 🚀 

Trabajaremos desde la terminal, ya sea de windows o de linux, funciona tanto en local como en vm y con todos los principales entornos de desarollo o IDE.

_Al ejecutar el programa este nos pedira dos parametros: tipo de descarga y url del video.
- Tipo de descarga: estan dentro de sus propias variables, definidas en el documento "variables.py" 
- Url del video: Es el id del video y se almacena en la variable "codVd".
  Sencuentra en el link del mismo. Siempre se encuentra al final de esta cadena.
    ejemplo: https://www.youtube.com/watch?v=     re4TwtTjZjg  <- url del video

### Pre-requisitos ⚙️

_Unicamente necesitaremos descargar:  
_archivo "youtube-dl.exe"._
_carpeta "ffmpeg" Framework libre de audio_

### Descarga e Instalación youtube-dl.exe y ffmpeg 🔧

_Descarga youtube-dl.exe._

_- Windows:_

_Descarga youtube-dl.exe aquí: "" y alojala el archivo en el mismo directorio donde se encuentran los ejecutables._
_Descarga ffmpeg aquí: https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2_. Es una carpeta, alojala en el directorio raiz.
_(aquí encontraras toda la dpcumentacion del software: https://github.com/FFmpeg/FFmpeg)_


_- Linux:_

_Descarga desde la terminal con uno de los siguientes comandos:_ 

$ sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl

_ó bien_

$ sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl

_ó bien, si lo queremos instalar mediante un gestor de paquetes_

$ sudo apt install youtube-dl


_Damos permisos de ejecución a nuestro usuario para el archivo:_ ""_

$ sudo chmod a+rx /usr/local/bin/youtube-dl


### Configuración youtube-dl.exe 🔧

Puede configurar youtube-dl colocando cualquier opción de línea de comando admitida en un archivo de configuración. 
En Linux y macOS, el archivo de configuración de todo el sistema se encuentra en /etc/youtube-dl.conf y el archivo de configuración de todo el usuario 
en ~/.config/youtube-dl/config. En Windows, las ubicaciones de los archivos de configuración de todo el usuario son %APPDATA%\youtube-dl\config.txt 
o C:\Users\<nombre de usuario>\youtube-dl.conf. Tenga en cuenta que, de forma predeterminada, es posible que el archivo de configuración no exista, 
por lo que es posible que deba crearlo usted mismo.


_- Windows:_

_Puedes crear el archivo de configuración usando los siguientes dos comandos:_

mkdir -p ~/.config/youtube-dl/
echo "-o ~/Downloads/%(title)s-%(id)s.%(ext)s" > ~/.config/youtube-dl/config

_El primer comando mkdir crea las carpetas que llevan al archivo de configuración._
_El segundo comando echo escribe la opción de salida en el archivo._


_- Linux:_

_Cear un archivo de configuración que sea usado para la totalidad de usuarios:_

sudo touch /etc/youtube-dl.conf

_Crear un archivo de configuración que  sea útil para su usuario deberán ejecutar el siguiente comando:_

touch ~/.config/youtube-dl/config

_Las opciones establecidas dentro de su archivo de configuración se aplican a cada llamada a youtube-dl . Use la opción --ignore-config para deshabilitar la lectura del archivo de configuración._


## Como usar este programa

_Elije el archivo.exe que se adapte a la modalidad de descarga que deseas (1to1 o modo list), ejecuta dicho archivo y sigue las instrucciones_


## Archivos que contiene 📋

_mp3_list.txt   -> La completaremos con las url que vamos a descargar en mp3, en caso de querer usar una lista._
_mp4_list.txt   -> La completaremos con las url que vamos a descargar en mp4, en caso de querer usar una lista._
README.md       -> Es este documento mismo._
down_list_mp3.py   -> Es el archivo ejecutable que desencadenará las acciones del script, para descargar loos elementos de la lista  "_mp3_list.txt"
down_list_mp4.py   -> Es el archivo ejecutable que desencadenará las acciones del script, para descargar loos elementos de la lista  "_mp4_list.txt"
down_mp3_1to1_input  -> Es el archivo ejecutable que desencadenara las acciones del script, para descargar archivos mp3 1 a 1.
down_mp4_1to1_input  -> Es el archivo ejecutable que desencadenara las acciones del script, para descargar archivos mp4 1 a 1.
variables.py       -> Los tipos de datos que podemos descargar metido en variables para ser seleccionados._
youtube-dll.exe    -> Es el motor de busqueda que vamos a utilizar._


### Errores posibles ⌨️

_ERROR: ffprobe/avprobe and ffmpeg/avconv not found. Please install one:_
_Ejemplo:_
```
[youtube] 0o268IlcLbY: Downloading webpage
[download] El Origen de Navidad _ Destripando la Historia _ CANCIÓN Parodia-0o268IlcLbY.webm has already been downloaded
[download] 100% of 2.85MiB
ERROR: ffprobe/avprobe and ffmpeg/avconv not found. Please install one.
```
_-No tienes instalado ( o ubicado en la carpeta correcta ) ffprobe, consulta la documentación: https://github.com/FFmpeg/FFmpeg_

## Despliegue 📦

_Funciona en entornos virtuales, sin embargo dada su extrema sencillez, se puede trabajar directamente en local_

## Construido con 🛠️

_youtube-dl.exe_
_ffmpeg_

## Contribuyendo 🖇️

Por favor lee el ""

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki]

## Versionado 📌

Usamos version ""


## Autores ✒️

* **J.M** - *Trabajo Inicial* - 
* **J.M** - *Documentación* - 


## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo ... para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---
⌨️ con ❤️ por [J.M](https://(WEB)) 😊
