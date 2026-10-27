import cv2
import matplotlib.pyplot as plt 
import numpy as np

def display_image(title,image):
    plt.figure (figsize=(8,8))
    if len (image.shape)==2:
        plt.imshow(image,cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis ("off")
    plt.show()

def interactive_edge_detection(image_path):
    image=cv2.imread(image_path)
    if image is None:
        print("IMAGE NOT FOUND.")
        return 

    gray_image=(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY))
    display_image("Orignal gray scale image",gray_image)

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit") 

    while True:
        choice=input("Please select a number from 1-6. ")
        if choice ==1:
            sobel_x=cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=3)
            sobel_y=cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=3)
            combine_sobel=cv2.bitwise_or(sobel_x.astype(np.uint8),sobel_y.astype(np.uint8))
            display_image("Sobel Edge Detection",combine_sobel)

        elif choice==2:
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_thresh=int(input("Enter lower threshold: "))
            upper_thresh=int(input("Enter upper threshold: "))
            edges=cv2.Canny(gray_image,lower_thresh,upper_thresh)
            display_image("Canny Edge Detection",edges)

        elif choice==3:
            laplacian=cv2.Laplacian(gray_image,cv2.CV_64F)
            display_image("Laplacian Edge Detection",np.abs(laplacian).astype(np.uint8))

        elif choice==4:
            print("Adjust kernal size for gaussian blur (Must be blur,defult is 5)")
            kernal_size=int(input("Enter a kernal size: "))
            blurred=cv2.GaussianBlur(image,(kernal_size,kernal_size),0)
            display_image("Gaussian Smoothing",blurred)

        elif choice==5 :
            print("Adjust kernal size for median filtering (Must be blur,defult is 5)")
            kernal_size=int(input("Enter a kernal size: "))
            median_filter=cv2.medianBlur(image,kernal_size)
            display_image("Median Filtering",median_filter)

        elif choice==6:
            print("Exiting")
            break 
        else:
            print("Invalid input- ENTER NUMBER 1-6")

interactive_edge_detection('example.jpg')

        
            
          


            