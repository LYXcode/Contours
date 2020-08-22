import os
import trimesh
from trimesh import transformations as tf
import math
import shutil
import numpy as np

def rotate(angle, mesh : trimesh):
    # matrix_x = tf.rotation_matrix(math.radians(angle[0]), [1,0,0], mesh.centroid)
    # matrix_y = tf.rotation_matrix(math.radians(angle[1]), [0,1,0], mesh.centroid)
    # matrix_z = tf.rotation_matrix(math.radians(angle[2]), [0,0,1], mesh.centroid)
    mesh.apply_transform(tf.quaternion_matrix(tf.quaternion_from_euler(math.radians(angle[0]),math.radians(angle[1]),math.radians(angle[2]))))
    # matrix = tf.concatenate_matrices(matrix_x, matrix_y, matrix_z)
    # print(np.array(matrix))
    # print(np.array(matrix_x).dot(np.array(matrix_y).dot(np.array(matrix_z))))
    # mesh.apply_transform()

models = os.listdir('./Models')
shutil.rmtree("./Output", ignore_errors=True)
os.mkdir("./Output")
# transformAngles = [[-120, 180, 0], [0, 60, 90], [-120, 180, 0], [0, -60, -90], [210, 180, 0], [90, 0, 120], [150, 0, -180], [90, 0, -120], [90, 0, 150] , [30, 0, 90], [90, 0, 210], [150, 0, 90]]

transformAngles = [[0, 0, 0],[0, -90, -90]]
for model in models:
    modelName = model.split('.')[0]
    for tranAngle in transformAngles:
        # quaterX = tf.quaternion_from_euler(math.radians(tranAngle[0]),math.radians(0)),math.radians(0))
        # matrix = tf.quaternion_matrix(rotate_matrix(tranAngle))       
        mesh = trimesh.load('./Models/' + model)
        # print(matrix)
        # rotate([-120,180,0], mesh)
        rotate(tranAngle, mesh)
        # matrix_y = tf.rotation_matrix(math.radians(tranAngle[1]), [0,1,0])
        # mesh.apply_transform(matrix_y)
        path = '.\\ModelObj\\' + modelName + '.obj'
        mesh.export(path)
        objPath = '..\\ModelObj\\' + modelName + '.obj'
        os.system('.\\Tool\\cpu_objectbased.exe ' + path)
    files = os.listdir('.')
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".ppm":
            newname = filename.replace("img", modelName)
            os.rename(filename, newname)
            shutil.move(newname, ".\\Output")
