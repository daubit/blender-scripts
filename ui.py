from re import L
import bpy
from bpy.types import Panel, Operator


class GenerateNFT(Operator):
    """Genereates NFTs"""
    bl_idname = "object.generate_nft"
    bl_label = "Generate NFT"

    def execute(self, context):
        print("Button!")
        return {'FINISHED'}


class NFTPanel(Panel):
    bl_label = "NFT Generator"
    bl_idname = "OBJECT_PT_my_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Hello World!", icon='WORLD_DATA')

        # resolution input
        row = layout.row()
        row.label(text="Resolution:")
        row.prop("res_x")
        row.prop("res_y")

        # output directory path
        row.label(text="Output Directory:")
        row.prop("output_dir")

        # file format
        row.label(text="File Format:")
        row.prop("file_format")

        # render
        row = layout.row()
        row.operator(GenerateNFT.bl_idname, text="Render", icon="RENDER_STILL")


def register():
    bpy.utils.register_class(NFTPanel)
    bpy.utils.register_class(GenerateNFT)


def unregister():
    bpy.utils.unregister_class(NFTPanel)
    bpy.utils.unregister_class(GenerateNFT)
