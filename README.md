# Blender NFT Generator

Blender Addon to generate NFTs from a given scene.

## Installation

1. Get the addon zip file from [GitHub](https://github.com/daubit/blender-scripts/releases/).
2. Go to `Edit > Preferences > Addons > Install` and select the downloaded zip file.
3. Type `NFT Generator` in the search box and enable the addon.

## Usage

Open the scene you want to generate NFTs of.

Go to `Scene Properties > NFT Generator`.

Move all objects that is a part of the NFT into a collection called `NFT Gen` (The collection name can be adjusted in the `NFT Generator` panel).

Adjust the nft properties in the `NFT Generator` panel and click `Generate NFTs`.
(This may take some time depending on the complexity of your scene. NOTE: The rendering is done on the main thread and on the GPU to speed up the process.)

### Properties

| Property Name     | Type       | Default Value | Description                                            |
| ----------------- | ---------- | ------------- | ------------------------------------------------------ |
| Resolution        | (int, int) | (128, 128)    | The resolution of the generated NFTs.                  |
| Output Directory  | string     | "Home/NFTs"   | The directory string path to the output directory.     |
| Target Collection | string     | "NFT Gen"     | The collection name where all the objects are located. |
| File Format       | Enum       | "PNG"         | The output file format for the generated NFTs.         |
