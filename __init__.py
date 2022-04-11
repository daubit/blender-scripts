import bpy
import sys
import os

dir = os.path.join(os.path.dirname(bpy.data.filepath), "gen-nft")
print(dir)
if not dir in sys.path:
    sys.path.append(dir)

bl_info = {
    "name": "NFT Generator",
    "description": "Generate NFT",
    "author": "Eugene Matsumura",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Render"
}

def register():
    from ui import register as ui_register
    from properties import register as properties_register
    ui_register()
    properties_register()


def unregister():
    from ui import unregister as ui_unregister
    from properties import unregister as properties_unregister
    ui_unregister()
    properties_unregister()


# if __name__ == '__main__':
#     register()
