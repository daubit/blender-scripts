# Blender NFT Generator

Blender Addon to generate NFTs from a given scene.

## Installation


1. Get the addon zip file from [GitHub](https://github.com/daubit/blender-scripts/releases/).
2. Go to `Edit > Preferences > Addons > Install` and select the downloaded zip file.
3. Type `NFT Generator` in the search box and enable the addon.

## Usage

Open the scene you want to generate NFTs of.

Go to `Scene Properties > NFT Generator`.

Adjust the scene to your needs and click on `Render`.
(This may take some time depending on the complexity of your scene. NOTE: The rendering is done on the main thread and on the GPU to speed up the process.)

### Properties

**Resolution** (int, int): The resolution of the generated NFTs.

**Ouput Directory** (string): The directory string path to the output directory.

**Camera Scene** (string): The collection name where the camera and the lights are located (This is needed since the camera and the lights need to be ignored when rendering the different combinations of NFTs).

**File Format** ("PNG" | "JPEG"): The output file format for the generated NFTs.
