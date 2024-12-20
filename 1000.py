import bpydef set_refractive_index():



for obj in bpy.data.objects:



if obj.type == 'MESH' and obj.data.materials:

for mat_slot in obj.material_slots:

mat = mat_slot.material

if mat:



if mat.use_nodes:

for node in mat.node_tree.nodes:

if node.type == 'BSDF_PRINCIPLED':



node.inputs ['IOR'].default_value = 1.5

print(f"Set IOR to 1.5 for material: {mat.name} on object: {obj.name}")

else:

print(f"Material {mat.name} on object {obj.name} does not use nodes.")
set_refractive_index()