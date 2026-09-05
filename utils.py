import bpy
import math

def get_unique_materials(collection):
    materials = {}
    for obj in collection.objects:
        if obj.type == 'MESH' and obj.data.materials:
            for mat in obj.data.materials:
                if mat and mat.name not in materials:
                    materials[mat.name] = mat
    return list(materials.values())

def calculate_grid_dimensions(count):
    cols = int(math.ceil(math.sqrt(count)))
    rows = int(math.ceil(count / cols))
    return rows, cols

def cleanup_preview_scene(scene):
    coll = scene.collection.children.get("Preview_Sheet")
    if coll:
        for obj in list(coll.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(coll)
