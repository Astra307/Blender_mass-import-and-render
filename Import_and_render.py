import bpy
import os
import math
from pathlib import Path
import mathutils



camAngle = 0.698132 #40 degrees field of view
render_path = 'D:\\Test crap\\Art\\Cinematics\\'
library_path = 'D:\\WSlibrary\\Art\\Cinematics'


#Setting up scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(1.10932, -4.6508e-08, 0.814928), scale=(1, 1, 1))
bpy.data.objects["Camera"].location = (0,0,0)
bpy.data.objects["Camera"].rotation_euler=(1, 0, -1)
bpy.context.object.data.lens_unit = 'FOV'
bpy.context.object.data.angle = camAngle
bpy.data.scenes["Scene"].camera = bpy.data.objects["Camera"] #Make camera the active one for render

bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.511795, 0.511795, 0.511795, 1) #Set world brightness

bpy.context.scene.render.resolution_x = 1080
bpy.context.scene.render.resolution_y = 1080



#Search for 3D files

print('-Starting search')

def find_files(root, extensions):
    for ext in extensions:
        yield from Path(root).glob(f'**/*.{ext}')


def find_distance_to_object(angle, width):
    h = width / (2 * math.tan(angle/2))
    return h


files = find_files(library_path, ['gltf'])
errors = 0


print('--Starting import:')

for file in files:
    
    maxDim = 0
    
    filename = str(file)
    filename = filename.rpartition('\\')[2]
    filename = filename.rpartition('.')[0]
    
    print(filename)
    
    try:
        bpy.ops.import_scene.gltf(filepath=str(file))
    except:
        print('ERROR WHILE IMPORTING FILE')
        filename = filename + "-ERROR"
        errors = errors + 1
      

    #col = bpy.data.collections.new(filename) 
    #bpy.context.scene.collection.children.link(col)

    objs = bpy.context.selected_objects
    #bpy.ops.collection.objects_remove_all() # Remove active object from all collections not used in a scene
    for obj in objs:
        #bpy.data.collections[filename].objects.link(obj) # add it to our specific collection
        for dim in obj.dimensions:
            if dim > maxDim:
                maxDim = dim
    
    #Set camera distance
    distance = find_distance_to_object(camAngle, maxDim)
    print(distance)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects["Camera"].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects["Camera"]
    bpy.ops.transform.translate(value=(0, 0, distance), orient_type='LOCAL', orient_matrix=((0.540302, -0.841471, 0), (0.454649, 0.291927, 0.841471), (-0.708073, -0.454649, 0.540302)), orient_matrix_type='LOCAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    
    bpy.context.scene.render.filepath = render_path + filename
    bpy.ops.render.render(write_still=True)
    
    #bpy.data.collections[filename].hide_render = True
    #bpy.data.collections[filename].hide_viewport = True
    bpy.ops.object.select_all(action='SELECT')
    bpy.data.objects['Camera'].select_set(False)
    bpy.ops.object.delete()
    
    for material in bpy.data.materials:
        try:
            material.user_clear()
        except:
            print('Material error')
        try:
            bpy.data.materials.remove(material)
        except:
            print('Material error')
        
    for mesh in bpy.data.meshes:
        try:
            mesh.user_clear()
        except:
            print('Mesh error')
        try:
            bpy.data.meshes.remove(mesh)
        except:
            print('Mesh error')
        
    for armature in bpy.data.armatures:
        try:
            armature.user_clear()
        except:
            print('Arm error')
        try:
            bpy.data.armatures.remove(armature)
        except:
            print('Arm error')
        
    for image in bpy.data.images:
        try:
            image.user_clear()
        except:
            print('Image error')
        try:
            bpy.data.images.remove(image)
        except:
            print('Image error')
    
    
    bpy.data.objects["Camera"].location = (0,0,0)
    bpy.data.objects["Camera"].rotation_euler=(1, 0, -1)


print('FINISHED')
print('Number of erroneous imports: {0}'.format(errors))