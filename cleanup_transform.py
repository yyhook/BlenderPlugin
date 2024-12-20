import bpy

class CleanupTransformOperator(bpy.types.Operator):
    """Operator for cleaning up, transforming, and clearing custom split normals"""
    bl_idname = "object.cleanup_transform"
    bl_label = "Cleanup and Transform"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # 执行你的清理和变换代码
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        for obj in bpy.context.selected_objects:
            if obj.type == 'EMPTY' and obj.instance_type != 'NONE':
                bpy.ops.object.duplicates_make_real(use_base_parent=True, use_hierarchy=True)
                bpy.ops.object.delete(use_global=False, confirm=False)

        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL')

        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.data.objects:
            if obj.type in ['EMPTY', 'LIGHT', 'CAMERA', 'CURVE']:
                obj.select_set(True)
        bpy.ops.object.delete()

        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                bpy.context.view_layer.objects.active = obj
                bpy.ops.mesh.customdata_custom_splitnormals_clear()

        return {'FINISHED'}

class CleanupTransformPanel(bpy.types.Panel):
    """Creates a Panel in the 3D View sidebar"""
    bl_label = "Cleanup & Transform"
    bl_idname = "OBJECT_PT_cleanup_transform"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Clean Up"

    def draw(self, context):
        layout = self.layout
        layout.operator(CleanupTransformOperator.bl_idname)

def register():
    bpy.utils.register_class(CleanupTransformOperator)
    bpy.utils.register_class(CleanupTransformPanel)

def unregister():
    bpy.utils.unregister_class(CleanupTransformPanel)
    bpy.utils.unregister_class(CleanupTransformOperator)

if __name__ == "__main__":
    register()