# INET 4031 Add User Script (Python)
  
**Python Script for Adding Users/Groups to a System**
  
## Description
  
For this lab we created a python script that reads from a create-user input file which contians a list 
of users and this script then uses the data form the input file to create and add users to each system. 
The regular expression re.match(r'^#', line) is used to match a pattern in the input file. In this script, it checks if the line starts with a # character. If a match is found, the line is skipped and the script moves on to the next iteration.
The imports that were used in the script are os, re, and sys. These are all important because: 

os: provides a way to use operating system-dependent functionality. It is used in this script to execute system commands.

re: provides support for regular expressions. It is used in this script to perform pattern matching using regular expressions.

sys: provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter. It is used in this script to read input from the command line.


  
## Operation
  
### Input File Specification
  
The input file should have the following format:

*** username:default_password:last_name:first_name:comma_separated_list_of_groups

For example:

jdoe11:mypass:Doe:John:admins, reviewers

The name of the input file is up to the user.  Convention is create-users.input

### Running the Script
Before you run the script make sure have python 3 installed. In order to run this code open a terminal and ensure that you are in the correct directory and that both the python script create-users and create-users.input are in the directory, you then can either run the command
sudo ./create-users.py < create-users.input  or $ cat create-users.input | sudo ./create-users.py either command will work as both commands use the contents from the input file as an input to the 
python script. 

