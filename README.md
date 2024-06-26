# DroidInspect

## About
DroidInspect is a lightweight test input generator for Android.
It can send random or scripted input events to an Android app, achieve higher test coverage more quickly, and generate a UI transition graph (UTG) after testing.


DroidInspect has the following advantages as compared with other input generators:

 The purposes of this document are: 

     Identify and analyze the requirements
     Design the test plan 
     Reduce the development effort 
     Improve understanding
     Store Information in Database.

The scope of this project is defined below: 

  ● The apk file for the android app to be tested will be provided.
  ● The tool will not require any source code of the app to be tested. 

The assumptions of the project are: 

● Android device connected to the computer and accessible via USB 
● All permissions are granted 
● Valid inputs are given with correct label 
● Disabled notifications, auto-rotation, flight mode, and enabled mobile data and           Wi-Fi 
● Biometric and face-recognition inputs will not be considered



**## Prerequisite##**

1. `Python` (both 2 and 3 are supported)
2. `Java`
3. `Android SDK`
4. Add `platform_tools` directory in Android SDK to `PATH`
5. (Optional) `OpenCV-Python` if you want to run DroidBot in cv mode.


## How to use

1. Make sure you have:

    + `.apk` file path of the app you want to analyze.
    + A device or an emulator connected to your host machine via `adb`.


2. How to Run.

   
   Execute commands :
   
      --> Python .\start.py -a <<Path_of_apk>> -o output

   Or
      Run the code with :
   
      --> python gut2.py
       

![IMG_4207-removebg-preview](https://github.com/Nasir-1310/DroidInspect/assets/113335416/9db75517-b06e-44ae-8c81-9a60b8da5340)

