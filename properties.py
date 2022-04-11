import os
import bpy
from bpy.types import Scene

from bpy.props import EnumProperty
from bpy.props import IntProperty
from bpy.props import StringProperty


file_types = [
    ("PNG", "PNG", "PNG"),
    ("JPEG", "JPEG", "JPEG"),
]

default_output_dir = os.path.join(os.path.dirname(bpy.data.filepath), "generated")

def register():
    Scene.res_x = IntProperty(default=128)
    Scene.res_y = IntProperty(default=128)
    Scene.output_dir = StringProperty(default=default_output_dir)
    Scene.scene_name = StringProperty(default="Scene")
    Scene.file_format = EnumProperty(items=file_types, default="PNG")


def unregister():
    del Scene.res_x
    del Scene.res_y
    del Scene.output_dir
    del Scene.scene_name
    del Scene.file_format
