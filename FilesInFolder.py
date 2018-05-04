import os

#change this to a folder that has some files
folderName = 'D:\Folder'
for file in os.listdir(folderName):
  print file
