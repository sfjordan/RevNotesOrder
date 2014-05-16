#!/usr/bin/python

import sys
import re

#get arguments
if (len(sys.argv)!=2):
	print("---")
	print("Usage: NoteOrderFlipper your_notes_file.html")
	print("---")
	sys.exit(0)
else:
	arg1 = sys.argv[1]
	arg2 = "FLIPPED_"+arg1

print "flipping...   ",
f = open(arg1,"r")
newf = open(arg2,"w")

fullstr = f.read()
list = re.split('<table width="100%"',fullstr)

#deal with first items
firstItems = list[0].split('body>')
headerstr = firstItems[0]+'body>'

#get title of first note from header
title = headerstr.split('<title>')[1].split('</title>')[0]

#fix the first note
firstNoteStr = firstItems[1]
firstNoteStr = ' bgcolor="#D4DDE5" border="0"><tr><td><h1>'+title+'</h1></td></tr></table>'+firstNoteStr
list[0] = firstNoteStr

#fix the html
noteList = []
for item in list:
	str = ""
	if "bgcolor=" in item:
		str = '<table width="100%"'+item
	else:
		str = item
	noteList.append(str)

#flip it!
noteList.reverse()

#write it!
newf.write(headerstr)
for note in noteList:
	newf.write(note)
f.close()
newf.close()
print("Done.")