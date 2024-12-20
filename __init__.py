bl_info = {
    "name": "Cleanup & Transform Plugin",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (4, 3, 1),  
    "location": "3D View > Sidebar > Clean Up",
    "description": "Cleanup, transform, and clear custom split normals",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}

import bpy
import cleanup_transform

classes = (
    cleanup_transform.CleanupTransformOperator,
    cleanup_transform.CleanupTransformPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()