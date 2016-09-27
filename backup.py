######################## python program to back up files  ################################
###
#Name: Parth Patel
#Date: 27/9/2016
###

#import required modules
import sys
import os
import time  

#take path of source file as input...
##eg
# on windows  "C:\\MyDocuments\\myfile"
# on linux '/Karma/Desktop/myfile.txt'
source = [input("Enter path of file to be backed up ")]

#take path of backup directory as input.
target_dir	= input("Enter path of target Directory/Folder ")

# if path does not exist create directory

if not os.path.exists(target_dir):
    print('Given Directory doesn\'t exist.\nCreating new directory...')
    os.mkdir(target_dir)
    print('Directory created successfully...')

    
#backing up file in zip file
#name of file will have date and time of backup
#if you want you can add comment to it's name as to distinguish your backup file
today	=	target_dir + os.sep	+ time.strftime('%d%m%Y')
now  = time.strftime('%H%M%S')
comment = input('Enter comment --->')   # comment is optional

if(len(comment) == 0):
    target	= today + os.sep + now + '.zip'
else:
    target	=	today + os.sep + now + '_' + comment + '.zip'
#	Create	the	subdirectory	if	it	isn't	already	there
if	not	os.path.exists(today):
    os.mkdir(today)
    print('Successfully	created	directory',	today)


zip_command = "zip	-r	{0}	{1}".format(target,''.join(source))

#	Run	the	backup
print("Zip	command	is: ")
print(zip_command)
print("Running: ")
if	os.system(zip_command)	==	0:
	print('Successful	backup	to',	target)
else:
    print('Backup	FAILED')
