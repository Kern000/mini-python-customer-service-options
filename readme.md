Python Project Documentation

This is project one for BELLS SG basic python course for business automation.

===== Requirements =====

This is a python application that allows the admin user to navigate between methods to create, read, update, delete and export the customers' collected information.

Functional Requirements
FR1.1: The system allows users to create a new customer entry.
FR1.2: The system allows users to list the existing customers entries.
FR1.3: The system allows users to search for a customer entry.
FR1.4: The system allows users to update a customer entry.
FR1.5: The system allows users to delete a customer entry.
FR1.6: The system allows users to save and export the list of customer entries into a file on local storage.
FR1.7: The system allows user to load a list from file into the application to add on to existing data or to modify it.

Non-Functional Requirements
NFR2.1: Security - user input is validated based on datatype and size. This prevents cross-site scripting and poor data entry.

Task Attributes
NFR3.1: Accessibility - users are given the choice to confirm their input or to reinput when there are mistakes in data entry.
NFR3.2: Accessibility - users only exit a function when they choose to, allowing them to continue working on a similar type of task repeatedly.
NFR3.3: Accessibility - users error allows the application to continue operating and users can continue to navigate within the application seamlessly.
NFR3.4: Error catching - errors in uploading files like uploading unsupported file types are caught and prevents the application from break.

===== Design =====
Python is chosen due to the ease of input validation. Python's "re" package allow easy use of regex matching to perform user input validation, the prevalent operation in this application.
Procedural programming is employed, breaking down the application's operations into small functions to perform tasks in bitesize, efficient manners. This can be implemented because users may not need to create, update, and delete within a single workflow.
This allows the user and the application to run only the necessary functions and operations for their intentions and purpose.

Additionally, functional programming is also employed.

Functions that are often utilized across different operations were refactored into reuseable functions, and in some instances, higher order functions.
Specifically, the return_choice function accepts a core operation function as an argument, allowing restarting or exiting of an operation when a process needs to be restarted or cut short as it is more efficient to do so.

PEP8 is adhered to. Each line of code is kept short and concise. Functions and variables are written in descriptive manners.
In other words, functions are verbs that are descriptive of an action. Variables are descriptive of the value and datatype they hold.

====== UI/UX ======

The application can be seamlessly navigated with the typing of short y/n letters or single numeric number.
Important confirmations, like the overwriting or appending of data during uploading operations, require the user to type 'append' or 'overwrite' to confirm their intentions.

====== Testing ======

Test Case 1
== Success Case ==
Press 3 to Add customer entry:
key in:
Alex Goh
alexgoh@gmail.com
99090238

Expected:
Confirmation printed on terminal. It should display:
Alex Goh
alexgoh@gmail.com
99090238
press y to save customer details.

On main terminal, press 2. to search for Alex Goh (with matching case) and it should display the same.

Test Case 2
== Failure case for testing validation ==
Try to add the following customer details:
Alex Goh 5
alexgod.com
+6590909090

Expected Output: It should prompt for reentry of the data, guiding user on the correct information to enter.

Test Case 3
== Testing for the loading of wrong data type ==
Enter meow.csv (an unsupported file format) -> Expected: it will inform unsupported file format
Enter meow.json (a non-existent file name) -> Expected: After choosing append or overwrite, it will detect if file exist. Since it does not, it will inform file not found.

---

Thank you for reading.
