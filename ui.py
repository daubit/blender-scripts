import bpy
from bpy.types import Panel, Operator
from nftgen import render


class GenerateNFT(Operator):
    """Genereates NFTs"""
    bl_idname = "object.generate_nft"
    bl_label = "Generate NFT"

    def execute(self, context):
        print("Button!")
        # get properties from scene
        scene = context.scene
        res_x = scene.res_x
        res_y = scene.res_y
        output_dir = scene.output_dir
        scene_name = scene.scene_name
        file_format = scene.file_format

        render(output_dir, (res_x, res_y), scene_name, file_format)

        return {'FINISHED'}


class NFTPanel(Panel):
    bl_label = "NFT Generator"
    bl_idname = "OBJECT_PT_my_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # resolution input
        row = layout.row()
        row.label(text="Resolution:")
        row.prop(scene, "res_x")
        row.prop(scene, "res_y")

        # output directory path
        row = layout.row()
        row.label(text="Output Directory:")
        row.prop(scene, "output_dir")

        # scene name
        row = layout.row()
        row.label(text="Camera Scene Name:")
        row.prop(scene, "scene_name")

        # file format
        row.label(text="File Format:")
        row.prop(scene, "file_format")

        # render
        row = layout.row()
        row.operator(GenerateNFT.bl_idname, text="Render", icon="RENDER_STILL")


def register():
    bpy.utils.register_class(NFTPanel)
    bpy.utils.register_class(GenerateNFT)


def unregister():
    bpy.utils.unregister_class(NFTPanel)
    bpy.utils.unregister_class(GenerateNFT)
