import os
import trimesh
from trimesh import transformations as tf
import math
import shutil
import numpy as np


models = os.listdir('./Models')
shutil.rmtree("./Output", ignore_errors=True)
os.mkdir("./Output")

for model in models:
    
    modelPath = '.\\Models\\' + model
    os.system('.\\Tool\\cpu_objectbased.exe ' + modelPath)


    files = os.listdir('.')
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".ppm":
            newname = filename.replace("img", model.split('.')[0])
            os.rename(filename, newname)
            shutil.move(newname, ".\\Output")