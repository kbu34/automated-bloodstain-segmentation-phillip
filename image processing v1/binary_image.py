import cv2
import numpy as np
import sys
import time
from matplotlib import pyplot as plt
import bloodstain

def main():
    t0 = time.time()
    img_original = cv2.imread('./images/' + sys.argv[1])
    
    hsv_img = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
    # plt.hist(hsv_img.ravel(), 256, [0, 255])
    # plt.xlim([0, 360])
    # plt.show()
    blur = cv2.GaussianBlur(img_original, (3,3), 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    gray_hsv = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)

    thresh = binarize_image(img_original, gray, gray_hsv, hsv_img)
    hist = cv2.calcHist( [gray_hsv], [0], None, [256], [0, 256] )
    remove_circle_markers(gray, thresh)

    label_stains(thresh)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img_original, contours, -1, (0,0,255), 3)
    analyseContours(contours, img_original)

    t1 = time.time()
    labels = label_stains(thresh)
    

    display_result(img_original)

  #  cv2.imwrite(sys.argv[1] + ".mask", thresh)
    cv2.imwrite(sys.argv[1] + "_annotation.jpg", img_original)


def label_stains(thresh):
    ret, labels = cv2.connectedComponents(thresh)

    label_hue = np.uint8(179 * labels / np.max(labels))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    labeled_img[label_hue==0] = 0

    return labels


def analyseContours(contours, img_original):
   # area = float('inf')
    count = 0
    for cnt in contours:
        stain = bloodstain.Stain(cnt)
        stain.draw_ellipse(img_original)
        stain.annotate(img_original)
        if stain.ellipse:
          #  angle = stain.ellipse[2]
            count += 1 
            #  print("gamma ", angle)        

    #print("min area:", area)
    print("ellispe count: ", count)


def display_result(img_original) :
    while True:
        # plt.hist(hsv_img.ravel(), 256, [0, 255])
        # plt.xlim([0, 360])
        # plt.show()
        small = cv2.resize(img_original, (0,0), fx=0.25, fy=0.25)
        cv2.imshow('Blood Spatter', small)
        
        if cv2.waitKey(100) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def remove_circle_markers(gray, img):
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100,
                                param2=58, minRadius=24, maxRadius=82)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img, (i[0],i[1]),i[2] + 10, (0,0,0), -2)


def binarize_image(img_original, gray, gray_hsv, hsv_img) :

    ret, thresh = cv2.threshold(gray_hsv, 0, 255, cv2.THRESH_OTSU)

    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(thresh, kernel, iterations = 2)
    dilation = cv2.dilate(thresh, kernel, iterations = 2)

    return dilation


if __name__ == '__main__':
    main()