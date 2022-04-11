import properties
import ui

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
    ui.register()
    properties.register()


def unregister():
    ui.unregister()
    properties.unregister()


if __name__ == '__main__':
    register()
