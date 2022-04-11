import bpy
from bpy.types import Scene

from bpy.props import EnumProperty
from bpy.props import IntProperty
from bpy.props import StringProperty

#
# Add additional functions or classes here
#

# This is where you assign any variables you need in your script. Note that they
# won't always be assigned to the Scene object but it's a good place to start.
def register():
    Scene.res_x = IntProperty(default=128)
    Scene.res_y = IntProperty(default=128)
    Scene.file_path = StringProperty(default="")
    # Scene.file_format = EnumProperty(items=["png", "jpg"], default="png")
    

def unregister():
    del Scene.res_x
    del Scene.res_y
    del Scene.file_path
    # del Scene.file_format