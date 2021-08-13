## Computer vision image registration algorithm in CoVSTii
Computer vision image registration algorithm in CoVSTii is a LabVIEW software to correct image motion displacement and deformation of time-lapse microscope image sequences. The inputs of the software are one or multi-channel video files (AVI). Stand-alone installer of the software is also available using the link (https://uofi.app.box.com/v/stand-aloneCoVSTii) which is a zip-file including the installation files, instructions, and a sample dataset.

Image processing of Computer vision image registration algorithm consists of four distinct steps: (i) feature points detection, (ii) motion tracking, (iii) motion correction and (iv) frame averaging.
Using the Shi and Tomasi method, the software detects feature points, which are the 'corners' changing rapidly in intensity in the reference image. The software tracks the feature points from the reference image to the paired image using Lucas Kanade optical flow analysis, the algorithm estimating the motion vector between frames. These feature point pairs are then used to calculate a homography matrix, which defines the geometric transformation of the paired images. This perspective transformation matrix is used for motion correction. Furthermore, to reduce the oscillatory motion, the software averages specified frames.

### 1. System requirements
1)	Windows 10/8.11/7 SP1.
2)	Pentium 4 G1 equivalent (Intel i5 equivalent or higher recommended).
3)	4 GB disk space.
4)	4 GB RAM [You may need more RAM for large datasets].
5)	.NET Framework 4.6.
6)	1024 x 768 resolution (1366 x 768 or higher recommended)
7)	We recommend 32-bit LabVIEW 2017 17.0f2 or newer on Windows 7 or newer.
8)	LabVIEW add-on modules
a)	Vision Development Module 2017 or newer (required by image processing in LabVIEW) 
b)	Enthought Python Integration Toolkit for LabVIEW 1.2.0 or newer (required by Python-OpenCV function in LabVIEW) 
9)	Python 2.7.13 or newer (required by Python-OpenCV function in LabVIEW) with following packages
    i)	mkl 2017.0.1-2 or newer, 
    ii)	numpy 1.11.3-2 or newer, 
    iii)	opencv 2.4.9-5 or newer (required by Python-OpenCV function in LabVIEW)

### 2. Installation
### 2. How-to-execute
-Install LabVIEW and LabVIEW add-on modules and python and python modules.  
-Go to the GitHub releases page, download 'Computer vision image registration algorighm full_Open Source.llb' and 'Perspective trasform.py'.  
-Open the downloaded LLB file in LabVIEW and then choose 'Computer vision image registration algorighm full_Open Source_Open Source.vi'.  
-Choose 'python.exe' in Python to call on front panel in LabVIEW.  
-Choose 'perspective transorm.py' in Py file to call on front panel in LabVIEW.  
-Click white arrow buttom in upper left of application.  
-Open reference movies in 'Please select Ref data' dialog.  
Note: File name should include 'Ch1-4' and all data should be in same folder. The only AVI file is available for this software. To test software, please use sample movies of the GitHub releases pages ('Sample-Ch1.avi', 'Sample-Ch2.avi', 'Sample-Ch4.avi').  
-Stabilization results will appear into the folder with reference movies file.   

