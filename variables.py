"Ocultaremos este archivo con git ignore cuando el proyecto este terminado"

#(Utilizamos ".\" al principio de la sentencia si trabajamos con windows, para linux, simplemente se elimina, si no funcona puedes probar a añadir 
#.exe a la sentancia, ejemplo: .\youtube-dl.exe https://...) 

asinYT = "https://www.youtube.com/watch?v=ich_pnsybrY"  """El origen de juego de tronos"""
    
    # Descarga un video 

dowVd = ".\youtube-dl " + asinYT 

    # Descarga un audio.

dowAu = ".\youtube-dl -x --extract-audio  --audio-format mp3 " + asinYT


    # Visualiza todos los formatos de un video.

formatVd = ".\youtube-dl --list-formats " + asinYT 


    # Descarga audio + caratula. No funciona.

audioImg = ".\youtube-dl.exe -x  –-embed-thumbnail  --audio-format mp3 " + asinYT 


    # Descarga mp3 con el mejor audio disponible.

bestAudio = ".\youtube-dl.exe -f bestaudio -x --audio-format mp3 " + asinYT


    # Descarga mp3 un listado de videos almacenado en un archivo. No funciona (es audio).

listVd = ".\youtube-dl -a C:\Users\...\...\...\AutomaticDowTube\lista.txt"


    # Descarga una lista de mp3 almacenada en un archivo.

listAudio = ".\youtube-dl -x --extract-audio  --audio-format mp3 -a C:\Users\...\...\...\AutomaticDowTube\lista.txt"


    # Descarga mp3 un listado de videos almacenado en un archivo. (mejorado + metadatos). No funcionan los metadatos ni la caratula.

VdMeta = ".\youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 --no-part --no-mtime --embed-thumbnail --add-metadata " + asinYT



