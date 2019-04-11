# CLOCRepo
Repo containing files necessary to run the CxCmdLineCounter script.

CLOC.py will take user input to determine a specified github repository.  It will then attempt to clone that repo if a local one does not already exist.  This repo will be scanned using the CLOC procedure to generate a number representing the lines of code.  It will then create an output file, attach it to an email specified by the user, and send the email to a recipient also specified by the user. 

Usage: ./CLOC.py

C:\User ./CLOC.py

Please enter your email address: <user's email address>

Type your password and press enter: <user's email password>

Please enter the receiving email address: <recipient email address>
  
Enter the UR for the desired Github respository: <Github URL>
  
Enter the name of the branch you would like to scan: <branch name>
