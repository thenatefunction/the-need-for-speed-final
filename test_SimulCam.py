# import important libraries and classes:
import pytest
from CameraCalib import CameraCalib
from FeatureMatching import FeatureMatching
from MotionDetection import MotionDetection

class test_SimulCam:
    # test 1 for camera calibration:
    @staticmethod
    def test_CameraCalibrationOne(pathToCalibPhotos):
        if not (pathToCalibPhotos):
            raise TypeError('Please provide a list argument.')
        else:
            print("Test 1 for camera calibration passed.")
    # test 2 for camera calibration:
    @staticmethod
    def test_CameraCalibrationTwo(pathToCalibPhoto):
        if pathToCalibPhoto is None:
            raise TypeError('Please provide an array argument.')
        else:
            print("Test 2 for camera calibration passed.")
    # test 1 for feature matching:
    @staticmethod
    def test_PerformFeatureMatchingOne(grayBlur1):
        if grayBlur1 is None:
            raise TypeError('Please provide an array argument.')
        else:
            print("Test 1 for feature matching passed.")
    # test 2 for feature matching:
    @staticmethod
    def test_PerformFeatureMatchingTwo(grayBlur2):
        if grayBlur2 is None:
            raise TypeError('Please provide an array argument.')
        else:
            print("Test 2 for feature matching passed.")
    # test for motion detection bounding box user input positions:
    @staticmethod
    def test_BoundingBox(posX1, posY1, posX2, posY2):
        if not isinstance(posX1, int):
            if not isinstance(posY1, int):
                if not isinstance(posX2, int):
                    if not isinstance(posY2, int):
                        raise TypeError('Please provide an integer argument.')
        else:
            print("Test for motion detection bounding box user input positions passed.")
            
    
    
    
