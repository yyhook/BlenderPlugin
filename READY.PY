import bpy

def cleanup_and_transform():
    # 第一步：清除并保证变换结果
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    # 第二步：实例独立化
    for obj in bpy.context.selected_objects:
        if obj.type == 'EMPTY' and obj.instance_type != 'NONE':
            bpy.ops.object.duplicates_make_real(use_base_parent=True, use_hierarchy=True)
            bpy.ops.object.delete(use_global=False, confirm=False)

    # 第三步：全部变换
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL')

    # 第四步：删除所有空物体、灯光、相机和样条线
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.data.objects:
        if obj.type in ['EMPTY', 'LIGHT', 'CAMERA', 'CURVE']:
            obj.select_set(True)
    bpy.ops.object.delete()

    # 第五步：在物体模式下清除自定义拆边法向数据
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.mode_set(mode='OBJECT')  # 确保在物体模式
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            bpy.context.view_layer.objects.active = obj
            bpy.ops.mesh.customdata_custom_splitnormals_clear()

if __name__ == "__main__":
    cleanup_and_transform()