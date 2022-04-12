
import os 
#from variables import *


codVd = input("Introduce la url del video" +'\n')

dowAu = ".\youtube-dl -x --extract-audio  --audio-format mp3 " + codVd 

os.system(dowAu)