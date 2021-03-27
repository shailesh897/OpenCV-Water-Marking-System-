# OpenCV-Water-Marking-System-
This  project takes images and adds water mark of your choice

OpenCV Project- 
A Digital Watermarking System
Digital watermarking is the process of embedding watermarks into digital content such as images, audio, video, etc., and in this tutorial we are going to create a watermarking project for images using Python OpenCV and Tkinter.

Below are the steps to implement the project:
1. Import the required libraries-

import cv2
import os
import tkinter
from tkinter import *
from tkinter import filedialog


First, we are going to import all the modules and libraries that we are going to need in the project.For image reading and Writing we need openCV ,for GUI we need tkinter,for dealing with directory we need os module.
2. Define a function for drawing watermark-
def draw_watermark(watermark_path,image_path):

    watermark = cv2.imread(watermark_path)
    cv2.imshow("Watermark",watermark)
    image = cv2.imread(image_path)
    cv2.imshow("Photo",image)
    h_watermark, w_watermark, _ = watermark.shape
    h_image, w_image, _ = image.shape
    
    center_Y,center_X = h_image // 2,w_image // 2
    top_Y = center_Y - h_watermark // 2
    left_X = center_X - w_watermark // 2
    bottom_Y = top_Y + h_watermark
    right_X = left_X + w_watermark
    
    # Getting the  region (where watermark will go)
    region = image[top_Y: bottom_Y, left_X: right_X]

    # Adding the watermark to the region
    result = cv2.addWeighted(region, 1, watermark, 0.3, 0)

    # Replacing the region in the image
    image[top_Y: bottom_Y, left_X: right_X] = result
    
    # Getting filename and saving the image
    image_file_name = os.path.basename(image_path)
    cv2.imwrite("watermarked_" +image_file_name, image)
    print(image_file_name)
    watermarked=cv2.imread("watermarked_"+image_file_name)
    cv2.imshow("Watermarked Image",watermarked)
    print("Watermark is applied successfully")


This will show the image and watermark then it gets the central region  on the image where the watermark should be shown.
Then we will add the region with the watermark using cv2.addWeighted (). This is the core of the watermark effect. 
Using the addweighted() function we can choose to give opacity to the watermark so that it looks nice and smooth when placed over the image.Then we will save the file and show the file.

3. Define a function to get directories of the image file-  
def get_dir(text_widget):
   input = filedialog.askopenfile(initialdir="/")
   text_widget.delete(0,"end")
   text_widget.insert(0, input.name) 
   print(input.name)


This function accepts the tkinter's text widget object,opens the file selection  and sets the directory of the selected file to the text widget.

4. Define the main function-
def main():
    base = Tk()
    base.geometry('200x200')# Create a canvas
    T1 = tkinter.Entry(base)# Text widget
    T1.pack()
    
    b1 = Button(base, text ='Photo', command = lambda:get_dir(T1))# Button label
    b1.pack()
    
    T2 = tkinter.Entry(base)# Text widget
    T2.pack()  # Button label
  
    b2 = Button(base, text ='Watermark', 
                command = lambda:get_dir(T2))
    b2.pack()
    
    b3 = Button(
                base, text ='Add Watermark', 
                command = lambda:draw_watermark(T2.get() ,T1.get())
                )
    b3.pack()
    mainloop() 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 


This contains the for a basic GUI which looks like this:

And this main function calls all the previously defined functions.

5. Calling the main function-
if __name__=="__main__":
    main()











