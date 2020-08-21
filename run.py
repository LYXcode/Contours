import os
import trimesh
from trimesh import transformations as tf
import math
models = os.listdir('./Models')

transformAngles = []
quater = tf.quaternion_from_euler(0, 0, math.pi)
matrix = tf.quaternion_matrix(quater)
for model in models:
    modelName = model.split('.')[0]    
    mesh = trimesh.load('./Models/'+ model)
    path = './ModelObj/'+ modelName + '.obj'
    mesh.export(path)   
    os.system('./Binaries/cup_objectbased.exe ' + path)
