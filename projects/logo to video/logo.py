import bpy
import math

# ----------------------------
# CLEAN UP DEFAULT OBJECTS
# ----------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ----------------------------
# SCENE SETUP
# ----------------------------
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 64
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.fps = 30
bpy.context.scene.frame_end = 120  # 4 seconds at 30 fps

# ----------------------------
# BACKGROUND (STARFIELD)
# ----------------------------
world = bpy.data.worlds['World']
world.use_nodes = True
bg_nodes = world.node_tree.nodes
bg_nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)  # black

# ----------------------------
# IMPORT LOGO AS PLANE
# ----------------------------
bpy.ops.import_image.to_plane(files=[{"name":"logo.png"}], directory="//")
logo = bpy.context.active_object
logo.scale = (2.5, 2.5, 2.5)
logo.location = (0, 0, 0)

# ----------------------------
# PLANET SPHERE BEHIND LOGO
# ----------------------------
bpy.ops.mesh.primitive_uv_sphere_add(radius=2, location=(0, 0, -0.2))
planet = bpy.context.active_object
mat = bpy.data.materials.new(name="PlanetMat")
mat.use_nodes = True
nodes = mat.node_tree.nodes
nodes["Principled BSDF"].inputs[17].default_value = (0.1, 0.2, 0.5, 1)  # emission glow
planet.data.materials.append(mat)

# ----------------------------
# ORBITING RINGS
# ----------------------------
bpy.ops.mesh.primitive_torus_add(location=(0,0,-0.1), major_radius=3, minor_radius=0.03)
ring = bpy.context.active_object
ring.rotation_euler[0] = math.radians(45)

ring_mat = bpy.data.materials.new(name="RingMat")
ring_mat.use_nodes = True
ring_nodes = ring_mat.node_tree.nodes
ring_nodes["Principled BSDF"].inputs[17].default_value = (0.2, 0.6, 1, 1)
ring.data.materials.append(ring_mat)

# ----------------------------
# CAMERA
# ----------------------------
bpy.ops.object.camera_add(location=(0, -8, 0), rotation=(math.radians(90), 0, math.radians(180)))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# Animate zoom in
camera.keyframe_insert(data_path="location", frame=1)
camera.location.y = -4
camera.keyframe_insert(data_path="location", frame=90)

# ----------------------------
# LIGHT
# ----------------------------
bpy.ops.object.light_add(type='SUN', radius=1, location=(5, -5, 5))
light = bpy.context.active_object
light.data.energy = 3

# ----------------------------
# TEXT ("RUTIE'S CODEVERSE")
# ----------------------------
bpy.ops.object.text_add(location=(0, -0.5, 1))
text_obj = bpy.context.active_object
text_obj.data.body = "RUTIE'S\nCODEVERSE"
text_obj.data.align_x = 'CENTER'
text_obj.data.extrude = 0.05
text_obj.scale = (0.8, 0.8, 0.8)

# Animate fade in
text_obj.keyframe_insert(data_path="hide_render", frame=1)
text_obj.hide_render = True
text_obj.keyframe_insert(data_path="hide_render", frame=40)
text_obj.hide_render = False
text_obj.keyframe_insert(data_path="hide_render", frame=60)

# ----------------------------
# RENDER SETTINGS
# ----------------------------
bpy.context.scene.render.filepath = "//rutie_intro.mp4"
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
