import os
import trimesh


models = os.listdir('./Models')

for model in models:

    modelName = model.split('.')[0]    
    mesh = trimesh.load('./Models/'+ model)
    mesh.apply_transform(trimesh.transformations.random_rotation_matrix())
    path = './ModelObj/'+ modelName + '.obj'
    mesh.export(path)   
    os.system('./Binaries/cup_objectbased.exe ' + path)
