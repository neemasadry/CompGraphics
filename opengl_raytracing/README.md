# Assignment #2 - Neema Sadry

**Assignment #2** for **CSC 5870 - Computer Graphics** I completed by **Neema Sadry**

The original assignment was just not rendering the way I wanted it to, so I started from scratch and have achieved so many more successful results!

[Asset Importer (i.e., assimp)](https://github.com/assimp/assimp) was used to import OBJ files.

[stb_image.h](https://github.com/nothings/stb) from [stb](https://github.com/nothings/stb) was used for image loading/decoding from file/memory.

An [alternate Cow model](https://sketchfab.com/3d-models/cow-brown-29f7d53eae024e4d86d0d1360d32fa5d) was used in addition to the cow.obj file provided because the texture could not be displayed correctly on the given cow.obj file for some reason. 

## Instructions
### Important information
- Visual Studio 2022 (i.e., **vs143**) was used for this project. 
  - Therefore, you will ***most likely* need to use Visual Studio 2022** in order to build and run this project
- The project was compiled to run on x86 architecture in Debug mode. 
- All necessary files are included.

1) Open project folder
2) Double-click the Visual Studio Solution file named: **A2NS.sln**
3) Make sure ***Debug*** and ***x86*** are selected in the top row of Visual Studio's user interface
![VS top menu bar screenshot](https://capture.dropbox.com/rXG0ElCAfjH65TTP)
4) Click the adjacent button: **Local Windows Debugger**

Make sure to *clean* the solution if running into any issues, which can be found under the **Build** menu.

## Controls
###  Camera
Use mouse to *pan* camera around and `W`, `A`, `S`, and `D` keys to change the camera's *position*.

*Note: There is **no** command to adjust the `roll` of the camera because there is no reason to implement that functionality in the context of this project.*

### Lighting
Use the following keyboard inputs to modify the following lighting attributes:
- `L` - Turns on/off ***main*** lighting AND all shadows
- `K` - Turns on/off ***spot*** lights (*not* shadows)
- `J` - Turns on/off ***point*** lights (*not* shadows)

