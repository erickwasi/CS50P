# **CSS50P Final Project**
### Video Demo Link: ###
#

### **Medical Database implemented in Python3**
### By Eric Ayivor 

#### **Introduction to the Project**
#

This project is my implementation of a medical-style database with capabilities for adding new data, editing existing data, viewing the database renderered using ASCII art, searching by name, telephone number or date of birth, exporting to a CSV file and even deleting data. Deleting requires "administrator access", governed by a password which is currently 123456.

Originally, I used a 2D array to keep track of the database, however, when the program was rerun, the database defaulted to its original assignment. To deal with this I created the export function. This function converts the database to a csv file and saves it. When the file is rerun, the csv file is re-imported and converted back to a 2D array.

To create this project I made use of several packages: tabulate, datetime, sys and csv.

This project contains several files. The main file is project.py, which contains the source code for the project. test_project.py contains three (3) test functions accompanying project.py. database.csv is a CSV file which handles the database. It can be used to export the database at any time with the project.export() function, and also is used to save the database and store it until the program is rerun. Requirements.txt contains details of all the pip-installable libraries required to run this program. LICENSE contains details of this project's license (MIT License).

#
#### **License**
#

MIT License

Copyright (c) 2023 Eric Ayivor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.