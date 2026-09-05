import bpy
from mathutils import Vector
from . import constants

def setup_lighting_and_camera(scene, grid_width, grid_height):
    # Key Light
    key_data = bpy.data.lights.new("Key_Light", type='AREA')
    key_data.energy = constants.LIGHT_INTENSITY
    key_obj = bpy.data.objects.new("Key_Light", key_data)
    key_obj.location = (grid_width * 0.5, -grid_height * 0.5, 5)
    key_obj.rotation_euler = (0.5, 0, 0.5)
    scene.collection.objects.link(key_obj)

    # Fill Light
    fill_data = bpy.data.lights.new("Fill_Light", type='AREA')
    fill_data.energy = constants.LIGHT_INTENSITY * 0.5
    fill_obj = bpy.data.objects.new("Fill_Light", fill_data)
    fill_obj.location = (-grid_width * 0.5, -grid_height * 0.5, 3)
    fill_obj.rotation_euler = (0.5, 0, -0.5)
    scene.collection.objects.link(fill_obj)

    # Rim Light
    rim_data = bpy.data.lights.new("Rim_Light", type='AREA')
    rim_data.energy = constants.LIGHT_INTENSITY * 0.7
    rim_obj = bpy.data.objects.new("Rim_Light", rim_data)
    rim_obj.location = (0, grid_height * 0.5, 4)
    rim_obj.rotation_euler = (-0.5, 0, 0)
    scene.collection.objects.link(rim_obj)

    # Camera
    cam_data = bpy.data.cameras.new("Preview_Camera")
    cam_data.lens = 50
    cam_obj = bpy.data.objects.new("Preview_Camera", cam_data)
    dist = max(grid_width, grid_height) * constants.CAMERA_DISTANCE_FACTOR
    cam_obj.location = (0, -dist, dist * 0.5)
    cam_obj.rotation_euler = (1.2, 0, 0)
    scene.collection.objects.link(cam_obj)
    scene.camera = cam_obj
