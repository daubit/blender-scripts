import bpy
import os
import itertools as it

def get_total_combinations(collections):
    total = 1
    for layer in collections:
        if layer.name == "Scene":
            continue
        if len(layer.objects) > 0:
            total *= len(layer.objects)
    return total


def get_file_name(objs):
    traits = []
    for obj in objs:
        traits.append(obj.name)
    return "-".join(traits)


def render_scene(objs, path, file_format):
    for obj in objs:
        obj.hide_render = False

    # render
    scene = bpy.context.scene
    scene.render.filepath = os.path.join(path, f"{get_file_name(objs)}.{file_format.lower()}")
    bpy.ops.render.render(write_still=True)

    for obj in objs:
        obj.hide_render = True


def render(path, res=(128, 128), cam_scene="Scene", file_format="PNG"):
    for s in bpy.data.scenes:
        s.render.engine = "CYCLES"

    # Set the device_type
    bpy.context.preferences.addons[
        "cycles"
    ].preferences.compute_device_type = "CUDA"  # or "OPENCL"

    # Set the device and feature set
    bpy.context.scene.cycles.device = "GPU"

    # get_devices() to let Blender detects GPU device
    bpy.context.preferences.addons["cycles"].preferences.get_devices()
    print(bpy.context.preferences.addons["cycles"].preferences.compute_device_type)
    for d in bpy.context.preferences.addons["cycles"].preferences.devices:
        d["use"] = 1  # Using all devices, include GPU and CPU
        print(d["name"], d["use"])
        
    for sceneCol in bpy.data.scenes:
        sceneCol.render.resolution_x = res[0]
        sceneCol.render.resolution_y = res[1]

    # Get all objects
    collections = bpy.data.collections
    layers = {}

    # disable all objects in each collection
    for collection in collections:
        collection.hide_viewport = False
        collection.hide_render = False

        if len(collection.objects) <= 0:
            continue

        layers[collection.name] = []

        for obj in collection.objects:
            layers[collection.name].append(obj)

            obj.hide_viewport = True
            obj.hide_render = True

    layers.pop(cam_scene)
    layers.pop("Collection")

    total = get_total_combinations(collections)
    print(f"Total combinations: {total}")

    # enable the camera
    sceneCol = collections["Scene"]
    for obj in sceneCol.objects:
        obj.hide_viewport = False
        obj.hide_render = False

    allNames = sorted(layers)
    combinations = it.product(*(layers[Name] for Name in allNames))

    combinations = list(combinations)

    scene = bpy.context.scene
    scene.render.image_settings.file_format = file_format

    # create all folders to path
    if not os.path.exists(path):
        os.makedirs(path)

    for i, combination in enumerate(combinations):
        print(f"{i}/{total}")
        render_scene(combination, path, file_format)
