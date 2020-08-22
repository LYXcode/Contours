import os
import math
import shutil
import bpy

models = os.listdir('./Models')
shutil.rmtree("./Output", ignore_errors=True)
os.mkdir("./Output")

D = bpy.data
C = bpy.context

Angles = [[0,0,0],[0,0,90],[0,0,180],[0,0,270]]

def deg2rad(deg):
    return deg * math.pi / 180.

def rotate_export_model(filename, x,y,z):
    path = './Models/' + filename + '.off'
    bpy.ops.import_mesh.off(filepath=path, filter_glob='*.off')
    model = D.objects[filename]
    model.rotation_euler = (deg2rad(x),deg2rad(y), deg2rad(z))
    model.select_set(True)
    bpy.ops.object.transform_apply(location = True, scale = True, rotation = True)
    output_path = "./tmp/"+filename+".obj"
    #bpy.ops.export_mesh.off("EXEC_DEFAULT", filepath=output_path)
    bpy.ops.export_scene.obj("EXEC_DEFAULT", filepath=output_path, filter_glob="*.obj", use_selection=True)
    D.objects.remove(model, do_unlink=True)
    D.meshes.remove(D.meshes[filename])

for model in models:
    name = model.split('.')[0]
    for angle in Angles:
        rotate_export_model(name, angle[0], angle[1], angle[2])
        modelPath = './tmp/' + name + '.obj'
        os.system('.\\Tool\\cpu_objectbased.exe ' + modelPath)

    files = os.listdir('.')
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".ppm":
            newname = filename.replace("img", model.split('.')[0])
            os.rename(filename, newname)
            shutil.move(newname, "./Output")

