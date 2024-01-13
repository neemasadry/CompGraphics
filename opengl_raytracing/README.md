# Rendering 3D Environment
**Assignment #2** for **Computer Graphics I** completed by **Neema Sadry**

## Requirements
In general, we had to implement shading, local illumination, and global illumination using ray tracing.

Specfically, we had to render multiple different cow models from `cow.obj` after rendering a basic floor and three walls. Moreover, we were tasked with implementing the following features:
  - Support for *several* light sources.
  - Interactively turn lights on and off via keyboard input.
  - Support **flat** and **Gouraud** shading models.
  - Interactive change the (RGBA) values associated with the **global ambient light**.
  - Interactive change the (RGBA) values associated with the **specular material properties** of the objects.
  - Render **global illumination** by considering the interactions among *all* the objects and lights attenuated along *ray distance* to enable **shadows** and **reflections**.
    - Render **shadows** when an object comes in between a light source and the surface position of another given object.
    - Render **reflections** on cow models to be reflective by defining a recursive function to traverse a ray from the camera to the surface position to find the color of light. Repeat this process until the **maximum** number of recursions or the ***maximum distance*** of the ray path is reached.

## Libraries
Utilized the following open-source libraries to implement critical functionality:
  - [Asset Importer (i.e., `assimp`)](https://github.com/assimp/assimp) was used to import OBJ files.
  - [`stb_image.h`](https://github.com/nothings/stb) from [`stb`](https://github.com/nothings/stb) was used for image loading/decoding from file/memory.
  - An [alternate Cow model](https://sketchfab.com/3d-models/cow-brown-29f7d53eae024e4d86d0d1360d32fa5d) was used in addition to the cow.obj file provided because the texture wasn't rendering correctly. 

## Instructions
### Important information
- `Visual Studio 2022` (i.e., **`vs143`**) was used for this project. 
  - *Note: If you encounter any technical issues try installing **Visual Studio 2022 or later** for compiling and running the application.*
- The project was compiled to run on `x86` architecture in `Debug` mode. 
- All necessary files are included.

1) Open project folder
2) Double-click the Visual Studio Solution file named: **`A2NS.sln`**
3) Make sure **`Debug`** and **`x86`** are selected in the top row of Visual Studio's user interface
![VS top menu bar screenshot](https://capture.dropbox.com/rXG0ElCAfjH65TTP)
4) Click the adjacent button: **`Local Windows Debugger`**

Make sure to *clean* the solution if running into any issues, which can be found under the **Build** menu.

## Controls
###  Camera
  - Use the mouse to **pan** the camera around
  - Use the `W`, `A`, `S`, and `D` keys on the keyboard to change the camera's **position**.

*Note: There is **no** command to adjust the `roll` of the camera because there is no reason to implement that functionality in the context of this project.*

### Lighting
Use the following keyboard inputs to modify the following lighting attributes:
- `L` - Turns on/off ***`main`*** lighting AND all shadows
- `K` - Turns on/off ***`spot`*** lights (*not* shadows)
- `J` - Turns on/off ***`point`*** lights (*not* shadows)

