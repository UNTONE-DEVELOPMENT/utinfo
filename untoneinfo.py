import sys, os
import pathlib

print("UNTONE Project File Reader Version 1 (c) 2021 Matthew5pl")
f = open(sys.argv[1], 'r')
print("Printing info about project...")
rd = f.readlines()
print("Version is " + str(rd[0])[25:28] + ", ID is " + str(rd[2]).replace('ID : ', '') + "Name is " + str(rd[3]).replace('Name : ', '') + "Edition is " + str(rd[4]).replace('Edition : ', '') + "Genre is " + str(rd[6]).replace('Genre : ', '') + "Engine or Framework is " + str(rd[7]).replace('Engine/Framework : ', '') + "Language is " + str(rd[8]).replace('Language : ', '') + "The project directory is " + str(rd[9]).replace('Project Location : ', '') + "Created by " + str(rd[11]).replace('Creator : ', '') + "Copyright " + str(rd[12]).replace('Copyright : ', ''))
runpath = pathlib.Path(__file__).parent.absolute()
print("Printing parse results to" + str(runpath) + "/result.txt...")
fr = open(str(runpath) + "/result.txt", 'w')
fr.write("Version is " + str(rd[0])[25:28] + ", ID is " + str(rd[2]).replace('ID : ', '') + "Name is " + str(rd[3]).replace('Name : ', '') + "Edition is " + str(rd[4]).replace('Edition : ', '') + "Genre is " + str(rd[6]).replace('Genre : ', '') + "Engine or Framework is " + str(rd[7]).replace('Engine/Framework : ', '') + "Language is " + str(rd[8]).replace('Language : ', '') + "The project directory is " + str(rd[9]).replace('Project Location : ', '') + "Created by " + str(rd[11]).replace('Creator : ', '') + "Copyright " + str(rd[12]).replace('Copyright : ', ''))
print('done. ')
