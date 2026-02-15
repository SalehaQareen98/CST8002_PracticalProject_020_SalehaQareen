# CST8002_PracticalProject_020_SalehaQareen
Refactor or re-use your project started in Practical Project Part 1 to meet the following
requirements:
o Project has a layered design and implementation e.g. Presentation, Business, and
Persistence with record-objects (also known as Model or Entity objects) or uses a Model
View Controller framework. For example, all user interactions are via the Presentation
Layer, the sequential data structure in memory is within the Business Layer, and the File-IO
is within the Persistence Layer.
 Use a separate commit for each part of your layered architecture, or each part of
your MVC pattern as you develop them. The commit should briefly describe what
part was created.
 E.g., one commit for the model, one commit for the business layer (problem
domain), one for the presentation layer etc.
o Re-use your record object, or create one, (also known as entity object, data-transfer object)
that uses the column names from the dataset as part of the source code, e.g. variable
names, accessors/mutators names, or constants.
 Make sure you use a commit for this part.
o Use File-IO on startup to open and read the dataset, initializing one hundred record objects
with data parsed from the first one hundred records in the csv file. If there are fewer than
100 records in the dataset, use them all. The record objects should be stored in a simple
data structure (array or a list), use exception handling in case the file is missing or not
available.
 Use a commit after your file-IO logic is developed or updated.
o Displays your full name on screen so it always remains visible, or after each user
interaction.
o Provide the user the interactive options and functionality to:
 Reload the data from the dataset, replacing the in-memory data.
 Create a commit when this task is completed.
 Persist the data from memory to the disk as a comma-separated file, writing to a
new file. Research using a GUID or UUID using an API to generate the file name for
the output file. See [3].
 Create a commit when this task is completed.
 Select and display either one record or display multiple records from the in-memory
data.
 Create a commit when this task is completed.
 Create a new record and store it in the simple data structure in memory
 Create a commit when this task is completed.
 Select and edit a record held in the simple data structure in memory
 Create a commit when this task is completed.
 Select and delete a record from the simple data structure in memory
 Create a commit when this task is completed.
 Take a screen shot of your program performing each task above, ensuring your full name is within
each screen shot. E.g., print “Program by Your Name” replacing Your Name with your ACSIS
name every 10 records of output when displaying many records and / or as part of the menu
Page 2 of 8
system (or GUI or Web Page etc.) and include one to two sentences that describe what is
illustrated in the screen shot below each screen shot.
 Write a single unit-test as proof of concept using a testing framework to test one part of your
program. You should use a unit-testing framework with asserts or the equivalent.
o Unit-Test Examples (you would only do one test, or a similar test):
 Does the program read in records, placing data into correct fields of record objects?
 Does the program add a new record into the sequential data structure?
 Does the program update a record in the sequential data structure as expected?
 Does the program remove a record from the sequential data structure as expected?
 Does the program catch any exceptions or errors if the file is missing?
 Etc.
o Create a commit when this task is completed.
 Your program should use the programming concepts from practical project 01.
 Your program should also use the following new programming concepts: File-IO writing a csv file
using GUID or UUID as file name, unit testing, N-Layered or MVC architecture.