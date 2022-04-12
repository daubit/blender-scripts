import os
import bpy
from bpy.types import Scene

from bpy.props import EnumProperty, IntProperty, StringProperty, FloatProperty, BoolProperty


file_types = [
    ("PNG", "PNG", "PNG"),
    ("JPEG", "JPEG", "JPEG"),
]


def register():
    Scene.res_x = IntProperty(default=128, min=1)
    Scene.res_y = IntProperty(default=128, min=1)
    Scene.output_dir = StringProperty(default=os.path.join(os.path.expanduser('~'), "NFTs"))
    Scene.target_collection = StringProperty(default="NFT Gen")
    Scene.file_format = EnumProperty(items=file_types, default="PNG")

    Scene.progress = FloatProperty(
        name="Progress", subtype="PERCENTAGE", soft_min=0, soft_max=100, precision=0, options={'SKIP_SAVE'})
    Scene.progress_label = bpy.props.StringProperty(options={'SKIP_SAVE'})


def unregister():
    del Scene.res_x
    del Scene.res_y
    del Scene.output_dir
    del Scene.target_collection
    del Scene.file_format

    del Scene.progress
    del Scene.progress_label
