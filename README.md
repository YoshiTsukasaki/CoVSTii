## Computer-Vision Stabilization software in CoVSTii
Computer-vision stabilization is a LabVIEW software to correct motion displacement and deformation with computer-vision image registration algorithms, which is a part of Computer-Vision STabilized intravital imaging (CoVSTii) method.
Image processing of Computer-Vision Stabilization consists of four distinct steps: (i) feature points detection, (ii) motion tracking, (iii) motion correction and (iv) frame averaging.
Using the Shi and Tomasi method, the software detects feature points, which are the 'corners' changing rapidly in intensity in the reference image. The software tracks the feature points from the reference image to the paired image using Lucas Kanade optical flow analysis, the algorithm estimating the motion vector between frames. These feature point pairs are then used to calculate a homography matrix, which defines the geometric transformation of the paired images. This perspective transformation matrix is used for motion correction. Furthermore, to reduce the oscillatory motion, the software averages specified frames.

### 1. System requirements
We recommend 32-bit LabVIEW 2017 17.0f2 or newer on Windows 7 or newer to use the Computer-Vision Stabilization.
The following LabVIEW add-on modules and python modules are required:
Vision Development Module 2017 or newer (required by image processing in LabVIEW)
Enthought Python Integration Toolkit for LabVIEW 1.2.0 or newer (required by Python-OpenCV funcion in LabVIEW)
Python 2.7.13 or newer (required by Python-OpenCV funcion in LabVIEW)
Python package: mkl 2017.0.1-2 or newer,	numpy 1.11.3-2 or newer,	opencv 2.4.9-5 or newer (required by Python-OpenCV funcion in LabVIEW)

### 2. How-to-execute
-Install LabVIEW and LabVIEW add-on modules and python and python modules.  
-Go to the GitHub releases page, download 'Computer-Vision Stabilization_Open Source.llb' and 'Perspective trasform.py'.  
-Open the downloaded LLB file in LabVIEW and then choose 'Computer-Vision Stabilization_Open Source.vi'.  
-Choose 'python.exe' in Python to call on front panel in LabVIEW.  
-Choose 'perspective transorm.py' in Py file to call on front panel in LabVIEW.  
-Click white arrow buttom in upper left of application.  
-Open reference movies in 'Please select Ref data' dialog.  
Note: File name should include 'Ch1-4' and all data should be in same folder. The only AVI file is available for this software. To test software, please use sample movies n the GitHub releases pages ('Sample-Ch1.avi', 'Sample-Ch2.avi', 'Sample-Ch4.avi').  
-Stabilization results will appear into the folder with reference movies file.   

