# Blythonexport
A python script to export A 3DRT blender rigged animations to an ascii file.
At the time of development, this script was used on the following commerically available model:
https://3drt.com/store/characters/us-army-marines.html

Sample Fedora 34 (Linux) implementation image:<br>
<img src="https://github.com/vicktar/Blythonexport/blob/main/Capture.PNG" alt="screenshot" width="400" height="350"></img>

This script has no interface in blender, these are the GENERAL steps to use it
1. Load your model

2. Select your model

3. Load the script

(Optional) You will probably need to modify the script in a couple of places

      -change the export directory specified in "main_path"
     
      -change the export filename specified in the "outputfile"
  
      -change the frames to export..this is the python "frame" variable
  
4. Run this Python script...in Blender

5. Figure out what to do with the file...sample excerpts of the output file 

<a href="https://github.com/vicktar/Blythonexport/blob/main/uv5sldanim.dat">uv5sldanim</a>.dat


<pre>

verts, 2517
0, -0.00106, 1.33693, 0.19754 
1, -0.00106, 1.44455, 0.18907 
2, -0.12187, 1.44518, 0.19332 
3, -0.11234, 1.34821, 0.19172 
4, -0.11216, 1.23427, 0.15135 
5, -0.00106, 1.22970, 0.18043 
6, -0.00106, 1.28854, 0.18838 
7, -0.11524, 1.28618, 0.16111 
8, -0.10258, 1.15326, 0.11862 
9, -0.00115, 1.15313, 0.14921 
10, -0.09918, 1.09422, 0.11293 
11, -0.00118, 1.09147, 0.14374 
12, -0.11287, 1.06892, 0.12675 
13, -0.00120, 1.06770, 0.16365 
14, -0.19017, 1.36100, 0.17750 
15, -0.20090, 1.44625, 0.18587 
16, -0.20301, 1.30987, 0.15909 
17, -0.21359, 1.28180, 0.13040 
...
2514, 0.02195, 1.57276, -0.06826 
2515, 0.05728, 1.60761, -0.03013 
2516, 0.07298, 1.63466, 0.04400 
vnorm,2517
0, -0.00009,-0.08243,0.99658 
1, 0.00000,0.21894,0.97571 
2, -0.04965,0.21580,0.97516 
3, -0.15879,-0.21732,0.96307 
4, -0.39860,-0.37971,0.83480 
5, -0.01410,-0.25584,0.96658 
6, -0.00592,-0.21155,0.97732 
7, -0.16572,-0.28806,0.94314 
8, -0.53554,-0.25065,0.80642 
...2514, -0.33970,0.79067,0.50929 
2515, -0.75835,0.48125,-0.43959 
2516, -0.41417,0.86276,-0.28999 
faces, 4814
0, 2, 3, 0  
1, 0, 1, 2  
2, 6, 7, 4  
3, 4, 5, 6  
4, 9, 5, 4  
5, 4, 8, 9  
6, 9, 8, 10  
7, 10, 11, 9  
8, 13, 11, 10 
...
4811, 2515, 2494, 2507  
4812, 2494, 2515, 2495  
4813, 2500, 2499, 2508  
iduvxyz, 2, 0.36616, 0.25021, -0.12187, 1.44518, 0.19332
iduvxyz, 3, 0.37030, 0.20636, -0.11234, 1.34821, 0.19172
iduvxyz, 0, 0.44042, 0.20103, -0.00106, 1.33693, 0.19754
iduvxyz, 0, 0.44042, 0.20103, -0.00106, 1.33693, 0.19754
iduvxyz, 1, 0.44044, 0.25337, -0.00106, 1.44455, 0.18907
iduvxyz, 2500, 1.68900, 0.72760, 0.07827, 1.68087, -0.01608
iduvxyz, 2499, 1.67050, 0.74280, 0.08039, 1.71370, -0.01810
iduvxyz, 2508, 1.68910, 0.75980, 0.07548, 1.68087, -0.01569
face material list
0, 0,usmarine-01
0, 1,usmarine-01
0, 2,usmarine-01
0, 3,usmarine-01
0, 4,usmarine-01
0, 5,usmarine-01
...
0, 3305,usmarine-01
0, 3306,usmarine-01
0, 3307,usmarine-01
1, 3308,m16_gun
1, 3309,m16_gun
1, 3310,m16_gun
1, 3311,m16_gun
...
1, 4346,m16_gun
1, 4347,m16_gun
1, 4348,m16_gun
1, 4349,m16_gun
0, 4350,usmarine-01
0, 4351,usmarine-01
0, 4352,usmarine-01
0, 4353,usmarine-01
0, 4354,usmarine-01
...
0, 4810,usmarine-01
0, 4811,usmarine-01
0, 4812,usmarine-01
0, 4813,usmarine-01
frame, 1270, 1, 67
0, -0.00106, 1.33084, 0.19807 
1, -0.00106, 1.43850, 0.19006 
2, -0.12187, 1.43911, 0.19431 
3, -0.11234, 1.34214, 0.19230
...
2514, 0.02195, 1.56746, -0.06685 
2515, 0.05728, 1.60228, -0.02869 
2516, 0.07298, 1.62926, 0.04546 
frame, 1280, 2, 67
0, -0.00106, 1.32681, 0.19754 
1, -0.00106, 1.43443, 0.18907 
2, -0.12187, 1.43506, 0.19332 
      
</pre>
