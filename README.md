# PMP(Phase Measurement Profilometry)
----
## Introduction
This repository is a python implementation of "phase-shift + multi-frequency heterodyne" in the traditional PMP method. The image data in the './data' is collected by a "binocular camera + single projector". The projector projects 3 frequency fringe images separately, and each frequency fringe image projects 4 phase-shift fringes, so each camera acquires 12 images.
<center>
<figure class="forth">
    <img src="./data/L/0000_0000_L.bmp" height=135>
    <img src="./data/L/0000_0001_L.bmp" height=135>
    <img src="./data/L/0000_0002_L.bmp" height=135>
    <img src="./data/L/0000_0003_L.bmp" height=135>
</figure>
<center style="font-size:14px;color:#000000">Figure1.The camera acquires an image of a certain frequency of stripes(4 phase shift)</center> 
<figure>
    <img src="./Resourse/phaseActual1.bmp" height=135>
    <img src="./Resourse/phaseActual2.bmp" height=135>
    <img src="./Resourse/phaseActual3.bmp" height=135>
</figure>
<center style="font-size:14px;color:#000000">Figure2.Wrap phase image of three frequencies(left:28 middle:26 right:24)</center>
<figure>
    <img src="./Resourse/phaseActual12.bmp" height=135>
    <img src="./Resourse/phaseActual23.bmp" height=135>
</figure>
<center style="font-size:14px;color:#000000">Figure3.Unwrap the image(left:combining 28 and 26 middle:combining 26 and 24)</center>
<figure>
    <img src="./Resourse/phaseActual123.bmp" height=135>
</figure>
<center style="font-size:14px;color:#000000">Figure4.The result of unwrapping the phase</center>
</center>

## Getting Started
Make sure the './Resourse' folder is empty.
```markdown
python main.py
```