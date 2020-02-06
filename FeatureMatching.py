# import important libraries:
import numpy as np
import cv2 as cv

class FeatureMatching:
    # static function for performing feature matching on the video input:
    @staticmethod
    def PerformFeatureMatching(grayBlur1, grayBlur2):
        # create orb object
        orb = cv.ORB_create()
        try:
            # find key points and descriptors
            kp1, des1 = orb.detectAndCompute(grayBlur1, None)
            kp2, des2 = orb.detectAndCompute(grayBlur2, None)
            # initialise brute force matcher and match descriptors
            matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

            rawMatches = matcher.match(des1, des2)
            # sort matches based on distance
            dmatches = sorted(rawMatches, key = lambda x:x.distance)
            # draw matches
            matches = cv.drawMatches(grayBlur1,kp1,grayBlur2,kp2,dmatches[:10],None,flags=2)
            rsmatches = cv.resize(matches, (1280, 720))

            cv.imshow('matches', rsmatches)
            # find key point matrixes
            p1  = np.float32([kp1[m.queryIdx].pt for m in dmatches]).reshape(-1,1,2)
            p2  = np.float32([kp2[m.trainIdx].pt for m in dmatches]).reshape(-1,1,2)
            # if key point matrixes are not null fetch and estimate affine transformation matrix
            if(p1.size != 0 and p2.size != 0):
                H, _ = cv.estimateAffinePartial2D(p2, p1, cv.RANSAC, ransacReprojThreshold=5.0)
                # slice to find translation matrix only
                H2 = H[:,2]
                M = np.float32([[1,0,H2[0]],[0,1,H2[1]]])
                # return translation matrix
                return M
            else:
                print("Please check that the input video exists within the project.")
                return None
        except:
            print("Please check that the input video exists within the project.")
            return None

        

        
