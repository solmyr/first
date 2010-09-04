#! /bin/python

import os, glob

path = r'/home/solmyr/python/changeFilesName/test'

for file in glob.glob(os.path.join(path, "*")) :
    name, ext = os.path.splitext(file)
    print "name: " + name + "\text: " + ext
    newFileName = name + '.log'
    os.rename(file, newFileName)

