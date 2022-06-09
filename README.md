# INDUSTRTIAL-LAB
IMAGE BRIGHTENING

To run the program,

1. Make sure you have Python installed (at least 3.5, 3.8+ is recommended)

run the following command to install the necessary packages.

pip install -r requirements.txt.


run the Python file to start the program.
You will be prompted with a window to choose an image file.
You can adjust the brightness by changing the value of *brightness* variable on line 36.


FACE DETECTIONS
import open cv libraries as cv2.
firstly run create_data.py to capture your face for data to train model with the camera.
cascade haar face recognition files are initialized for face recogintion using default files in the open default face recogniton data.
a denotaition for the face recognition files are made as cascade_path.

with the assertion of the previous codes, cap.read is used to read frames from the camera connected to the computer.
the read image is converted to monochrome color space.

the initialized face cascade files are used to identify human faces in each frame produced by the camera.

the identified faces are places into a square with specified demensions, color and thickness, green in this case.

cv2.imshow command is used to display the resulting image recognition process in a window named image.

the window waits for the press of key 'x' before breaking the while true function to keep displaying the camera view finder.

cap.release() releases the camera device from use and cv2. destroyALLWindows() terminates all active windows.
then run face_detection.py to detect your face
