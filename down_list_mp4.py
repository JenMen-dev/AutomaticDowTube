
import os 
#from variables import *


input("¿Listo para descargar tu lista en mp4? Entonces dale doble Enter." +'\n')

listVd = r".\youtube-dl --download-archive C:\Users\Mountain\Documents\Proyectos\AutomaticDowTube\_mp4_list.txt"

os.system(listVd)
