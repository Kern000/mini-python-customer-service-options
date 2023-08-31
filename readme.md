Python Project Documentation

This is project one for BELLS SG basic python course for business automation.

===== Requirements =====

This is a python application that allows the admin user to navigate between methods to create, read, update, delete and export the customers' collected information.

Functional Requirements

FR1.1: The system allows users to create a new customer entry.

FR1.1.1: Each new customer entry must be filled in and cannot be left blank, and the input must match the required structure.

FR1.2: The system allows users to list the existing customers entries.

FR1.3: The system allows users to search for a customer entry.

FR1.4: The system allows users to update a customer entry.

FR1.4.1: Each new customer entry must be filled in and cannot be left blank, and the input must match the required structure.

FR1.5: The system allows users to delete a customer entry.

FR1.6: The system allows users to save and export the list of customer entries into a file on local storage.

FR1.7: The system allows user to load a list from file into the application to add on to existing data or to modify it.

FR1.7.1: The file type must be .json and the file must exist in the same folder where program is runned.

Non-Functional Requirements

NFR2.1: Security - user input is validated based on datatype and size. This prevents cross-site scripting and poor data entry.

Task Attributes

NFR3.1: Accessibility - users are given the choice to confirm their input or to reinput them when there are mistakes in data entry.

NFR3.2: Accessibility - users only exit a function when they choose to, allowing them to continue working on a similar type of task repeatedly.

NFR3.3: Accessibility - users error allows the application to continue operating and users can continue to navigate within the application seamlessly.

NFR3.4: Error catching - errors in uploading files like uploading unsupported file types are caught and prevents the application from breaking.

===== Design =====

Python is chosen due to the ease of input validation. Python's "re" package allow easy use of regex matching to perform user input validation, which is the prevalent operation in this application.

Procedural programming is employed, breaking down the application's operations into small functions to perform tasks in bitesize, efficient manners. This can be implemented because users may not need to create, update, and delete within a single workflow.

This allows the user and the application to run only the necessary functions and operations for their intentions and purpose.

Additionally, functional programming is also employed.

Functions that are often utilized across different operations were refactored into reuseable functions, and in some instances, higher order functions.

Specifically, the return_choice function accepts a core operation function as an argument, allowing restarting or exiting of an operation when a process needs to be restarted or cut short as it is more efficient to do so.

PEP8 is adhered to. Each line of code is kept short and concise. Functions and variables are written in descriptive manners.
In other words, functions are verbs that are descriptive of an action. Variables are descriptive of the value and datatype they hold.

====== UI/UX ======

The application can be seamlessly navigated with the typing of short y/n letters or a single numeric number.
Important confirmations, like the overwriting or appending of data during uploading operations, require the user to type 'append' or 'overwrite' to confirm their intentions.

====== Testing ======

Unit Test One: Add new customer and Search for added customer

-- Outcome 1 --

Function Tested: add_new_customer

Name of Test: Add new customer and Search for added customer

Input:

Press 3 to Add customer entry

Input: Enter 'Alex Goh' for name

Input: Enter 'alexgoh@gmail.com' for email

Input: 99090238 for phone_number

Expected Output:

Input data is printed on terminal:

Entered Particulars:

name: Alex Goh

email: alexgoh@gmail.com

phone_number: 99090238

press y to confirm customer details.

On main terminal, press 2. Input: Alex Goh (with matching case) and it should display the same.

-- Outcome 2 --

Function Tested: add_new_customer

Name of Test: Add new customer and Search for added customer

Input:

Press 3 to Add customer entry

Try to add the following customer details:
'Alex Goh 5'
'alexgod.com'
+6590909090

Expected Output: prompt user for reentry of the data, guiding user on the correct information to enter.

=========

Unit Test Two: Testing file loading

-- Outcome 1 --

Function Tested: load_data

Name of Test: loading data of required file type

Input:
Enter meow.csv (an unsupported file format)

Expected Output: console prints 'unsupported file format' and prompts reinput or return main page.

-- Outcome 2 --

Function Tested: load_data

Name of Test: loading data of required file type

Input: Enter meow.json (a non-existent file name)

Expected Output: console will print 'file not found' and prompt reinput or return to main.

====== Two Possible Enhancements ======

1. Login system can be implemented to allow authentication and authorization.

2. Indexing can be implemented for search to allow high performance when large datasets are expected.

Thank you for reading.
