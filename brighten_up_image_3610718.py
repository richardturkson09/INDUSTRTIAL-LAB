import cv2
# from tkinter import Tk for Python 3.x
from tkinter import Tk     
from matplotlib import pyplot as plt


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

if __name__ == '__main__':
    from tkinter.filedialog import askopenfilename

    # we don't want a full GUI, so keep the root window from appearing
    Tk().withdraw()

    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename()

    # The function imread loads an image
    # from the specified file and returns it.
    original = cv2.imread(filename)

    # Making another copy of an image.
    img = original.copy()

    # Brightness range from 0 to 255
    # Change the value to adjust brightness
    brighteness = 100
    brightened = increase_brightness(img, brighteness)

    plt.subplot(121),plt.imshow(original),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(brightened),plt.title('Brightened')
    plt.xticks([]), plt.yticks([])
    plt.show()
