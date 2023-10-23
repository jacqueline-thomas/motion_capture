import cv2

#capture one frame (image) from webcam
#create an object from the VideoCapture class to capture images from external webcam.
#then capture an image (aka, one frame of video) and save the image in a variable called "frame" 


input = print("press 'esc' to quit image display")
cap = cv2.VideoCapture(1) #0 is embedded webcam

keypressed = 1
while keypressed != 27:
    ret, frame = cap.read()
    cv2.namedWindow("image display") #create window for image to be placed
    cv2.imshow("image display", frame) #show image on window 
    cv2.waitKey(1) #display forever
if keypressed == 27: 
    cv2.destroyAllWindows()
    cv2.waitKey(1) #needed by macs to complete destroyAllwindows()
    
cap.release() #releases webcam from this code
