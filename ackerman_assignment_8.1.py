'''
File name - ackerman_assignment_8.1.py
Name - Tanner Ackerman
Date - 2/22/2022
Professor - Allen Voelcker
University - Bellevue
Assignment - Assignment 8.1
Description - This program will allow a user to create a new file and store it in a specified directory, if the directory doesn't exist than it will be created. The contents of the new file will include user input details.
'''

# Welcome the user to the program.
print("Welcome to the file creator program!")
print()

# Importing the os library.
import os

# Asking the user to input a directory path for the new file to be stored.__file__
directory_path = input("Please enter a directory path to store your new file: ")
print()

# Checking to see if the user input directory path exists.
isExist = os.path.exists(directory_path)

if not isExist:
  
  # Creating the new directory if it does not exist.
  os.mkdir(directory_path)
  print("The directory you input does not exist, but it has now been created!")
  print()

# Asking user to enter a file name including the file extension.
file_name = input("Please enter the name of the file you would like to create, including the file extension: ex: 'filename.txt': ")
print()

# Creating the complete path including both of the given directory path and filename from just above. 
complete_path = directory_path + file_name

# Asking the user for the necessary information for the assignment. Name, address, phone number.
name = input("Please enter your name: ")
address = input("Please enter your address: ")
phone_number = input("Please enter your phone number: ")

# Making a list including the personal info just provided, to easily call upon in the future.
info_list = [name, address, phone_number]

# Using a 'with open()' statement with the 'w' mode to create and write the contents to the new file. The text as requested should be entered in on a single line and each bit of content separated by a comma.
with open(complete_path, 'w') as fileHandle:
  fileHandle.write(", ".join(info_list))

# Using a 'with open()' statement with the 'r' mode to read the contents of the new file and print it out to the user using the variable 'print_file'.
with open(complete_path, 'r') as fileHandle:
  print_file = fileHandle.read()
  print()
  print("File Contents:")
  print()
  print(print_file)