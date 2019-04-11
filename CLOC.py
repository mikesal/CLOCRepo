import subprocess as sp
import getpass as gp
import os, ssl, shutil, sys, pip, shutil, smtplib

#Methods/Libraries needed to send email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail():
	msgBody = "This is an automated e-mail.  Attached is a CLOC report of the following Github repo: " + getRepoFromURL()
	subject = "CLOC report"
	#Use MIMEMultipart to fill in email fields
	email = MIMEMultipart()
	email['Subject'] = subject
	email['From'] = emailOut
	email['To'] = destEmail
	email.attach(MIMEText(msgBody, "plain"))
	
def CLOCRepo():
	#Clone repository if it doesn't already exist
	if not os.path.exists(currentLocalDir+repo):
		git.Repo.clone_from(repoURL, currentLocalDir)
		#Repo is not recognized. Stops script from running here.

	#use git to pull from repo
	#access clocExe... perform CLOC on current directory
	#Create output file
	
#Parses the repo name from the given URL
def getRepoFromURL():
	return(repoURL[repoURL.rfind('/')+1:repoURL.rfind('.')])

#Globals
port = 587
clocExe = 'CxCmdLineCounter.exe'
currentLocalDir = "C:\\Users\michael\Desktop\Python"

#git install required 
try:
	import git
except ImportError:
	install('git')

#Get input from user
emailOut = input("Please enter your email address: ")
#getpass keeps the output of the keyboard hidden from the console.
password = gp.getpass(prompt='Type your password and press enter: ', stream=None)
destEmail = input("Please enter the receiving email address: ")
repoURL = input("Enter the URL for the desired Github repository: ")
branch = input("Enter the name of the branch you would like to scan: ")

#Start CLOC procedure
repo = getRepoFromURL()
testFile = repo+"_CLOC"+".txt"
CLOCRepo()
sendMail()
#End procedure
