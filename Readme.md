# Attendance System using facial recognition
### Duration: May '22 - June '22

## Project Overview
The Facial Recognition Student Attendance System developed during the Microsoft Engage program is an innovative application designed to simplify the attendance tracking process in educational institutions. This system leverages facial recognition technology to identify and mark student attendance automatically, making attendance management more efficient and accurate. In addition to attendance tracking, the system includes interactive features like automatic sketch creation and real-time facial emotion recognition to enhance the user experience.

## Features
### User Interface and Data Storage
* Developed a user-friendly application using Tkinter for the graphical user interface (UI).
* The application allows the capture of student data, including name, roll number, and email.
* Implemented efficient data storage and retrieval using a MySQL database.
### Facial Recognition
* Utilized OpenCV for real-time face detection.
* Employed Haarcascade for accurate face detection in images.
* Integrated the LBPH (Local Binary Patterns Histograms) algorithm for precise face recognition.
* Student details, including their name, roll number, and email, are displayed over their faces once recognized.
### Automatic Attendance
* The system auto-marks attendance as students are recognized by the facial recognition component.
* This eliminates the need for manual attendance recording, saving time and reducing errors.
### Interactive Games
* Developed compelling games as part of the system, enhancing user engagement.
* Features automatic sketch creation, allowing students to express their creativity.
* Real-time facial emotion recognition in games adds an interactive element.
## Technologies Used
* Tkinter: For building the graphical user interface.
* OpenCV: For face detection and LBPH algorithm-based face recognition.
* NumPy: For numerical operations on image data.
* Haarcascade: For accurate face detection.
* MySQL: For efficient data storage and retrieval.
## Getting Started
### To use the Facial Recognition Student Attendance System, follow these steps:

* Clone the GitHub repository.
* Install the required dependencies (Tkinter, OpenCV, NumPy, MySQL).
* Configure the MySQL database for data storage.
* Run the application and explore the features.
## Future Enhancements
### Future enhancements for this system may include:

* Integration with more advanced deep learning-based face recognition models for increased accuracy.
* Implementation of user authentication for security.
* Enhancement of the game features to provide a more interactive learning experience.

## Contact Information
### For any inquiries or support, please contact the project maintainer:

* Name: Anmol Gupta, IIT Kanpur
* Email: ****
## You-Tube video for Project Explaination
* https://www.youtube.com/watch?v=09ZSkKOIS1o&t=1s
## How to clone and library in python need to install
* Use python 3.9
* Python libraries used so it need to install in the system
    pip install numpy
    pip install opencv-python / pip install opencv 
    pip install opencv-contrib-python
    pip install scipy
    pip install mysql-connector-python
    pip install pygame
    pip install mediapipe
    pip install matplotlib
    pip install scikit-learn
    pip install DateTime
    pip install strftime
    pip install pandas

## To use the attendance system in any system one should have to follow the following steps-
* MySQL should be there in the system contains -> MySQL workbench 8.0 CE ,MySQL shell etc
* Create a database as 'sys', host='localhost',username='root',password='Isha@41820'
* Then need to run all the sql file ->'sys_student.sql','sys_routines', 'sys_sys_config' prensent in the database folder  (contain the table)

* This will lead you to a table name 'student' in the database name 'sys' then you can easly run the code with no mysql connector error or no database 'sys' found in your local machine.

* All the folders and files should be systematic present (as the in the github) in the folder name 'Face_Recognition_System' in the desktop . 

* Then you need to run 'login.py' to run the Attendance system using face recognition .  
* If in any case 'login.py' doesn't work so open 'intro1.py'  
