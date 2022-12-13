
# MACHINE LEARNING
A basic machine learning that automatically checks test paper and also write scores in the image. It scans jpeg picture contains student tests do scan and check if the student inputs matches the given answer and then give scores afte a test.

### Sample Test Paper
![this is demo](/demo_test.jpg)
### Scanning every answer
![this is demo](/demo_scan.jpg)
### Add scores on a new Written Image
![this is demo](/demo.jpg)

## HOW TO RUN

### Step 1: Trained Data
```
RUN: py ./trained_data.py
    This will scan all the images in the respective folder 
    and scanned all pictures to train the program
```    
### Step 2: Assign Answer Key
```
 Check the line 27, the program will ask for answer keys 
 or you can manually define the password by declaring the
 value of the answer key.
``` 
### Step 3: Check the test paper
```
RUN:  py ./test_data.py 
    This will scan the test folder where the test
    papers are located and will perform checkings 
    found on the check_test_paper folder
```    
### Step 4: Check extracted values from each test paper (*Optional*)
```
    The program automatically check and put scores on the 
    new image but you can manually scan each test paper 
    for back tracking characters of the test paper. 
    To do that remove the comment '#' symbol from 
    the line 72 and 73 of test_data.py file.
Done:
    Then all are done, Thank you.
```
## Author
GILLBERT PADON

