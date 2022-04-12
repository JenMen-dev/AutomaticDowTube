
import os 
#from variables import *


codVd = input("Introduce la url del video" +'\n')

dowVd = ".\youtube-dl " + codVd 

os.system(dowVd)