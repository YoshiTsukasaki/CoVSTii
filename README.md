## Computer vision image registration algorithm in CoVSTii
Computer vision image registration algorithm in CoVSTii is a LabVIEW software to correct image motion displacement and deformation of time-lapse microscope image sequences. The inputs of the software are one or multi-channel video files (AVI). Stand-alone installer of the software is also available using the link (https://uofi.app.box.com/v/stand-aloneCoVSTii) which is a zip-file including the installation files, instructions, and a sample dataset.

Image processing of Computer vision image registration algorithm consists of four distinct steps: (i) feature points detection, (ii) motion tracking, (iii) motion correction and (iv) frame averaging.
Using the Shi and Tomasi method, the software detects feature points, which are the 'corners' changing rapidly in intensity in the reference image. The software tracks the feature points from the reference image to the paired image using Lucas Kanade optical flow analysis, the algorithm estimating the motion vector between frames. These feature point pairs are then used to calculate a homography matrix, which defines the geometric transformation of the paired images. This perspective transformation matrix is used for motion correction. Furthermore, to reduce the oscillatory motion, the software averages specified frames.

### 1. System requirements
a)	Windows 10/8.11/7 SP1.  
b)	Pentium 4 G1 equivalent (Intel i5 equivalent or higher recommended).  c)	4 GB disk space.  d)	4 GB RAM (You may need more RAM for large datasets).  e)	.NET Framework 4.6.  f)	1024 x 768 resolution (1366 x 768 or higher recommended).  g)	We recommend 32-bit LabVIEW 2017 17.0f2 or newer on Windows 7 or newer.  h)	LabVIEW add-on modules.  i)	Vision Development Module 2017 or newer (required by image processing in LabVIEW).  j)	Enthought Python Integration Toolkit for LabVIEW 1.2.0 or newer (required by Python-OpenCV function in LabVIEW).  k)	Python 2.7.13 or newer (required by Python-OpenCV function in LabVIEW) with following packages.  i)	mkl 2017.0.1-2 or newer.  ii)	numpy 1.11.3-2 or newer.  iii)	opencv 2.4.9-5 or newer (required by Python-OpenCV function in LabVIEW)

### 2. Installation
a) LabVIEW
Installing LabVIEW and LabVIEW add-on modules and python and python modules.
To install LabVIEW go to https://www.ni.com/en-us/shop/labview/select-edition.html.
You may need to create an NI account to be able to purchase and download LabVIEW VI Package Manager (VIPM). Using VIPM you can choose the required modules and packages to be installed with your LabVIEW software.

b) Computer vision image registration algorithm
To download our computer vision image registration algorithm, go to the GitHub releases page, https://github.com/YoshiTsukasaki/CoVSTii.
Option 1: You can download the whole GitHub directory into your computer by clicking on “Code” and then “Downlod ZIP”. This will put all the files in a zip file named “CoVSTii-main.zip” that you can extract and use (you can go the next step if you choose this option).
Option 2: The other way is to download the following files, separately,
-'Computer vision image registration algorighm full_Open Source.llb' and 
-'Perspective trasform.py'.
You may put both files in a folder in your working directory. Also, in the GitHub page, there are three sample AVI files that you can download to test the application.

### 3. Running the application
Here are the step by step instructions to open and load computer vision image registration algorithm:
a)	Open LabVIEW and click on “Open Existing”.
b)	Locate the downloaded LLB file (“Computer vision image registration algorighm full_Open Source.llb”), choose it, and press “OK”.
c)	A window may appear for selecting the “vi” file. Choose “Computer vision image registration algorighm full_Open Source.vi”, and press “OK”.
d)	The “vi” file will automatically load the required modules and packages and the program interface will appear.

a) Open LabVIEW and click on “Open Existing”.


b) Locate the downloaded LLB file (“Computer vision image registration algorighm full_Open Source.llb”), choose it, and press “OK”.
To download our computer vision image registration algorithm, go to the GitHub releases page, https://github.com/YoshiTsukasaki/CoVSTii.
Option 1: You can download the whole GitHub directory into your computer by clicking on “Code” and then “Downlod ZIP”. This will put all the files in a zip file named “CoVSTii-main.zip” that you can extract and use (you can go the next step if you choose this option).
Option 2: The other way is to download the following files, separately,
-'Computer vision image registration algorighm full_Open Source.llb' and 


### Naming the Input files
The current version of our software only accepts AVI files. At least one AVI file is needed to be fed to the software. If you have more channels, you need to name them in accordance to the reference channel. For example, if the reference channel is named “Sample-Ch1.avi”, the other channels should be named as “Sample-Ch2.avi”, Sample-Ch3.avi, …. (“Sample-”) in the same folder with reference movie. Please note that the software stabilizes your data based on the reference channel.

### Parameter description
Before executing the application, you may change the following parameters:
(i)	“Tracking”: (Default value is “on”) You can turn off or on the illustration of the optical flow tracking algorithm. This doesn’t affect the stabilization procedure.
(ii)	“Setting feature point number”: (Default value is “500”) This parameter defines the number of feature points extracted to be used in the optical flow tracking algorithm. You may increase this value if your data has a lot of deformations.
(iii)	“Optical Flow Setting”: These settings specify the options that are used to track features between two successive frames.
a.	“Level”, (Default value is “6”), specify the number of pyramid levels to use. Higher level values help to track larger motions, but costs more running time.
b.	“Max. Iterations”, (Default value is “20”), identifies the maximum number of iterations in the optimization step of the tracking algorithm at each level. The higher this value, the more accurate stabilizations; but costs more running time. 
c.	“Window Size”, n, (Default value is “30”), defines the size (n×n) of the patch window around each feature point that is used to search for a match. You may increase this value if your data has big motions.
d.	“Displacement Threshold”, (Default value is “0.1”), defines the minimum allowed displacement between the location of the tracked features from iteration to iteration. So, if the position of a feature point does not move more than the “Displacement Threshold” from its previous location, its current location is finalized and not tracked anymore. The lower this value, the more accurate stabilizations; but costs more running time.
(iv)	“Average frame number”, (Default value is “14”), is used to down-sample the output files by averaging the specified number of frames.

### Run the application
To run the application, you can either select “Run” from the “Operate” menu or click on the white arrow. A window opens to select the reference channel. You can choose “Sample-Ch1.avi” from our provided sample data in the “test” folder. The program will start doing the stabilization process and save the results in the same folder. 
For each input channel, there will be three outputs: 
1)	“…-Stabilize.avi”, which is the stabilized video of the input, 
2)	“…-Stabilize_NorAve.avi”, which is the down-sampled version of the stabilized output (based on the parameter “Average frame number”), and 
3)	“…-Ch1_NorAve.avi”, which is actually the down-sampled version of the input (used for comparison).
To stop the operation, you can either select “Stop” from the “Operate” menu or click on the red circle.
