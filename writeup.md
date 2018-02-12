#  Project: Advanced lane finding

In this project, we are challenged to improve on the first lane finding project.
We are given images and video's, taken from a camera in the center of a car. From this data, we are asked to detect the lane line we are in.

The code I implemented can be found here:

https://github.com/kkalera/CarND-Advanced-Lane-Lines/blob/master/Untitled.ipynb

This code works good on the project video, but fails on the challenge video's. I'm going to try and implement a few different approaches to solving this at a later time.

## The steps I took:

 - Camera calibration

 - Calibrating the images

 - Using different color chanels, sobel and gradients to get a binary image.

 - Transform the image into a top-down or birds-eye view image.

 - Calculate which of the pixels make up the lane line

 - Calculate the radius of the lane line in meters

 - Calculate the vehicle's position on the lane line

 - Draw the polygon that make's up the lane on the image

 - Transform the image back to the original view

 - Overlay the information on the image.

   ​

 ### Camera Calibration:

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

I started off by loading the calibration images into memory. In this case we had 20 images of a checkered board with 9x6 squares.

I then created a function that takes in an array of calibration images, the shape of the checkered board and two booleans. One for returning the rotation vector and one for returning the translation vector.

The function takes the following steps:

- Prepare an array for the object points and define these points using np.mgrid function
- For each image, find the corners of the chessboard using opencv's "findChessboardCorners" function.
- With the corners found, use opencv's "calibrateCamera" function to get the camera matrix, distortion matrix, rotation vectors and translation vectors

This is a result of that function:

![](writeup_images/chessboard_calibration.png)

### Pipeline (single images)

#### 1. Provide an example of a distortion-corrected image.

To demonstrate this step, I will describe how I apply the distortion correction to one of the test images like this one:
![alt text](writeup_images/image_undistorted.png)

#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image. Provide an example of a binary image result.

The first step was converting all the images to grayscale. (Code found in the notebook at 2.3: Convert to grayscale).

This produces the following result:

![alt text](writeup_images/image_gray.png)

After that, I applied Sobel and gradients to the image and used those to apply thresholding to get a binary image. (Code found in the notebook at 2.4: Thresholding)

This function produces the following result:

![alt text](writeup_images/image_thresholded.png)

