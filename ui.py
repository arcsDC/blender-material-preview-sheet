import bpy
from bpy.props import FloatProperty, StringProperty, BoolProperty, CollectionProperty

class PreviewSheetProperties(bpy.types.PropertyGroup):
    cube_size: FloatProperty(name="Cube Size", default=1.0, min=0.1, max=10.0)
    grid_spacing: FloatProperty(name="Grid Spacing", default=2.0, min=0.5, max=20.0)
    export_path: StringProperty(name="Export Path", default="", subtype='FILE_PATH')
    clear_scene: BoolProperty(name="Clear Scene", default=False)
    render_mode: BoolProperty(name="Render Image", default=False)

class PreviewSheetPanel(bpy.types.Panel):
    bl_label = "Preview Sheet"
    bl_idname = "PREVIEW_PT_preview_sheet"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Preview Sheet"

    def draw(self, context):
        layout = self.layout
        props = context.scene.preview_sheet_props
        layout.prop(props, "cube_size")
        layout.prop(props, "grid_spacing")
        layout.prop(props, "clear_scene")
        layout.prop(props, "render_mode")
        layout.prop(props, "export_path")
        layout.operator("preview.generate_sheet", text="Generate Sheet")
