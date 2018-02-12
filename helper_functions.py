import numpy as np
import matplotlib.pyplot as plt
import glob
import cv2
import math


def get_calibration_images(path="camera_cal/*.jpg"):
    calibration_images = []
    for img_name in glob.glob(path):
        # Load all the images in grayscale
        calibration_images.append(
            cv2.cvtColor(cv2.imread(img_name), cv2.COLOR_BGR2GRAY))
    return calibration_images


def calibrate_camera(images, chessboard=(8, 6), return_rotation=False,
                     return_translation=False):
    print("Calibrating camera..")
    obj_points = []
    img_points = []

    # Prepare object points for each point of the chessboard in 3d space
    # First point will be [0,0,0](xyz) and the last will be (7,5,0)
    objp = np.zeros((chessboard[1] * chessboard[0], 3), np.float32)

    # For the first 2 columns (x and y) fill in the coordinates
    # numpy's mgrid function returns all the coordinates for the given grid size
    # finally we reshape the coordinates back into two columns (x and y)
    # Check the video "Calibrating Your Camera" for an explanation
    objp[:, :2] = np.mgrid[0:chessboard[0], 0: chessboard[1]].T.reshape(-1, 2)

    for image in images:
        # Find the corners
        found, corners = cv2.findChessboardCorners(image, chessboard, None)

        if found == True:
            img_points.append(corners)
            obj_points.append(objp)

    # Calibrate the camera with the found points
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points,
                                                       images[0].shape[::-1],
                                                       None, None)
    print("Camera calibration done!")
    # Return the values
    if return_rotation is True and return_translation is True:
        return mtx, dist, rvecs, tvecs

    elif return_rotation is True:
        return mtx, dist, rvecs

    elif return_translation is True:
        return mtx, dist, tvecs

    else:
        return mtx, dist


def undistort_image(image, camera_matrix, distortion_matrix):
    return cv2.undistort(image,camera_matrix, distortion_matrix, None, camera_matrix)