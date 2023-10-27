# PMP(Phase Measurement Profilometry)
----
## Introduction
This repository is a python implementation of "phase-shift + multi-frequency heterodyne" in the traditional PMP method. The image data in the './data' is collected by a "binocular camera + single projector". The projector projects 3 frequency fringe images separately, and each frequency fringe image projects 4 phase-shift fringes, so each camera acquires 12 images.

![image-20231027232253075](.\Resourse\image-20231027232253075.png)

Figure1.The camera acquires an image of a certain frequency of stripes(4 phase shift)

![image-20231027232551703](.\Resourse\image-20231027232551703.png)

Figure2.Wrap phase image of three frequencies(left:28 middle:26 right:24)

![image-20231027232624550](.\Resourse\image-20231027232624550.png)

Figure3.Unwrap the image(left:combining 28 and 26 middle:combining 26 and 24)

<img src=".\Resourse\phaseActual123.bmp" alt="phaseActual123" style="zoom:10%;" />

Figure4.The result of unwrapping the phase


## Getting Started
Make sure the './Resourse' folder is empty.
```markdown
python main.py
```
