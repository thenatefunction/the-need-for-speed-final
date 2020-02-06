# opencv version: opencv-contrib-python==3.4.2.16
# author: nathaniel mcparland
# import important libraries and classes:
import numpy as np
import cv2 as cv
import glob
from CameraCalib import CameraCalib
from FeatureMatching import FeatureMatching
from MotionDetection import MotionDetection
from test_SimulCam import test_SimulCam

# chessboard calibration images stored in folder: 'chessboard'
pathToCalibPhotos = glob.glob('chessboard\*.jpg')
# one image in folder 'chessboard' must have the name: 'calibCam.jpg'
pathToCalibPhoto = cv.imread('chessboard\calibCam.jpg')
mtx, dist, optCamMtx = CameraCalib.CameraCalibration(pathToCalibPhotos, pathToCalibPhoto)

# *** run tests on CameraCalibration static function ***
test_SimulCam.test_CameraCalibrationOne(pathToCalibPhotos)
test_SimulCam.test_CameraCalibrationTwo(pathToCalibPhoto)

background1 = cv.VideoCapture('v1a.mp4')
background2 = cv.VideoCapture('v2a.mp4')
M = None

try:
    while(True):
        ret1, frame1 = background1.read()
        ret2, frame2 = background2.read()
        # undistort frames
        dst1 = cv.undistort(frame1, mtx, dist, None, optCamMtx)
        dst2 = cv.undistort(frame2, mtx, dist, None, optCamMtx)
        # resize to 720p HD videos should all be in this format as input
        backgroundOne = cv.resize(dst1, (1280, 720))
        backgroundTwo = cv.resize(dst2, (1280, 720))

        gray1 = cv.cvtColor(backgroundOne, cv.COLOR_BGR2GRAY)
        gray2 = cv.cvtColor(backgroundTwo, cv.COLOR_BGR2GRAY)

        grayBlur1 = cv.medianBlur(gray1,1)
        grayBlur2 = cv.medianBlur(gray2,1)
    
        M = FeatureMatching.PerformFeatureMatching(grayBlur1, grayBlur2)
        
        # *** run tests on PerformFeatureMatching function ***
        test_SimulCam.test_PerformFeatureMatchingOne(grayBlur1)
        test_SimulCam.test_PerformFeatureMatchingTwo(grayBlur2)
        
        break
except:
    print("Please make sure background videos 'v1.mp4' and 'v2.mp4' exist in the project folder.")
    background1.release()
    background2.release()
    
background1.release()
background2.release()

cameraOne = cv.VideoCapture('v3a.mp4')
cameraTwo = cv.VideoCapture('v4a.mp4')

milTracker = cv.TrackerMIL_create()

posX1 = int(input("Please enter position of bounding box X1. \n"))
posY1 = int(input("Please enter position of bounding box Y1. \n"))
posX2 = int(input("Please enter position of bounding box X2. \n"))
posY2 = int(input("Please enter position of bounding box Y2. \n"))

try:
    while(True):
        ret3, frame3 = cameraOne.read()
        ret4, frame4 = cameraTwo.read()

        dst3 = cv.undistort(frame3, mtx, dist, None, optCamMtx)
        dst4 = cv.undistort(frame4, mtx, dist, None, optCamMtx)

        videoOne = cv.resize(dst3, (1280, 720))
        videoTwo = cv.resize(dst4, (1280, 720))
        # warp video two based on the M matrix and video one's shape
        result = cv.warpAffine(videoTwo,M,(videoOne.shape[1],videoOne.shape[0]))
        # perform blending
        simulCam = cv.addWeighted(videoOne,0.5,result,0.5,0)
        rssimulCam = cv.resize(simulCam, (1280, 720))

        MotionDetection.TrackMotion(posX1, posY1, posX2, posY2, milTracker, videoOne, videoTwo, rssimulCam)

        # *** run test on position input for trackMotion function ***
        test_SimulCam.test_BoundingBox(posX1, posY1, posX2, posY2)
        
        # escape key press the escape key to exit the program
        esckey = cv.waitKey(27)
        if esckey == 27:
            break
except:
    print("Please make sure camera foreground videos 'v3.mp4' and 'v4.mp4' exist in the project folder.")
    cameraOne.release()
    cameraTwo.release()
    cv.destroyAllWindows()
cameraOne.release()
cameraTwo.release()
cv.destroyAllWindows()
        
    






    

