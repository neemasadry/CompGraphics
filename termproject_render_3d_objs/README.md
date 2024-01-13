# 3D Model Reconstruction

**Term Project** for **Computer Graphics I** completed by **Neema Sadry**

## Requirements & Process
The goal of this project was to render a 3D model from a reasonably sized object in the real world.

## Libraries
Utilized the following open-source libraries to implement critical functionality:

  - [`OpenCV-Python`](https://github.com/opencv/opencv-python) was used to slice high-resolution images (i.e., *frames*) from a 4K video file running at 60 FPS.
    - An **`iPhone 14 Pro`** was used to take a full 360-degree recording of the model.
    - The `iPhone` remained fixed in position with respect to the model(s), which were placed on a `lazy Susan`, and rotated slowly.
      - In general, the longer the video, the more frames are able to be sliced out from the video file when using `OpenCV-Python`, which increases `COLMAP` processing times significantly, but yields a larger, richer, and more accurate `dense point cloud`. Using this higher-quality `dense point cloud` renders a much crisper, accurate, and correct 3D reconstruction of the model(s).

  - [`COLMAP`](https://colmap.github.io/index.html) was used to process all the sliced high-resolution images via COLMAP's dense reconstruction pipeline. Processing was handled by the GPU to speed up the process and output the best results, specifically using a `RTX 3070` card. Overall, processing took *roughly* 3-4 hours to complete for ***each*** of the models.
    - Starts off by producting both `normal` and `depth` maps for all the images.
    - Next, both maps are fused into a `dense point cloud` with normal information.
    - Finally, a `dense surface` is estimated from the fused point cloud output using `Poisson reconstruction`.
    - More information can be found under [Dense Reconstruction](https://colmap.github.io/tutorial.html#dense-reconstruction) on [COLMAP's tutorial page](https://colmap.github.io/tutorial.html#).

  - [`MeshLab`](https://www.meshlab.net/) was used to import and view the `dense point cloud` data we obtained from the previous step, and to reconstruct the surfaces of the model using the `Screened Poisson Surface Reconstruction` algorithm, which theoretically yields a realistics representation of the model's surfaces.

Screenshots were taken at various times from all these steps and are available for viewing under the folder `screenshots`.
