bl_info = {
    "name": "Material Preview Sheet",
    "author": "Blender Tools",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Preview Sheet",
    "description": "Generate organized material preview sheets with automated lighting and export",
    "category": "3D View",
}

import bpy
from . import constants, utils, lighting, export, ui, operators

classes = (
    operators.GeneratePreviewSheet,
    ui.PreviewSheetProperties,
    ui.PreviewSheetPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.preview_sheet_props = bpy.props.PointerProperty(type=ui.PreviewSheetProperties)

def unregister():
    del bpy.types.Scene.preview_sheet_props
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
