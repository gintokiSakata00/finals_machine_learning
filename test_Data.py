import copy
import numpy as np
import cv2
import os
from timeit import default_timer as timer
start = timer()

path = "C:\\final_machine_learning\\test"
dir_list = os.listdir(path)
files_dir = []
for x in dir_list:
    length = len(x)
    # print(x[0:length-4]) # print filenames
    files_dir.append(x[0:length-4])
 
img_width = 30
img_height = 40
con_output =""
classified_char = np.loadtxt("char_classifications.txt", np.float32)
char_flat_images = np.loadtxt("flat_char_img.txt", np.float32)
classified_char = classified_char.reshape((classified_char.size,1))
knn_var = cv2.ml.KNearest_create()
KNearest_var = knn_var
knn_var.train(char_flat_images,cv2.ml.ROW_SAMPLE, classified_char)

names = files_dir
answer_key = "DADBCDACBC"
# user_input= input(str("How many files to checked :"))
user_input = 3
def path_loc (a): #pathlocation for letters 
    return f"./test/{a}.jpg"
def arrlop(a):
    arr = []
    for i in a:
        arr.append(i)
    return arr
def checker(a,b):
    counter= correct=0
    for i in a:
        if i.lower() == b[counter].lower():
            correct+=1
        counter+=1
    return correct
for i in names:
    test_paper = cv2.imread(path_loc(i)) 
    bilateral_filter = cv2.bilateralFilter(test_paper, 50 , 100 , 100)
    img_gray = cv2.cvtColor(bilateral_filter,cv2.COLOR_BGR2GRAY)
    return_val, theshold = cv2.threshold(img_gray, 150, 255, cv2.CHAIN_APPROX_NONE)
    thresh_Copy = theshold.copy()
    con, h = cv2.findContours(thresh_Copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    con_copy = copy.copy(con)
    con_character =""
    for c in con_copy:
        approx_cv = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c,True),True)
        if len(approx_cv)==4:
            if len(str(cv2.contourArea(approx_cv))) <6:
                pass
            else:
                [intX, intY, intW, intH] = cv2.boundingRect(approx_cv)
                cv2.rectangle(test_paper, (intX , intY), (intX+intW, intY+intH),(0,255,0),2)
                cv2.imshow('12123',test_paper) #show how boxes were scanned in the test paper
                cv2.waitKey(0) # wait for key press to continue
                img_to_char = theshold[intY:intY+intH, intX:intX+intW]
                img_to_char = img_to_char[5:60,5:60]
                invert_img = cv2.bitwise_not(img_to_char)
                return_vals,thresholds = cv2.threshold(invert_img,150,255,cv2.CHAIN_APPROX_NONE)
                cntr, h = cv2.findContours(thresholds,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for myc in cntr:
                    [intX, intY, intW, intH] = cv2.boundingRect(myc)
                    img = thresholds[intY:intY+intH, intX:intX+intW]
                    img_resize = cv2.resize(img, (img_width,img_height))
                    # cv2.imshow('12123',img_resize) #show the images and observe how characters were scanned
                    # cv2.waitKey(0) 
                
                    newResized = img_resize.reshape((1,img_width * img_height))
                    newResized = np.float32(newResized)

                    return_val,results,resp,dist = KNearest_var.findNearest(newResized,k=1)

                    get_char = str(chr(int(results[0][0])))
                    con_character = con_character + get_char
    image = cv2.imread(path_loc(i),cv2.IMREAD_UNCHANGED)
    position = (500,75)
    student_answer= arrlop(con_character[::-1])#reverse order of string
    answer_key = arrlop(answer_key) 
    scores = checker(answer_key,student_answer)
    scores = f"{scores}/{len(answer_key)}"
    cv2.putText( image, scores, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),3) 
    cv2.imwrite(f'./check_test_paper/{i}_checked.jpg', image)
    output = f"Name: {i}\nScore: {scores}"
    print(output)
    print(f"{i[0:7]}\t\t{student_answer}")
    print(f"Answer Key:\t{answer_key}")
    print()
    con_output +=output+"\n"
    con_output +="\n"
res = open("results", "w")
res.write("Results\n")
res.write(con_output)
res.close()
end = timer()
print(f"Time Execution: {end-start}")