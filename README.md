# Blender_mass-import-and-render
A script for Blender to import and render out simple images of all 3D models in any file tree. This is particularly useful for getting a visual overview of available assets in a library. Filenames of rendered images correspond to filenames of imported 3D files.

Created for Blender 2.9, but will probably work in later versions aswell.

DISCLAIMER: This script is functional but still need some cleanup for more accessible use. 

# Using the script
1. Download the script file "Import_andrender.py"
2. Open a new Blender instance
3. Open the sript in the text editor
4. Set the render_path varable (line 10) to the folder you want the rendered images to be put, and the ary_path variable (line 11) to the folder or folder tree containing the 3D files you want visualized. (NB! Remember "\\\\")
5. The resolution of the rendered images can be set in line 27 and 28.
6. The script is set to import and process 3D files in the .gltf file format. To change this change correspoding areas (search for "gltf" in the document and replace)
7. Hit the "run script" button and it will start rendering out the pictures! 

You can follow the progress in the System Console (Menu: Window > Toggle System Console)
