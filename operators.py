import bpy
from . import utils, lighting, export, constants

class GeneratePreviewSheet(bpy.types.Operator):
    bl_idname = "preview.generate_sheet"
    bl_label = "Generate Preview Sheet"
    bl_description = "Generate a material preview sheet"

    def execute(self, context):
        props = context.scene.preview_sheet_props
        scene = context.scene
        
        # Get materials from active collection
        active_coll = context.view_layer.active_layer_collection
        materials = utils.get_unique_materials(active_coll)
        
        if not materials:
            self.report({'WARNING'}, "No materials found in active collection")
            return {'CANCELLED'}

        # Cleanup
        if props.clear_scene:
            utils.cleanup_preview_scene(scene)

        # Create Collection
        preview_coll = bpy.data.collections.new(constants.PREVIEW_COLLECTION_NAME)
        scene.collection.children.link(preview_coll)

        # Create Cubes
        rows, cols = utils.calculate_grid_dimensions(len(materials))
        spacing = props.grid_spacing
        size = props.cube_size
        
        for i, mat in enumerate(materials):
            row = i // cols
            col = i % cols
            x = (col - (cols - 1) / 2) * spacing
            y = (row - (rows - 1) / 2) * spacing
            
            bpy.ops.mesh.primitive_cube_add(size=size, location=(x, y, 0))
            cube = bpy.context.active_object
            cube.name = mat.name
            cube.data.materials.clear()
            cube.data.materials.append(mat)
            preview_coll.objects.link(cube)

        # Setup Lighting and Camera
        grid_w = cols * spacing
        grid_h = rows * spacing
        lighting.setup_lighting_and_camera(scene, grid_w, grid_h)

        # Export
        if props.export_path:
            if props.render_mode:
                export.render_sheet(props.export_path)
            else:
                export.save_blend_file(props.export_path)

        return {'FINISHED'}
