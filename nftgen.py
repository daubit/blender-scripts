from math import comb
import bpy
import os
import itertools as it
from collections import OrderedDict


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
    scene.render.filepath = os.path.join(
        path, f"{get_file_name(objs)}.{file_format.lower()}")
    bpy.ops.render.render(write_still=True)

    for obj in objs:
        obj.hide_render = True


def get_collections(collection, col_list=[]):
    col_list.append(collection)
    for sub_collection in collection.children:
        get_collections(sub_collection, col_list)
    return col_list


def get_render_operations(path, res=(128, 128), target_collection="NFT Gen", file_format="PNG"):
    for s in bpy.data.scenes:
        s.render.engine = "CYCLES"

    compute_device_type = "CUDA"  # or "OPENCL"

    # Set the device_type
    bpy.context.preferences.addons[
        "cycles"
    ].preferences.compute_device_type = compute_device_type

    # Set the device and feature set
    bpy.context.scene.cycles.device = "GPU"

    # get_devices() to let Blender detects GPU device
    bpy.context.preferences.addons["cycles"].preferences.get_devices()
    print(
        bpy.context.preferences.addons["cycles"].preferences.compute_device_type)
    for d in bpy.context.preferences.addons["cycles"].preferences.devices:
        d["use"] = True
        print(d["name"], d["use"] == True)

    for sceneCol in bpy.data.scenes:
        sceneCol.render.resolution_x = res[0]
        sceneCol.render.resolution_y = res[1]

    # enable the camera
    for obj in bpy.data.objects:
        obj.hide_viewport = False
        obj.hide_render = False

    # Get all objects
    collections = get_collections(bpy.data.collections[target_collection])
    layers = OrderedDict()

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

    total = get_total_combinations(collections)
    print(f"Total combinations: {total}")

    allNames = list(layers.keys())
    combinations = it.product(*(layers[Name] for Name in allNames))

    combinations = list(combinations)

    scene = bpy.context.scene
    scene.render.image_settings.file_format = file_format

    # create all folders to path
    if not os.path.exists(path):
        os.makedirs(path)

    operations = {}

    for i, combination in enumerate(combinations):
        def render_combination(combination=combination):
            # print(f"{get_file_name(combination)}.{file_format.lower()}")
            render_scene(combination, path, file_format)
        operations[f"Rendering combination {i + 1}/{total}"] = render_combination

    return operations
