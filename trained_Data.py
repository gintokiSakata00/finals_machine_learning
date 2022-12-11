import string
from timeit import default_timer as timer
import cv2
import numpy as np 
start = timer() #timer starts
img_width, img_height= 30,40
# char_Small= [*string.ascii_lowercase]
# char_Big= [*string.ascii_uppercase]
# num = [*string.digits]
def path_loc (a): #pathlocation for letters 
    if a.isdigit():
        return f"./test_numbers/{a}.jpg"
    else:
        return f"./small/{a}.jpg" if a.islower() else f"./big/{a}.jpg"
def main_function(char,ascii_value):
    char_int_classified =[]
    flat_char_img = np.empty((0, img_width* img_height))
    for x in char:
        char_imread = cv2.imread(path_loc(x))
        char_gray = cv2.cvtColor(char_imread, cv2.COLOR_BGR2GRAY)
        return_A, char_thresh = cv2.threshold(char_gray, 150,255,cv2.CHAIN_APPROX_NONE)
        thresh_copy = char_thresh.copy()
        con_char, hB = cv2.findContours(thresh_copy,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        countA=0
        for iter in con_char:
            [intX, intY, intW, intH ]=cv2.boundingRect(iter)
            char_img_roi = char_thresh[intY: intY+intH,intX:intX+intW ]
            resize_img_roi = cv2.resize(char_img_roi,(img_width,img_height))
            countA +=1
            char_int_classified.append(ascii_value)
            flat_img = resize_img_roi.reshape(1,img_width*img_height)
            flat_char_img = np.append(flat_char_img,flat_img,0)
        print(f"Char :{x}\t\tCountour:{countA}\t\tChar_value : {ascii_value}")
        ascii_value+=1
        countA+=1
    classifications_img = np.array(char_int_classified, float) #np.float
    classifications_final_img= classifications_img.reshape(classifications_img.size,1)    
    np.savetxt("char_classifications.txt", classifications_final_img)
    np.savetxt("flat_char_img.txt",flat_char_img)
# num = ['1','2','3','4','5','6','7','8','9']
# char_Big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# main_function(num,48)
# main_function(char_Big,65)
SMALL = ["a","b","c","d"]
main_function(SMALL,97)
BIG = ["A","B","C","D"]
main_function(BIG,65)

print("Complete!!!")
end = timer()
print(f"Time Execution: {end-start}")