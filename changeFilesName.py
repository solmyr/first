#! /bin/python

import os, glob, sys, shutil

path = os.getcwd()

newExt = 'log'

argc = len(sys.argv)

if(argc > 1) :
    path = sys.argv[1]

if(argc > 2) :
    newExt = sys.argv[2]

for file in glob.glob(os.path.join(path, "*")) :
    #path = os.path.dirname(file)
    #filename = os.path.basename(file)
    name, ext = os.path.splitext(file)
    print "name: " + name + "\text: " + ext
    newFileName = name + '.' + newExt
    if file == newFileName :
	continue
    #os.mkdir("..\logFiles");
    #shutil.copyfile(file, "../logFiles/" + newFileName)
    os.rename(file, newFileName)

