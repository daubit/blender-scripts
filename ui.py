from bpy.utils import register_class, unregister_class
import bpy
from bpy.types import Panel, Operator
from nftgen import get_render_operations

NFT_DONE = True


class ProgressbarOperator(Operator):

    bl_idname = "example.progressbar_operator"
    bl_label = "Progressbar Operator"

    def __init__(self):

        self.step = 0
        self.timer = None
        self.max_step = None

        self.operations = {}

    def modal(self, context, event):
        operations = self.operations

        # update progress bar
        global NFT_DONE
        if not NFT_DONE:
            # update progess bar
            context.scene.progress = ((self.step+1)/(self.max_step))*100
            # update label
            context.scene.progress_label = list(operations.keys())[self.step]
            # send update signal
            context.area.tag_redraw()

        # by running a timer at the same time of our modal operator
        # we are guaranteed that update is done correctly in the interface

        if event.type == 'TIMER':

            if NFT_DONE:
                self.step = 0
                context.scene.progress = 0
                context.window_manager.event_timer_remove(self.timer)
                context.area.tag_redraw()

                return {'FINISHED'}

            if self.step < self.max_step:
                # run step function
                print(f"Running step ({self.step+1}/{self.max_step})...")
                list(operations.values())[self.step]()

                self.step += 1
                if self.step == self.max_step:
                    NFT_DONE = True

                return {'RUNNING_MODAL'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        # terermine max step
        scene = context.scene
        res_x = scene.res_x
        res_y = scene.res_y
        output_dir = scene.output_dir
        target_collection = scene.target_collection
        file_format = scene.file_format

        global NFT_DONE
        NFT_DONE = False

        self.operations = get_render_operations(
            output_dir, (res_x, res_y), target_collection, file_format)
        operations = self.operations

        if self.max_step == None:
            self.max_step = len(operations.keys())

        context.window_manager.modal_handler_add(self)

        # run timer
        self.timer = context.window_manager.event_timer_add(
            0.1, window=context.window)

        return {'RUNNING_MODAL'}


class StopButton(Operator):
    bl_idname = "example.stop_button"
    bl_label = "Stop"

    def execute(self, context):
        global NFT_DONE
        NFT_DONE = True
        return {'FINISHED'}


class NFTPanel(Panel):
    bl_label = "NFT Generator"
    bl_idname = "OBJECT_PT_nft_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        global NFT_DONE
        if not NFT_DONE:
            row = layout.row()
            row.prop(scene, "progress")
            row = layout.row()
            row.active = False
            row.label(text=scene.progress_label)
            row = layout.row()
            row.operator(StopButton.bl_idname,
                         text="Cancel", icon="CANCEL")
        else:
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
            row.label(text="Target Collection Name:")
            row.prop(scene, "target_collection")

            # file format
            row.label(text="File Format:")
            row.prop(scene, "file_format")

            # render
            row = layout.row()
            row.operator_context = "INVOKE_DEFAULT"
            row.operator(ProgressbarOperator.bl_idname,
                         text="Render", icon="RENDER_STILL")


def register():
    register_class(ProgressbarOperator)
    register_class(StopButton)
    register_class(NFTPanel)


def unregister():
    unregister_class(ProgressbarOperator)
    unregister_class(StopButton)
    unregister_class(NFTPanel)
