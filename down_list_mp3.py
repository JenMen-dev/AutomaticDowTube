
import os 
#from variables import *


input("¿Listo para descargar tu lista en mp3? Entonces dale doble Enter." +'\n')

listAudio = r".\youtube-dl -x --extract-audio  --audio-format mp3 -a C:\Users\Mountain\Documents\Proyectos\AutomaticDowTube\_mp3_list.txt"

os.system(listAudio)


