import cv2
import os
import tkinter
from tkinter import *
from tkinter import filedialog

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
    
    # Get region
    region = image[top_Y: bottom_Y, left_X: right_X]

    # Add the watermark to the region
    result = cv2.addWeighted(region, 1, watermark, 0.3, 0)

    # Replace the region on the image
    image[top_Y: bottom_Y, left_X: right_X] = result
    
    # Get filename and save the image
    image_file_name = os.path.basename(image_path)
    cv2.imwrite("watermarked_" +image_file_name, image)
    print(image_file_name)
    watermarked=cv2.imread("watermarked_"+image_file_name)
    cv2.imshow("Watermaked Image",watermarked)
    print("Watermark is applied successfully")

def get_dir(text_widget):
   input = filedialog.askopenfile(initialdir="/")
   text_widget.delete(0,"end")
   text_widget.insert(0, input.name) 
   print(input.name)
  
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


if __name__=="__main__":
    main()