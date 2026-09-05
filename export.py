import bpy
import os

def save_blend_file(filepath):
    try:
        bpy.ops.wm.save_as_mainfile(filepath=filepath)
        return True
    except Exception as e:
        print(f"Error saving blend file: {e}")
        return False

def render_sheet(filepath, transparent=False):
    try:
        scene = bpy.context.scene
        scene.render.filepath = filepath
        scene.render.image_settings.file_format = 'PNG'
        scene.render.image_settings.color_mode = 'RGBA' if transparent else 'RGB'
        bpy.ops.render.render(write_still=True)
        return True
    except Exception as e:
        print(f"Error rendering sheet: {e}")
        return False
