# import important libraries:
import numpy as np
import cv2 as cv

class MotionDetection:
    # static function for motion detection:
    @staticmethod
    def TrackMotion(posX1, posY1, posX2, posY2, milTracker, videoOne, videoTwo, rssimulCam):
        # initialise bounding boxes using user input positions and default size of 86
        boundBox1 = (posX1, posY1, 86, 86)
        boundBox2 = (posX2, posY2, 86, 86)
        # initialise MIL tracker objects based on bounding boxes and the two motion videos
        trackInit1 = milTracker.init(videoOne, boundBox1)
        trackInit2 = milTracker.init(videoTwo, boundBox2)

        trackInit1, boundBox1 = milTracker.update(videoOne)
        trackInit2, boundBox2 = milTracker.update(videoTwo)
        # if MIL tracker has bounding box co-ordinates
        if(trackInit1 and trackInit2):
            # find bounding box corners based on shape and convert co-ordinates to int
            ptx1 = (int(boundBox1[0]), int(boundBox1[1]))
            ptx2 = (int(boundBox1[0] + boundBox1[2]), int(boundBox1[1] + boundBox1[3]))

            pty1 = (int(boundBox2[0]), int(boundBox2[1]))
            pty2 = (int(boundBox2[0] + boundBox2[2]), int(boundBox2[1] + boundBox2[3]))
            # draw rectangle based on bounding box co-ordinates on main SimulCam window
            cv.rectangle(rssimulCam, ptx1, ptx2, (0,255,0), 2, 1)
            cv.rectangle(rssimulCam, pty1, pty2, (0,255,0), 2, 1)
            # find the top left corner co-ordinates for each box
            x1 = ptx1[0]
            y1 = ptx1[1]
            x2 = pty1[0]
            y2 = pty1[1]
            # draw line on main SimulCam window starting at top left corner
            cv.line(rssimulCam, (posX1, posY1), (x1,y1), (0,0,255), 2)
            cv.line(rssimulCam, (posX2, posY2), (x2,y2), (0,0,255), 2)
            # find Euclidean distance of the line drawn
            length1 = cv.norm((posX1, posY1), (x1, y1))
            length2 = cv.norm((posX2, posY2), (x2, y2))
            # display the Euclidean distance in text on the main SimulCam window
            cv.putText(rssimulCam,'Eucl Distance 1: ' + str(length1), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            cv.putText(rssimulCam,'Eucl Distance 2: ' + str(length2), (50, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            
            cv.imshow('simulcam', rssimulCam)
        else:
            print("No motion has been detected.")
