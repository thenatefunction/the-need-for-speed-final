# import important libraries:
import numpy as np
import cv2 as cv

class CameraCalib:
    # static function for calibrating the video camera:
    @staticmethod
    def CameraCalibration(pathToCalibPhotos, pathToCalibPhoto):
        try:
            # setup variables
            criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            objp = np.zeros((6*7,3), np.float32)
            objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

            objpoints = []
            imgpoints = []

            for fname in pathToCalibPhotos:
                # read in each chessboard camera calibration image
                img = cv.imread(fname)
                gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                # find chessboard corners
                ret1, corners1 = cv.findChessboardCorners(gray, (7,6),None)
                # if corners are found then draw the corners
                if ret1 == True:
                    objpoints.append(objp)
        
                    corners2 = cv.cornerSubPix(gray,corners1,(11,11),(-1,-1),criteria)
                    imgpoints.append(corners2)

                    img = cv.drawChessboardCorners(img, (7,6), corners2,ret1)
                    cv.imshow('img',img)
                    cv.waitKey(500)
            cv.destroyAllWindows()
        except:
            print("Please ensure chessboard calibration images exist within the project.")
            cv.destroyAllWindows()
            
        try:
            # fetch camera calibration info
            ret2, mtx2, dist2, rvecs2, tvecs2 = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
            cam1base = pathToCalibPhoto
    
            h1, w1 = cam1base.shape[:2]
            # fetch undistorted image matrix
            newcameramtx, roi1=cv.getOptimalNewCameraMatrix(mtx2,dist2,(w1,h1),1,(w1,h1))
            # return all camera info and undistorted image matrix
            return mtx2, dist2, newcameramtx
        except:
            print("Please ensure the base photo exists and has been named correctly within the project.")
            return None

    
